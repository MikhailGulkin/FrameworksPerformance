const Router = require("koa-router");
const { extraTests } = require("../../utils/paths");

const router = new Router();

router.get(extraTests.helloWorld, async (ctx) => {
  ctx.body = { Hello: "World" };
});
module.exports = router;
