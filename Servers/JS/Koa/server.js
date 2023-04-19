const { parseCmdPort, parseCmdWorkers } = require("../utils/parseCmd");
const Koa = require("koa");
const app = new Koa();
const cluster = require("cluster");

const { pool } = require("./db");

const port = parseCmdPort(process.argv);
const clusterWorkerSize = parseCmdWorkers(process.argv);
app.pool = pool;
app
  .use(require("./routers/dbSelect").routes())
  .use(require("./routers/dbSelect").allowedMethods())
  .use(require("./routers/dbSleep").routes())
  .use(require("./routers/dbSleep").allowedMethods())
  .use(require("./routers/jsonResponse").routes())
  .use(require("./routers/jsonResponse").allowedMethods())
  .use(require("./routers/extra").routes())
  .use(require("./routers/extra").allowedMethods());

const startServer = async () => {
  app.listen(port, () => {
    console.log(`Example app listening on port ${port} and pid ${process.pid}`);
  });
};
module.exports = {
  startServer,
  clusterWorkerSize,
  cluster,
};
