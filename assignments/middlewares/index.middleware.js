const verifyBeforeCreation = (req, res, next) => {
  const { name, email, phone } = req.body;
  if (!name || !email || !phone) {
    return res
      .status(400)
      .json({ error: true, message: "Name, email, and phone are required." });
  }
  next();
};

module.exports = {verifyBeforeCreation}