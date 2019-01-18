'use strict';
var knex = {
  client: 'mysql',
  connection: {
    host : 'weatherdbprototype1.c3abupa67dux.us-east-2.rds.amazonaws.com',
    port:'3306',
    user : 'pro1wsu',
    password : 'wsucapstone2018',
    database : 'weatherstation',
    connectionLimit : 50, // Limits the number of open connections to mysql (ie the rpis)
  }
};

module.exports = knex;