
const path = require("path");
const express = require("express");
const { request } = require("express");
const app = express()

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html");
});

app.get("/real-data/public/index.html", function(req, res){
    res.sendFile(__dirname + "/real-data/public/index.html");
});

app.listen(3000);