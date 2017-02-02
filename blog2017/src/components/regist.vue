<template>
  <div id="">
  <div class="row">
<form class="col s12">
  <div class="row">
    <div class="input-field col s12">
      <input id="username" type="text" class="validate">
      <label for="username" data-error="用户名已占用">用户名</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="github" type="text" class="validate">
      <label for="github">Github</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="wechat" type="text" class="validate">
      <label for="wechat">微信</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="info" type="text" class="validate">
      <label for="info">签名*</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="password" type="password" class="validate">
      <label for="password">密码</label>
    </div>
  </div>
  <div class="row">
    <div class="input-field col s12">
      <input id="password" type="password" class="validate">
      <label for="password" data-error="密码不一致">重复密码</label>
    </div>
  </div>
  <div class="row" style="text-align:center">
<a class="waves-effect waves-light btn" href="#userknow" >完成</a>
  </div>
</form>
<div class="progress">
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
      <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">反对</a>
      <a href="#!" class=" modal-action waves-effect waves-green btn">接受</a>
    </div>
  </div>
</div>

  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'regist',
  mounted: () => {
    $('.modal').modal();
  },
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style>
</style>
