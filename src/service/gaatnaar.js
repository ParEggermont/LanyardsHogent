const { getLogger } = require('../core/logging');
const ServiceError = require('../core/serviceError');
const gaarNaarRepo = require('../repository/gaatnaar');

const debugLog = (message, meta = {}) => {
  if (!this.logger) this.logger = getLogger();
  this.logger.debug(message, meta);
};

const getAll = async () => {
  debugLog('Fetching all gaatNaar');
  const data = await gaarNaarRepo.findAll();
  return {
    data,
  };
};

const getById = async (id) => {
  debugLog(`Fetching user with id ${id}`);
  const gaatNaar = await gaarNaarRepo.findById(id);

  if (!gaatNaar) {
    throw ServiceError.notFound(`No user with id ${id} exists`, { id });
  }

  return gaatNaar;
};

module.exports = {
  getAll,
  getById,
};
