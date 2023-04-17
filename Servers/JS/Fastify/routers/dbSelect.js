const { QUERY_1, QUERY_1K, QUERY_10K, QUERY_100K } = require("../../db/query");

const selectRouter = async (fastify) => {
  fastify.get("/1_record", async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_1);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get("/1_k_records", async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_1K);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get("/10_k_records", async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_10K);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get("/100_k_records", async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_100K);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
};
module.exports = selectRouter;
