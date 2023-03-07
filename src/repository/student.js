const { tables, getKnex } = require('../data');
const { getLogger } = require('../core/logging');

const findAll = () => {
  return getKnex()(tables.student)
    .select()
    .orderBy('student_id', 'ASC');
};

const findById = (id) => {
  return getKnex()(tables.student)
    .where('student_id', id)
    .first();
};



module.exports = {
  findAll,
  findById,
};
