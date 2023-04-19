const { parseCmdPort, parseCmdWorkers } = require("../utils/parseCmd");

const express = require("express");
const cluster = require("cluster");

const dbSelect = require("./routers/dbSelect");
const dbSleep = require("./routers/dbSleep");
const jsonResponse = require("./routers/jsonResponse");
const extra = require("./routers/extra");
const app = express();

app.use("/", dbSelect);
app.use("/", dbSleep);
app.use("/", jsonResponse);
app.use("/", extra);

const clusterWorkerSize = parseCmdWorkers(process.argv);

const port = parseCmdPort(process.argv);
const startServer = async () => {
  app.listen(port, () => {
    console.log(`Example app listening on port ${port} and pid ${process.pid}`);
  });
};
module.exports = {
  startServer,
  cluster,
  clusterWorkerSize,
};
