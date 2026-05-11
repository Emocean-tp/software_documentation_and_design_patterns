
const express = require("express")
const bodyParser = require("body-parser")
const path = require("path")

const app = express()

const movieRoutes = require("./routes/movieRoutes")

app.set("view engine", "ejs")

app.set(
    "views",
    path.join(__dirname, "view_layer/views")
)

app.use(bodyParser.urlencoded({ extended: true }))

app.use(
    express.static(
        path.join(__dirname, "view_layer/public")
    )
)

app.use("/", movieRoutes)

app.listen(3000, () => {

    console.log(
        "Server started: http://localhost:3000"
    )
})