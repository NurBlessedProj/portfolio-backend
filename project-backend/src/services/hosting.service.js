const s3 = require('../config/aws');
const cloudinary = require('../config/cloudinary');
const config = require('../config/config');

class HostingService {
  async uploadToS3(file, subdomain, fileType) {
    const key = `sites/${subdomain}/${fileType}/${Date.now()}-${file.originalname}`;
    
    const params = {
      Bucket: config.aws.bucketName,
      Key: key,
      Body: file.buffer,
      ContentType: file.mimetype,
      ACL: 'public-read'
    };

    const result = await s3.upload(params).promise();
    return {
      key: result.Key,
      url: result.Location
    };
  }

  async uploadToCloudinary(file) {
    return new Promise((resolve, reject) => {
      const uploadStream = cloudinary.uploader.upload_stream(
        {
          folder: 'site-assets',
        },
        (error, result) => {
          if (error) reject(error);
          else resolve({
            cloudinaryId: result.public_id,
            url: result.secure_url
          });
        }
      );

      uploadStream.end(file.buffer);
    });
  }

  async deleteFromS3(key) {
    const params = {
      Bucket: config.aws.bucketName,
      Key: key
    };
    return s3.deleteObject(params).promise();
  }

  async deleteFromCloudinary(publicId) {
    return cloudinary.uploader.destroy(publicId);
  }
}

module.exports = new HostingService();
