const Profile = require("../models/profile.model");
const User = require("../models/user.model");
const authService = require("../services/auth.service");

const register = async (req, res) => {
  const { name, email, password } = req.body;
  const user = await User.findOne({ email });
  if (user) {
    res.json({
      error: true,
      message: "Email already exists",
    });
  }
  const hashedPassword = await authService.hashPassword(password);
  const newUser = new User({
    name,
    email,
    password: hashedPassword,
  });
  const userProfile = new Profile({
    user: newUser._id,
    avatar: "",
    bio: "",
  });
  await newUser.save();
  await userProfile.save();

  res.status(201).json({
    error: false,
    message: "Registeration succesfull",
    user: newUser,
  });
};
const login = async (req, res) => {
  const { user, token } = req;

  res.json({
    error: false,
    message: "User logged in successfully",
    token,
  });
};

module.exports = { login };

module.exports = {
  register,
  login,
};
