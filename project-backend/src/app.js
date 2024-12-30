require("dotenv").config();
const express = require("express");
const app = express();
const cors = require("cors");
const mongoose = require("mongoose");
const multer = require("multer");
mongoose
  .connect(process.env.MONGODB_URL)
  .then(() => {
    
    
    app.use(cors());
    app.use(express.json());
    
    const sitesRouter = require('./routes/sites');
    const authRoute = require("./routes/auth.routes");
    
    //ROUTES
    app.use('/api/sites', sitesRouter);
    app.use("/auth", authRoute);

    console.log("Connected to MONGO DB");
    app.listen(process.env.PORT, () => {
      console.log(`Server is running on port ${process.env.PORT}`);
    });
  })
  .catch((err) => {
    console.error("Error connecting to MONGO DB", err);
  });
