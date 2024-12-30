const Product = require("../models/Product");
var express = require("express");
var router = express.Router();
const productController = require("../controllers/product.controller");
/* GET home page. */
router.get("/", function (req, res, next) {
  res.render("index", {
    title: "Homepage",
    intro: "This is Home page",
  });
});

// assignment

router.get("/add_products", function (req, res, next) {
  res.render("add_products", {
    title: "Add Products",
    intro: "This is add Products Page",
  });
});

router.get("/products", async function (req, res, next) {
  try {
    const products = await productController.getProducts(req, res);
    res.render("products", {
      title: "Products",
      intro: "This is Products Page",
      products: products,
      query: req.query,
    });
  } catch (error) {
    next(error);
  }
});

router.get("/products/update/:id", async function (req, res, next) {
  try {
    const product = await Product.findById(req.params.id);
    res.render("update_products", { product });
  } catch (error) {
    next(error);
  }
});


router.post("/add_products/add", productController.addProduct);
router.post("/products/update/:id", productController.updateProduct);
router.post("/products/delete/:id", productController.deleteProduct);

module.exports = router;
