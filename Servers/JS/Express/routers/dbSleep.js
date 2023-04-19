const router = require("express").Router();

const { pool } = require("../db");
const {
  QUERY_SLEEP_0_25,
  QUERY_SLEEP_0_5,
  QUERY_SLEEP_0_75,
  QUERY_SLEEP_1,
  QUERY_SLEEP_2,
} = require("../../db/query");

const { dbSleep } = require("../../utils/paths");

router.get(dbSleep.zero25SecondSleep, async (_, res) => {
  await pool.query(QUERY_SLEEP_0_25);
  res.send({ Hello: "World" });
});
router.get(dbSleep.zero5SecondSleep, async (_, res) => {
  await pool.query(QUERY_SLEEP_0_5);
  res.send({ Hello: "World" });
});
router.get(dbSleep.zero75SecondSleep, async (_, res) => {
  await pool.query(QUERY_SLEEP_0_75);
  res.send({ Hello: "World" });
});
router.get(dbSleep.oneSecondSleep, async (_, res) => {
  await pool.query(QUERY_SLEEP_1);
  res.send({ Hello: "World" });
});
router.get(dbSleep.twoSecondSleep, async (_, res) => {
  await pool.query(QUERY_SLEEP_2);
  res.send({ Hello: "World" });
});

module.exports = router;
