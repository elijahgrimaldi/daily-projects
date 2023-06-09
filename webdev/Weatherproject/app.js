const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.urlencoded({extended : true}))
app.get("/", function(req,res){
    res.sendFile(__dirname + "/index.html")
})

app.post("/", function(req,res){
    const query = req.body.cityName
    const apiKey = "cf1ed49fb87485b3139aaf9f209df896"
    const units = "metric"
    const url = "https://api.openweathermap.org/data/2.5/weather?q="+ query + "&appid=" + apiKey+ "&units=" + units
    https.get(url, function(response){
        console.log(response.statusCode)
        response.on('data', function(data) {
            const weatherData = JSON.parse(data)
            const temp = weatherData.main.temp
            const icon = weatherData.weather[0].icon
            const imageURL = "https://openweathermap.org/img/wn/" + icon +".png"
            // res.set("Content-Type", "text/html");
            res.write("<h1>The temperature in "+ query + " is " + temp + " degrees Celcius.</h1>")
            res.write("<img src='" + imageURL + "'>");
            res.send()
            
        });
    })

})



app.listen(3000,function(){
    console.log("Sever is runnning on port 3000.")
})