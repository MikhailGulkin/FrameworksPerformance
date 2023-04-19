const Router = require("koa-router");
const router = new Router();
const {
  QUERY_SLEEP_0_25,
  QUERY_SLEEP_0_5,
  QUERY_SLEEP_0_75,
  QUERY_SLEEP_1,
  QUERY_SLEEP_2,
} = require("../../db/query");

const { dbSleep } = require("../../utils/paths");

router.get(dbSleep.zero25SecondSleep, async (ctx) => {
  await ctx.app.pool.query(QUERY_SLEEP_0_25);
  ctx.body = { Hello: "World" };
});
router.get(dbSleep.zero5SecondSleep, async (ctx) => {
  await ctx.app.pool.query(QUERY_SLEEP_0_5);
  ctx.body = { Hello: "World" };
});
router.get(dbSleep.zero75SecondSleep, async (ctx) => {
  await ctx.app.pool.query(QUERY_SLEEP_0_75);
  ctx.body = { Hello: "World" };
});
router.get(dbSleep.oneSecondSleep, async (ctx) => {
  await ctx.app.pool.query(QUERY_SLEEP_1);
  ctx.body = { Hello: "World" };
});
router.get(dbSleep.twoSecondSleep, async (ctx) => {
  await ctx.app.pool.query(QUERY_SLEEP_2);
  ctx.body = { Hello: "World" };
});
module.exports = router;
