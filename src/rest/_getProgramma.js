const Joi = require('joi');
const Router = require('@koa/router');

const getProgrammaService = require('../service/getProgramma');
const validate = require('./_validation');



const getProgById = async (ctx) => {
  const user = await getProgrammaService.getById(ctx.params.id);
  ctx.body = user;
};
getProgById.validationScheme = {
  params: {
    id: Joi.number().integer().positive(),
  },
};

module.exports = function installGetProgRoutes(app) {
  const router = new Router({
    prefix: '/getprog',
  });

  router.get('/:id', validate(getProgById.validationScheme), getProgById);
  app
  .use(router.routes())
  .use(router.allowedMethods());
};