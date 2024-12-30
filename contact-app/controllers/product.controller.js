const Product = require("../models/Product");

const addProduct = async (req, res) => {
  const { name, description, price } = req.body;

  try {
    const existingProduct = await Product.findOne({ name });
    if (existingProduct) {
      return res.send("Product already exists");
    }

    const newProduct = new Product({
      name,
      description,
      price,
    });

    await newProduct.save();

    res.redirect("/products?message=Product created successfully");
  } catch (error) {
    res.status(500).json({
      error: true,
      message: "An error occurred while adding the product",
    });
  }
};
const updateProduct = async (req, res) => {
  try {
    const { name, description, price } = req.body;
    await Product.findByIdAndUpdate(req.params.id, {
      name,
      description,
      price,
    });
    res.redirect("/products");
  } catch (error) {
    next(error);
  }
};
const deleteProduct = async (req, res) => {
  try {
    const id = req.params.id;
    await Product.findByIdAndDelete(id);
    res.redirect("/products?message=Product Deleted successfully");
  } catch (error) {
    console.log(error);
  }
};

const getProducts = async (req, res) => {
  try {
    const products = await Product.find();
    return products;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error; 
  }
};
module.exports = { addProduct, getProducts, updateProduct, deleteProduct };
