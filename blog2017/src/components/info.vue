<template>
  <div id="">
  <div class="row">
<form class="col s12">
  <div class="row">
    <div class="input-field col s12">
      <input disabled id="username" type="text" class="validate"  v-model="username">
      <label for="username"  v-bind:data-error="userror">用户名</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="github" type="text" class="validate" v-bind:class="{invalid:githubok}" v-model="github">
      <label for="github" data-error="不能为空">Github</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="wechat" type="text" class="validate" v-model="wechat" v-bind:class="{invalid:wechatok}">
      <label for="wechat" data-error="不能为空">微信</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="info" type="text" class="validate" v-model="info">
      <label for="info">签名*</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="password" type="password" class="validate" v-model="password" >
      <label for="password">修改密码</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="password" type="password" class="validate" v-bind:class="{invalid:psok}" v-model="spassword" v-on:input="validpassword">
      <label for="password" data-error="密码不一致">重复密码</label>
    </div>
  </div>
  <div class="row" style="text-align:center">
<a class="waves-effect waves-light btn"  v-on:click="validform">完成</a>
  </div>
</form>
<div class="progress" v-if="loading">
      <div class="indeterminate"></div>
  </div>

  </div>
</template>

<script>
/* eslint-disable */
import {User} from '../common/http.js'
import Cookie from '../common/cookie.js'

export default {
  name: 'info',
  data: function () {
    return {
      psok: true,
      githubok: false,
      wechatok: false,
      loading: false,
      userror: '不能为空',
      username: "",
      password: "",
      spassword: "",
      github: "",
      wechat: "",
      info: "",
      userid: ""
    }
  },
  mounted: function () {
    this.getInfo()
  },
  methods: {
    validform: function () {
      let vm=this
      vm.github.length == 0 ? vm.githubok=true :
      function(){vm.wechat.length == 0 ? vm.wechatok=true :
      function(){!vm.psok&&vm.password.length!=0?function(){ vm.regist()}():
      alert('请确认密码！')}()}()
    },
    validpassword: function () {
      this.spassword == this.password ? this.psok = false:this.psok = true
    },
    getInfo: function () {
      let vm = this
      User.getInfo(vm.$route.params, function(data,status){
        data.status == 'error' ? Materialize.toast('获取用户信息错误：'+data.info, 4000) : data = data.data
        vm.username = data.username
        vm.github = data.github
        vm.wechat = data.wechat
        vm.info = data.info
        vm.userid = data.id
      }, function(err){
        Materialize.toast('获取用户信息错误：'+err.statusText, 4000)
      })
    },
    regist: function () {
      this.loading = true
      let vm=this
      let formData = {password:this.password, github:this.github, wechat:this.wechat, info:this.info}
      let userData,token
      Cookie.get('user') == '' ? function() {Materialize.toast('需要再次登录', 4000);vm.$router.push('/login')}() :userData = JSON.parse(Cookie.get('user'))
      User.login(userData,function(data,status){
        token = data['access_token']
        User.revise(formData,token,function(data){
          data.status=='error' ?
          function(){
            Materialize.toast('修改失败:'+data.info, 4000)
            vm.loading = false
          }():
          function(){
            Materialize.toast('修改成功', 4000);
            vm.loading = false
            let user={username:vm.username,password:vm.spassword}
            Cookie.set('user',JSON.stringify(user),2)
          }()
        },function(err){
          vm.loading = false
          Materialize.toast('错误：'+err.statusText, 4000)
        })
      },function(){})
    },
  },
};
</script>

<style>
</style>
