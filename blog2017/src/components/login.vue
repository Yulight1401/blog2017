<template>
  <div id="">
  <form class="col s12">
    <div class="row">
      <div class="input-field col s12">
        <input id="username" type="text" class="validate" v-model="username" v-bind:class="{'invalid':unok}">
        <label data-error="不能为空"  for="username">用户名</label>
      </div>
    </div>
    <div class="row">
      <div class="input-field col s12">
        <input id="password" type="password" class="validate" v-bind:class="{'invalid':psok}"  v-model="password">
        <label for="password"  v-bind:data-error='error'>密码</label>
      </div>
    </div>
    <div class="row" style="text-align:center">
  <a class="waves-effect waves-light btn" v-on:click="login">登录</a>
    </div>
  </form>
  <div class="progress" v-if="loading">
      <div class="indeterminate"></div>
  </div>
  </div>
</template>

<script>
/* eslint-disable */
import Cookie from '../common/cookie.js'
import {User} from '../common/http.js'

export default {
  name: 'login',
  data: function () {
    return {
      loading: false,
      username: '',
      password: '',
      error: '不能为空',
      psok: false,
      unok: false,
    }
  },
  mounted:function () {
    document.title = "Login.Yul's Blog"
    this.$store.commit('loadingState',false)
  },
  methods: {
    login: function (){
      this.username.length == 0 ? this.unok = true : this.unok = false ;
      this.password.length == 0 ? this.psok = true : this.psok = false ;
      !this.unok&&!this.psok ? this.post() : function(){} ;
    },
    post: function (){
      let userdata={'username':this.username,'password':this.password}
      let vm=this
      vm.loading=true
      User.login(userdata,function(data,status){
        vm.loading = false
        Cookie.set('user',JSON.stringify(userdata),2)
        vm.$store.commit('loginState',false)
        vm.$router.push('/article/1')
      },function(errMsg){
        vm.psok=true;
        vm.error='认证失败';
        vm.loading=false;
      })
    }
  },
};
</script>

<style>
</style>
