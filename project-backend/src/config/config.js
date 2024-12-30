module.exports = {
  allowedFileTypes: {
    code: ['.html', '.css', '.js'],
    assets: ['.jpg', '.jpeg', '.png', '.gif', '.svg']
  },
  maxFileSize: 5 * 1024 * 1024, // 5MB
  aws: {
    region: process.env.AWS_REGION,
    bucketName: process.env.AWS_BUCKET_NAME
  },
  cloudinary: {
    cloudName: process.env.CLOUDINARY_CLOUD_NAME,
    apiKey: process.env.CLOUDINARY_API_KEY,
    apiSecret: process.env.CLOUDINARY_API_SECRET
  }
};
