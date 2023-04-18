const { parseCmdWorkers, parseCmdPort } = require("../utils/parseCmd");
const { connection_pg } = require("../db/connection");
const cluster = require("cluster");
const fastify = require("fastify")({
  logger: false,
  disableRequestLogging: true,
});

fastify.register(require("./routers/jsoneResponse"));
fastify.register(require("./routers/dbSleep"));
fastify.register(require("./routers/dbSelect"));
fastify.register(require("./routers/extra"));

fastify.register(require("@fastify/postgres"), {
  connectionString: connection_pg,
});

const port = parseCmdPort(process.argv);
const clusterWorkerSize = parseCmdWorkers(process.argv);
const startServer = async () => {
  try {
    await fastify.listen({ port: port });
    console.log(
      `server listening on ${fastify.server.address().port} and worker ${
        process.pid
      }`
    );
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

module.exports = {
  startServer,
  clusterWorkerSize,
  cluster,
};
