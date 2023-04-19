const { QUERY_1, QUERY_1K, QUERY_10K, QUERY_100K } = require("../../db/query");

const Router = require("koa-router");
const { dbSelect } = require("../../utils/paths");
const router = new Router();

router.get(dbSelect.oneRecord, async (ctx) => {
  const { rows } = await ctx.app.pool.query(QUERY_1);
  ctx.body = { len: rows.length };
});
router.get(dbSelect.oneKRecord, async (ctx) => {
  const { rows } = await ctx.app.pool.query(QUERY_1K);
  ctx.body = { len: rows.length };
});
router.get(dbSelect.tenKRecords, async (ctx) => {
  const { rows } = await ctx.app.pool.query(QUERY_10K);
  ctx.body = { len: rows.length };
});
router.get(dbSelect.hundredKRecord, async (ctx) => {
  const { rows } = await ctx.app.pool.query(QUERY_100K);
  ctx.body = { len: rows.length };
});
module.exports = router;
