// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
/* eslint-disable*/

import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import App from './App';
import article from './components/Article'
import album from './components/Album'
import articleone from './components/Articleone'
import music from './components/Music'
import mv from './components/Mv'
import regist from './components/regist'
import login from './components/login'
import info from './components/info'

require('../static/materialize/css/materialize.css');
require('../static/materialize/js/materialize.js');

Vue.use(VueRouter);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    login: false,
    commentData: {
    }
  },
  mutations: {
    loginState (state, stateText) {
      state.login = stateText
    },
    commentState (state, obj) {
      state.commentData.type = obj.type
      state.commentData.id = obj.id
    }
  }
})

let routes = [
   {path: '/', name: 'index', component: App,
    children: [
      {path: '/article/:class', component: article},
      {path: '/album/:class', component: album},
      {path: '/articleone/:id',component:articleone},
      {path: '/music',component:music},
      {path: '/mv',component:mv},
      {path: '/regist', component:regist},
      {path: '/login', component:login},
      {path: '/info/:name', component:info}]
    },
    {path: '/manage', name: 'manage', component: (resolve) => {require(['./Manage.vue'],resolve)}},
    {path: '/edit/:type/:id' ,name: 'edit', component: (resolve) => {require(['./Edit.vue'],resolve)}},
    {path: '*', component: (resolve) => {require(['./Notfound.vue'],resolve)} }
];
let router = new VueRouter({
  'linkActiveClass': 'active',
   routes // （缩写）相当于 routes: routes
});
const app = new Vue({
  router,
  store
}).$mount('#app');
