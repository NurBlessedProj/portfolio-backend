const { Router } = require("express");
const router = Router();
const indexController = require("../controller/index.controller");
const ContactMiddleware = require("../middlewares/index.middleware");

router.get("/contact", indexController.contact);
router.get("/contact/:id", indexController.contactById);
router.put("/contact/:id", indexController.UpdateContactById);
router.delete("/contact/:id", indexController.deleteUserById);
router.get("/contacts/sort/:sortBy", indexController.sortAllContact);
router.post(
  "/contact/create",
  ContactMiddleware.verifyBeforeCreation,
  indexController.addContact
);

module.exports = router;
