
const sqlite3 = require("sqlite3").verbose()

const db = new sqlite3.Database("./imdb.db")

db.serialize(() => {

    db.run(`
        CREATE TABLE IF NOT EXISTS movies (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,
            genre TEXT,
            director TEXT,
            rating REAL,
            releaseYear INTEGER
        )
    `)
})

module.exports = db