// const data = require("../../test_data/1K.json");
const fs = require('fs').promises
const os = require("os");
const cluster = require("cluster");
const fastify = require('fastify')({
    logger: false,
    disableRequestLogging: true
});
fastify.register(require('@fastify/postgres'), {
    connectionString: 'postgres://postgres:1234@localhost:5431/SpeedTest'
})


const clusterWorkerSize = 13
fastify.get('/1_k_json', async (request, reply) => {
    const client = await fastify.pg.connect()
    try {
        await client.query(
            'SELECT pg_sleep(1)'
        )
        return {'Hello': 'world'}
    } catch (error) {
        console.error(error)
        reply.code(500).send('Внутренняя ошибка сервера')
    } finally {
        // Release the client immediately after query resolves, or upon error
        client.release()
    }
})

const start = async () => {
    try {
        await fastify.listen({port: 3000});
        console.log(`server listening on ${fastify.server.address().port} and worker ${process.pid}`);
    } catch (err) {
        fastify.log.error(err);
        process.exit(1);
    }
}

if (clusterWorkerSize > 1) {
    if (cluster.isMaster) {
        for (let i = 0; i < clusterWorkerSize; i++) {
            cluster.fork();
        }

        cluster.on("exit", function (worker) {
            console.log("Worker", worker.id, " has exited.")
        })
    } else {
        start();
    }
} else {
    start();
}