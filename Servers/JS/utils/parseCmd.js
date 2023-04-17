const parseCmdFactory = (replaceValue, defaultValue) => (argsList) => {
  for (const line of argsList) {
    let num = parseInt(line.replace(replaceValue, ""));
    if (num) {
      return num;
    }
  }
  return defaultValue;
};
const parseCmdWorkers = parseCmdFactory("workers=", 1);
const parseCmdPort = parseCmdFactory("port=", 3000);

module.exports = {
  parseCmdWorkers,
  parseCmdPort,
};
