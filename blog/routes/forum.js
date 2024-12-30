var express = require("express");
var router = express.Router();

/* GET forum page page. */
router.get("/", function (req, res, next) {
  const data = [
    {
      title: "hello world",
      content: "ZASDF",
      author: "fghjop",
    },
    {
      title: "hello world2",
      content: "ZASDFwd",
      author: "fghjop23e",
    },
    {
      title: "hello world3",
      content: "ZASDFqwe",
      author: "fghjopqwewer",
    },
  ];
  res.render("forum", {data});
});

module.exports = router;
