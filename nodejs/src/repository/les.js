const { tables, getKnex } = require('../data');
const { getLogger } = require('../core/logging');

const findAll = () => {
  return getKnex()(tables.les)
    .select()
    .orderBy('les_id', 'ASC');
};

const findById = (id) => {
  return getKnex()(tables.les)
    .where('les_id', id)
    .first();
};



module.exports = {
  findAll,
  findById,
};
