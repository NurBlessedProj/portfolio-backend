const Profile = require("../models/profile.model");
const User = require("../models/user.model");
const authService = require("../services/auth.service");

const verifyRegister = (req, res, next) => {
  const { name, email, password } = req.body;
  if (!name || !email || !password) {
    res.json({
      message: "please fill in all info",
    });
    return;
  }
  next();
};

const loginMiddleware = async (req, res, next) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({
      error: true,
      message: "Email and password are required",
    });
  }

  const user = await User.findOne({ email });
  if (!user) {
    return res.status(404).json({
      error: true,
      message: "Email not found",
    });
  }

  const isMatch = await authService.hashCompare(password, user.password);
  if (!isMatch) {
    return res.status(400).json({
      error: true,
      message: "Incorrect password",
    });
  }

  const token = await authService.generateToken(user._id);

  req.token = token;
  req.user = user;

  next();
};


module.exports = { verifyRegister , loginMiddleware};
