const {
  QUERY_SLEEP_0_25,
  QUERY_SLEEP_0_5,
  QUERY_SLEEP_0_75,
  QUERY_SLEEP_1,
  QUERY_SLEEP_2,
} = require("../../db/query");
const sleepRouter = async (fastify) => {
  fastify.get("/0_25_s_sleep", async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_25);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get("/0_5_s_sleep", async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_5);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get("/0_75_s_sleep", async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_75);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get("/1_s_sleep", async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_1);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get("/2_s_sleep", async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_2);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
};
module.exports = sleepRouter;
