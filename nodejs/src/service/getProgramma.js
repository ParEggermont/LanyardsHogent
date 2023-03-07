const { getLogger } = require('../core/logging');
const ServiceError = require('../core/serviceError');
const getProgrammaRepo = require('../repository/getProgramma');

const debugLog = (message, meta = {}) => {
  if (!this.logger) this.logger = getLogger();
  this.logger.debug(message, meta);
};



const getById = async (id) => {
  debugLog(`Fetching prog with id ${id}`);
  const gaatNaar = await getProgrammaRepo.findById(id);

  if (!gaatNaar) {
    throw ServiceError.notFound(`No user with id ${id} exists`, { id });
  }

  return gaatNaar;
};

module.exports = {
  getById,
};
