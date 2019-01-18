const express = require('express');
const mysql = require('mysql');

// create connection
const db = mysql.createConnection({
    host        : 'weatherdbinstance.c3abupa67dux.us-east-2.rds.amazonaws.com',
    user        : 'wsu',
    password    : 'wsucapstone2018',
    database    : 'pi'
});

// Connect
db.connect((err) => {
    if(err) {
        throw err;
    }
    console.log("MySQL Connected...");
});

const router = express();


router.get('/api/weatherData', (req, res) => {
    let sql = 'SELECT * FROM weather_data';
    let query = db.query(sql, (err, results, fields) => {
        if(err) throw err;
        console.log(results);
        res.json(results);
    })
});


// 3000 is default to create react app, 
// we are using that tool to generate the react application
const port = 5000;

router.listen(port, () => console.log(`Server started on port ${port}`));
