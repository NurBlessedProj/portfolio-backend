var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function (req, res, next) {
  const info = {
    title: "Contact Us",
    intro: "This is contact us page",
  };
  res.render("contact", info);
});
// router.post()

module.exports = router;
