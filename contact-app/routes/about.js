var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function (req, res, next) {
  const info = {
    title: "About Us",
    intro: "This is about us page",
  };
  res.render("about", info);
});

module.exports = router;
