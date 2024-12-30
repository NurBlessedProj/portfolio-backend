require("dotenv").config();
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const hashPassword = async (password) => {
  const hashedPassword = await bcrypt.hash(password, 12);
  return hashedPassword;
};
const hashCompare = async (value, hash) => {
  try {
    return await bcrypt.compare(value, hash);
  } catch (err) {}
};
const generateToken = async (userId) => {
  const token = jwt.sign({ userId }, process.env.JWT_SECRET, {
    expiresIn: "30d",
  });
  return token;
};
module.exports = {
  hashPassword,
  hashCompare,
  generateToken,
};
