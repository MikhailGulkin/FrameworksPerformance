const router = require("express").Router();

const { pool } = require("../db");
const { QUERY_1, QUERY_10K, QUERY_100K, QUERY_1K } = require("../../db/query");
const { dbSelect } = require("../../utils/paths");

router.get(dbSelect.oneRecord, async (_, res) => {
  const { rows } = await pool.query(QUERY_1);
  res.send({ len: rows.length });
});
router.get(dbSelect.oneKRecord, async (_, res) => {
  const { rows } = await pool.query(QUERY_1K);
  res.send({ len: rows.length });
});
router.get(dbSelect.tenKRecords, async (_, res) => {
  const { rows } = await pool.query(QUERY_10K);
  res.send({ len: rows.length });
});
router.get(dbSelect.hundredKRecord, async (_, res) => {
  const { rows } = await pool.query(QUERY_100K);
  res.send({ len: rows.length });
});

module.exports = router;
