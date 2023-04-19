const oneKJsonData = require("../../../test_data/1K.json");
const tenKJsonData = require("../../../test_data/10K.json");
const hundredJsonData = require("../../../test_data/100K.json");
const oneKKJsonData = require("../../../test_data/1M.json");
const { jsonResponse } = require("../../utils/paths");

const fiveKKJsonData = require("../../../test_data/5M.json");

const Router = require("koa-router");
const router = new Router();

router.get(jsonResponse.oneKJson, async (ctx) => {
  ctx.body = oneKJsonData;
});
router.get(jsonResponse.tenKJson, async (ctx) => {
  ctx.body = tenKJsonData;
});
router.get(jsonResponse.hundredKJson, async (ctx) => {
  ctx.body = hundredJsonData;
});
router.get(jsonResponse.oneKKJson, async (ctx) => {
  ctx.body = oneKKJsonData;
});
router.get(jsonResponse.fiveKKJson, async (ctx) => {
  ctx.body = fiveKKJsonData;
});

module.exports = router;
