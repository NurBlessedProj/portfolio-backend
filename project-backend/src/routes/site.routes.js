const express = require('express');
const router = express.Router();
const Site = require('../models/Site');
const upload = require('../middleware/upload');
const hostingService = require('../services/hosting');
const auth = require('../middleware/auth');

// Create new site
router.post('/', auth, async (req, res) => {
  try {
    const { name, subdomain } = req.body;
    
    // Check if subdomain exists
    const existingSite = await Site.findOne({ subdomain });
    if (existingSite) {
      return res.status(400).json({ error: 'Subdomain already taken' });
    }

    const site = new Site({
      name,
      subdomain,
      userId: req.user.id
    });

    await site.save();
    res.status(201).json(site);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Upload site files
router.post('/:siteId/upload', auth, upload.fields([
  { name: 'html', maxCount: 1 },
  { name: 'css', maxCount: 1 },
  { name: 'js', maxCount: 1 },
  { name: 'assets', maxCount: 10 }
]), async (req, res) => {
  try {
    const site = await Site.findOne({ _id: req.params.siteId, userId: req.user.id });
    if (!site) {
      return res.status(404).json({ error: 'Site not found' });
    }

    // Upload code files to S3
    const codeFiles = ['html', 'css', 'js'];
    for (const fileType of codeFiles) {
      if (req.files[fileType]) {
        const file = req.files[fileType][0];
        const result = await hostingService.uploadToS3(file, site.subdomain, fileType);
        
        // Delete old file if exists
        if (site.files[fileType]?.key) {
          await hostingService.deleteFromS3(site.files[fileType].key);
        }
        
        site.files[fileType] = result;
      }
    }

    // Upload assets to Cloudinary
    if (req.files.assets) {
      for (const asset of req.files.assets) {
        const result = await hostingService.uploadToCloudinary(asset);
        site.assets.push({
          originalName: asset.originalname,
          ...result
        });
      }
    }

    site.lastUpdated = Date.now();
    await site.save();
    res.json(site);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get site details
router.get('/:siteId', auth, async (req, res) => {
  try {
    const site = await Site.findOne({ _id: req.params.siteId, userId: req.user.id });
    if (!site) {
      return res.status(404).json({ error: 'Site not found' });
    }
    res.json(site);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Delete site
router.delete('/:siteId', auth, async (req, res) => {
  try {
    const site = await Site.findOne({ _id: req.params.siteId, userId: req.user.id });
    if (!site) {
      return res.status(404).json({ error: 'Site not found' });
    }

    // Delete all files from S3
    for (const fileType in site.files) {
      if (site.files[fileType]?.key) {
        await hostingService.deleteFromS3(site.files[fileType].key);
      }
    }

    // Delete all assets from Cloudinary
    for (const asset of site.assets) {
      await hostingService.deleteFromCloudinary(asset.cloudinaryId);
    }

    await site.remove();
    res.json({ message: 'Site deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
