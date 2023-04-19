const router = require("express").Router();

const { extraTests } = require("../../utils/paths");

router.get(extraTests.helloWorld, async (_, res) => {
  res.send({ Hello: "World" });
});

module.exports = router;
