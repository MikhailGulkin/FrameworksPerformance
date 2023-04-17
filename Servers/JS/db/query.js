TABLE_NAME = "Speed";

const QUERY_SLEEP_0_25 = "SELECT pg_sleep(0.25)";
const QUERY_SLEEP_0_5 = "SELECT pg_sleep(0.5)";
const QUERY_SLEEP_0_75 = "SELECT pg_sleep(0.75)";
const QUERY_SLEEP_1 = "SELECT pg_sleep(1)";
const QUERY_SLEEP_2 = "SELECT pg_sleep(2)";

const QUERY_1 = `
    SELECT *
    FROM ${TABLE_NAME}
    LIMIT 1
`;
const QUERY_1K = `
    SELECT *
    FROM ${TABLE_NAME}
    LIMIT 1000
`;
const QUERY_10K = `
    SELECT *
    FROM ${TABLE_NAME}
    LIMIT 10000
`;

const QUERY_100K = `
    SELECT *
    FROM ${TABLE_NAME}
    LIMIT 100000
`;
const QUERY_1KK = `
    SELECT *
    FROM ${TABLE_NAME}
    LIMIT 1000000
`;
module.exports = {
  QUERY_1,
  QUERY_1K,
  QUERY_10K,
  QUERY_100K,

  QUERY_SLEEP_0_25,
  QUERY_SLEEP_0_5,
  QUERY_SLEEP_0_75,
  QUERY_SLEEP_1,
  QUERY_SLEEP_2,
};
