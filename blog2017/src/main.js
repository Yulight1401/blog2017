// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
/* eslint-disable*/

import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import App from './App';
import article from './components/Article'
import album from './components/Album'
import articleone from './components/Articleone'
import music from './components/Music'
import mv from './components/Mv'
import regist from './components/regist'
import login from './components/login'

require('../static/materialize/css/materialize.css');
require('../static/materialize/js/materialize.js');

Vue.use(VueRouter);
Vue.use(VueResource);


let routes = [
  {path: '/', name: 'index', component: App, children: [{path: '/article', component: article}, {path: '/album', component: album},{path:'/articleone',component:articleone},{path:'/music',component:music},{path:'/mv',component:mv},{path:'/regist',component:regist},{path:'/login',component:login}]}
];
let router = new VueRouter({
  'linkActiveClass': 'active',
   routes // （缩写）相当于 routes: routes
});
const app = new Vue({
  router
}).$mount('#app');
