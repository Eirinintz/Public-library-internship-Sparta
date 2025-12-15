const express = require("express");
const multer = require("multer");
const xlsx = require("xlsx");
const { Pool } = require("pg");
const path = require("path");

const app = express();

// για να σερβίρει το index.html
app.use(express.static("public"));

// multer (κρατάμε το excel στη μνήμη)
const upload = multer({ storage: multer.memoryStorage() });

// postgres
const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "db",
  password: "",
  port: 5432
});

app.post("/upload", upload.single("file"), async (req, res) => {
  try {
    const workbook = xlsx.read(req.file.buffer);
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    const data = xlsx.utils.sheet_to_json(sheet);

    for (const row of data) {
      await pool.query(
        "INSERT INTO excel_data(name, age, salary) VALUES ($1,$2,$3)",
        [row.name, row.age, row.salary]
      );
    }

    res.send("Upload completed!");
  } catch (err) {
    console.error(err);
    res.status(500).send("Error");
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
