const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const pool = require("../config/db");

exports.register = async (req, res) => {
  try {
    const { email, username, password } = req.body;

    const hashedPassword = await bcrypt.hash(password, 10);

    const addUserQuery = {
      text: "INSERT INTO users (email, username) VALUES ($1, $2) RETURNING id",
      values: [email, username],
    };

    const result = await pool.query(addUserQuery);

    const addHashedPasswordQuery = {
      text: "INSERT INTO hashpwd (username, password) VALUES ($1, $2)",
      values: [username, hashedPassword],
    };

    await pool.query(addHashedPasswordQuery);

    res.json({ message: "Registration successful" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};

exports.login = async (req, res) => {
  try {
    const { username, password } = req.body;

    const getPasswordQuery = {
      text: "SELECT password FROM hashpwd WHERE username = $1",
      values: [username],
    };

    const result = await pool.query(getPasswordQuery);

    if (result.rows.length === 0) {
      return res.status(401).json({ error: "Authentication failed" });
    }

    const hashedPassword = result.rows[0].password;

    const passwordMatch = await bcrypt.compare(password, hashedPassword);

    if (!passwordMatch) {
      return res.status(401).json({ error: "Authentication failed" });
    }

    const token = jwt.sign({ username }, "your_secret_key", {
      expiresIn: "1h",
    });

    res.json({ token });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};
