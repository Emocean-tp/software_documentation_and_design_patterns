
const db = require("./db")

class MovieStorage {

    getAll(callback) {

        db.all(
            "SELECT * FROM movies",
            [],
            (err, rows) => {

                if (err) {

                    console.log(err)

                    callback([])

                    return
                }

                callback(rows)
            }
        )
    }

    getById(id, callback) {

        db.get(
            "SELECT * FROM movies WHERE id = ?",
            [id],
            (err, row) => {

                if (err) {

                    console.log(err)

                    callback(null)

                    return
                }

                callback(row)
            }
        )
    }

    add(movie, callback) {

        db.run(
            `
            INSERT INTO movies
            (
                title,
                genre,
                director,
                rating,
                releaseYear
            )
            VALUES (?, ?, ?, ?, ?)
            `,
            [
                movie.title,
                movie.genre,
                movie.director,
                movie.rating,
                movie.releaseYear
            ],
            callback
        )
    }

    update(movie, callback) {

        db.run(
            `
            UPDATE movies

            SET
                title = ?,
                genre = ?,
                director = ?,
                rating = ?,
                releaseYear = ?

            WHERE id = ?
            `,
            [
                movie.title,
                movie.genre,
                movie.director,
                movie.rating,
                movie.releaseYear,
                movie.id
            ],
            callback
        )
    }

    delete(id, callback) {

        db.run(
            "DELETE FROM movies WHERE id = ?",
            [id],
            callback
        )
    }
}

module.exports = MovieStorage