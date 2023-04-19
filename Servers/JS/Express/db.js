const { connection_pg } = require("../db/connection");
const { Pool } = require("pg");
const pool = new Pool({
  connectionString: connection_pg,
});
module.exports = {
  pool,
};
