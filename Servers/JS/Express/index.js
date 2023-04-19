const { startServer, cluster, clusterWorkerSize } = require("./server");

const run = () => {
  if (clusterWorkerSize > 1) {
    if (cluster.isMaster) {
      for (let i = 0; i < clusterWorkerSize; i++) {
        cluster.fork();
      }

      cluster.on("exit", function (worker) {
        console.log("Worker", worker.id, " has exited.");
      });
    } else {
      startServer();
    }
  } else {
    startServer();
  }
};

run();
