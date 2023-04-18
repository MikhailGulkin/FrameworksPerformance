const {
  QUERY_SLEEP_0_25,
  QUERY_SLEEP_0_5,
  QUERY_SLEEP_0_75,
  QUERY_SLEEP_1,
  QUERY_SLEEP_2,
} = require("../../db/query");
const { dbSleep } = require("../../utils/paths");
const sleepRouter = async (fastify) => {
  fastify.get(dbSleep.zero25SecondSleep, async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_25);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSleep.zero5SecondSleep, async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_5);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSleep.zero75SecondSleep, async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_0_75);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSleep.oneSecondSleep, async () => {
    const client = await fastify.pg.connect();
    try {
      await client.query(QUERY_SLEEP_1);
      return { Hello: "World" };
    } finally {
      client.release();
    }
  });
  fastify.get(dbSleep.twoSecondSleep, async () => {
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
