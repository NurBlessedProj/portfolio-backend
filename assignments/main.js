const express = require("express");
const app = express();
const port = 3000;
const indexRoute = require("./routes/index.route");
app.use(express.json());



app.use("/", indexRoute);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
