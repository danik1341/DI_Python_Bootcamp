const pool = require("../config/db");

exports.getAllUsers = async (req, res) => {
  try {
    const getUsersQuery = "SELECT * FROM users";
    const result = await pool.query(getUsersQuery);

    res.json(result.rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};

exports.getUserById = async (req, res) => {
  try {
    const userId = req.params.id;
    const getUserQuery = {
      text: "SELECT * FROM users WHERE id = $1",
      values: [userId],
    };

    const result = await pool.query(getUserQuery);

    if (result.rows.length === 0) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};

exports.updateUserById = async (req, res) => {
  try {
    const userId = req.params.id;
    const { email, username, first_name, last_name } = req.body;

    const updateUserQuery = {
      text: "UPDATE users SET email = $1, username = $2, first_name = $3, last_name = $4 WHERE id = $5",
      values: [email, username, first_name, last_name, userId],
    };

    await pool.query(updateUserQuery);

    res.json({ message: "User updated successfully" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};
