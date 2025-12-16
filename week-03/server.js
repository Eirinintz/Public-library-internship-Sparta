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
  password: "", // ή το πραγματικό σου password
  port: 5432
});

app.post("/upload", upload.single("file"), async (req, res) => {
  try {
    const workbook = xlsx.read(req.file.buffer);
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    const data = xlsx.utils.sheet_to_json(sheet);

    for (const row of data) {
      await pool.query(
        `INSERT INTO books(
          arithmos_eisagogis,
          hmerominia_eisagogis,
          syggrafeas,
          syggrafeas_kona,
          titlos,
          ekdotis,
          ekdosi,
          etos,
          topos_ekdosis,
          sxhma,
          selides,
          tomos,
          tropos_promitheias,
          isbn,
          stili1,
          stili2
        ) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16)`,
        [
          row['ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'],
          row['ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ'],
          row['ΣΥΓΓΡΑΦΕΑΣ'],
          row['ΣΥΓΓΡΑΦΕΑΣ ΚΟΝΑ'],
          row['ΤΙΤΛΟΣ'],
          row['ΕΚΔΟΤΗΣ'],
          row['ΕΚΔΟΣΗ'],
          row['ΕΤΟΣ'],
          row['ΤΟΠΟΣ ΕΚΔΟΣΗΣ'],
          row['ΣΧΗΜΑ'],
          row['ΣΕΛΙΔΕΣ'],
          row['ΤΟΜΟΣ'],
          row['ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ'],
          row['ISBN'],
          row['ΣΤΗΛΗ1'],
          row['ΣΤΗΛΗ2']
        ]
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
