const Joi = require('joi');
const Router = require('@koa/router');

const gaatNaarService = require('../service/gaatnaar');
const validate = require('./_validation');

const getAllGaatNaar = async (ctx) => {
  const users = await gaatNaarService.getAll();
  ctx.body = users;
};
getAllGaatNaar.validationScheme = null;

const getUserById = async (ctx) => {
  const user = await userService.getById(ctx.params.id);
  ctx.body = user;
};
getUserById.validationScheme = {
  params: {
    id: Joi.number().integer().positive(),
  },
};

module.exports = function installGaatNaarRoutes(app) {
  const router = new Router({
    prefix: '/gaatnaar',
  });

  router.get('/', validate(getAllGaatNaar.validationScheme), getAllGaatNaar);
  app
  .use(router.routes())
  .use(router.allowedMethods());
};