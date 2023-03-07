const { tables, getKnex } = require('../data');
const { getLogger } = require('../core/logging');



const findById = (id) => {
  return getKnex()(tables.les)
    .join(tables.gaat_naar, 'gaat_naar.les_id', '=', 'les.les_id')
    .where('gaat_naar.student_id', id);
};



module.exports = {

  findById,
};