const { getLogger } = require('../core/logging');
const ServiceError = require('../core/serviceError');
const lesRepo = require('../repository/gaatnaar');

const debugLog = (message, meta = {}) => {
  if (!this.logger) this.logger = getLogger();
  this.logger.debug(message, meta);
};

const getAll = async () => {
  debugLog('Fetching all users');
  const data = await lesRepo.findAll();
  return {
    data,
  };
};

const getById = async (id) => {
  debugLog(`Fetching user with id ${id}`);
  const les = await lesRepo.findById(id);

  if (!gaatNaar) {
    throw ServiceError.notFound(`No user with id ${id} exists`, { id });
  }

  return gaatNaar;
};

module.exports = {
  getAll,
  getById,
};
