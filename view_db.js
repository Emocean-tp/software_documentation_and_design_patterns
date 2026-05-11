
const sqlite3 = require("sqlite3").verbose()

const db = new sqlite3.Database("./imdb.db")

db.all(
    "SELECT * FROM movies",
    [],
    (err, rows) => {

        console.log(rows)
    }
)