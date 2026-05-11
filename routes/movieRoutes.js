
const express = require("express")

const router = express.Router()

const controller = require(
    "../controller_layer/movieController"
)

router.get("/", controller.index)

router.get("/add", controller.showAdd)

router.post("/add", controller.add)

router.get("/edit/:id", controller.showEdit)

router.post("/edit/:id", controller.edit)

router.get("/delete/:id", controller.delete)

module.exports = router