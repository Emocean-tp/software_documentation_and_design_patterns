
const MovieStorage = require(
    "../data_access_layer/movieStorage"
)

class MovieService {

    constructor() {

        this.storage = new MovieStorage()
    }
}

module.exports = MovieService