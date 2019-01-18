var express     = require('express');
var morgan      = require('morgan');

var app = express();
var server = require('http').Server(app);
port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.send("testing site");
});

app.use(morgan('dev')); 

server.listen(port);
console.log('running at port' + port);