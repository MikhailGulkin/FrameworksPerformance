const { extraTests } = require("../../utils/paths");

const helloWorld = async () => {
  return { Hello: "World" };
};
const jsonRouter = async (fastify) => {
  fastify.get(extraTests.helloWorld, helloWorld);
};
module.exports = jsonRouter;
