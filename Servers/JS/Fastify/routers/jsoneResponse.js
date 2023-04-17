const oneKJsonData = require("../../../test_data/1K.json");
const tenKJsonData = require("../../../test_data/10K.json");
const hundredJsonData = require("../../../test_data/100K.json");
const oneKKJsonData = require("../../../test_data/1M.json");
const fiveKKJsonData = require("../../../test_data/5M.json");

const oneKJson = async () => {
  return oneKJsonData;
};
const tenKJson = async () => {
  return tenKJsonData;
};
const hundredKJson = async () => {
  return hundredJsonData;
};
const oneKKJson = async () => {
  return oneKKJsonData;
};
const fiveKKJson = async () => {
  return fiveKKJsonData;
};

const jsonRouter = async (fastify) => {
  fastify.get("/1_k_json", oneKJson);
  fastify.get("/10_k_json", tenKJson);
  fastify.get("/100_k_json", hundredKJson);
  fastify.get("/1_kk_json", oneKKJson);
  fastify.get("/5_kk_json", fiveKKJson);
};
module.exports = jsonRouter;
