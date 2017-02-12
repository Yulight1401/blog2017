<template>
  <div id="">
  <div class="row">
<form class="col s12">
  <div class="row">
    <div class="input-field col s12">
      <input id="username" type="text" class="validate" v-bind:class="{invalid:usok}" v-model="username">
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
      <label for="password">密码</label>
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
<div id="userknow" class="modal modal-fixed-footer">
    <div class="modal-content">
      <h4>用户须知</h4>
      <p>谢谢您注册Yul的博客，您一定是Yul的朋友吧！</p>
      <p>自您同意本协议起，您就获得了评论功能，开心吧？！</p>
      <p>请您与作者一起构建一个优雅的博客环境，不要在评论区搞事情！</p>
      <p>求大佬别来搞我的后台哦，我对部分接口有一定的防护措施～</p>
      <p>告诉您一个小秘密：本系统开源在github,项目名blog2017。
      同时你可以和我联系，让你成为合作作者，然后我们就可以一起愉快的撸文呢</p>
    </div>
    <div class="modal-footer">
      <a  class=" modal-action modal-close waves-effect waves-green btn-flat">反对</a>
      <a  class=" modal-action waves-effect waves-green btn" v-on:click="regist">接受</a>
    </div>
  </div>
</div>

  </div>
</template>

<script>
/* eslint-disable */
import {User} from '../common/http.js'
import Cookie from '../common/cookie.js'
import SQLDT from '../common/sqldatetime.js'

export default {
  name: 'regist',
  data: function () {
    return {
      psok: false,
      usok: false,
      githubok: false,
      wechatok: false,
      loading: false,
      userror: '不能为空',
      username: "",
      password: "",
      spassword: "",
      github: "",
      wechat: "",
      info: ""
    }
  },
  mounted:function ()  {
    $('.modal').modal()
    document.title = "Regist.Yul's Blog"
    this.$store.commit('loadingState',false)
  },
  methods: {
    validform: function () {
      let vm=this
      this.username.length == 0 ? this.usok=true :
      function(){vm.github.length == 0 ? vm.githubok=true :
      function(){vm.wechat.length == 0 ? vm.wechatok=true :
      function(){!vm.psok&&vm.password.length!=0?function(){ $('#userknow').modal('open')}():alert('请确认密码！')}()}()
      }()
    },
    validpassword: function () {
      this.spassword == this.password ? this.psok = false:this.psok = true
    },
    regist: function () {
      this.loading = true
      let vm=this
      let data = {username:this.username, password:this.password,create: SQLDT(), github:this.github, wechat:this.wechat, info:this.info}
      User.create(data,function(data){
        data.status=='error' ?
        function(){
          Materialize.toast('注册失败:'+data.info, 4000)
          $('#userknow').modal('close')
          vm.loading = false
          vm.userror = "用户名重复"
          vm.usok = true
        }():
        function(){
          Materialize.toast('注册成功', 4000);
          $('#userknow').modal('close')
          vm.loading = false
          let user={username:vm.username,password:vm.spassword}
          Cookie.set('user',JSON.stringify(user),2)
          vm.$store.commit('loginState',false)
        }()
      },function(err){
        $('#userknow').modal('close')
        vm.loading = false
        Materialize.toast('错误：'+err.statusText, 4000)
      })
    },
  },
};
</script>

<style>
</style>
