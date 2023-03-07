const Router = require('@koa/router');

const installGaatNaarRouter = require('./_gaatnaar');
const installGetProgRouter = require('./_getProgramma');

module.exports = (app) => {
  const router = new Router({
    prefix: '/api',
  });

  installGaatNaarRouter(router);
  installGetProgRouter(router);
  

  app.use(router.routes()).use(router.allowedMethods());
};