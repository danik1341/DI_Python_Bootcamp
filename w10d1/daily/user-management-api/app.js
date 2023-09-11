const express = require("express");
const app = express();
const port = 5000;
const authRoutes = require("./routes/auth");
const userRoutes = require("./routes/users");

app.use(express.json());

app.use("/api/auth", authRoutes);
app.use("/api/users", userRoutes);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
