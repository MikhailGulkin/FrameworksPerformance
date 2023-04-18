const oneKJsonData = require("../../../test_data/1K.json");
const tenKJsonData = require("../../../test_data/10K.json");
const hundredJsonData = require("../../../test_data/100K.json");
const oneKKJsonData = require("../../../test_data/1M.json");
const fiveKKJsonData = require("../../../test_data/5M.json");
const { jsonResponse } = require("../../utils/paths");

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
  fastify.get(jsonResponse.oneKJson, oneKJson);
  fastify.get(jsonResponse.tenKJson, tenKJson);
  fastify.get(jsonResponse.hundredKJson, hundredKJson);
  fastify.get(jsonResponse.oneKKJson, oneKKJson);
  fastify.get(jsonResponse.fiveKKJson, fiveKKJson);
};
module.exports = jsonRouter;
