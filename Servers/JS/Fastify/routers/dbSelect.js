const { QUERY_1, QUERY_1K, QUERY_10K, QUERY_100K } = require("../../db/query");
const { dbSelect } = require("../../utils/paths");
const selectRouter = async (fastify) => {
  fastify.get(dbSelect.oneRecord, async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_1);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSelect.oneKRecord, async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_1K);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSelect.tenKRecords, async () => {
    const client = await fastify.pg.connect();
    try {
      const { rows } = await client.query(QUERY_10K);
      return { len: rows.length };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSelect.hundredKRecord, async () => {
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
