const oneKJsonData = require("../../../test_data/1K.json");
const tenKJsonData = require("../../../test_data/10K.json");
const hundredJsonData = require("../../../test_data/100K.json");
const oneKKJsonData = require("../../../test_data/1M.json");
const fiveKKJsonData = require("../../../test_data/5M.json");

const router = require("express").Router();

const { jsonResponse } = require("../../utils/paths");

router.get(jsonResponse.oneKJson, async (_, res) => {
  res.send(oneKJsonData);
});
router.get(jsonResponse.tenKJson, async (_, res) => {
  res.send(tenKJsonData);
});
router.get(jsonResponse.hundredKJson, async (_, res) => {
  res.send(hundredJsonData);
});
router.get(jsonResponse.oneKKJson, async (_, res) => {
  res.send(oneKKJsonData);
});
router.get(jsonResponse.fiveKKJson, async (_, res) => {
  res.send(fiveKKJsonData);
});

module.exports = router;
