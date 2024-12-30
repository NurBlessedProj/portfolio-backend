const { Router } = require("express");
const router = Router();

const authController = require("../controllers/auth.controller");
const authMiddleware = require("../middlewares/auth.middleware");

router.post(
  "/register",
  authMiddleware.verifyRegister,
  authController.register
);
router.post("/login", authMiddleware.loginMiddleware, authController.login);

module.exports = router;
