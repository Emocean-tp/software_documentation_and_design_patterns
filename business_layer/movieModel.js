
class AppModel {

    constructor(
        id,
        title,
        category,
        developer,
        rating,
        downloads
    ) {

        this.id = id
        this.title = title
        this.category = category
        this.developer = developer
        this.rating = rating
        this.downloads = downloads
    }
}

module.exports = AppModel