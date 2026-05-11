
const MovieService = require(
    "../business_layer/movieService"
)

const service = new MovieService()

exports.index = (req, res) => {

    service.storage.getAll((movies) => {

        res.render("index", { movies })
    })
}

exports.showAdd = (req, res) => {

    res.render("add")
}

exports.add = (req, res) => {

    service.storage.add(req.body, () => {

        res.redirect("/")
    })
}

exports.showEdit = (req, res) => {

    service.storage.getById(
        req.params.id,
        (movie) => {

            res.render("edit", { movie })
        }
    )
}

exports.edit = (req, res) => {

    const movie = {

        id: req.params.id,

        ...req.body
    }

    service.storage.update(movie, () => {

        res.redirect("/")
    })
}

exports.delete = (req, res) => {

    service.storage.delete(
        req.params.id,
        () => {

            res.redirect("/")
        }
    )
}