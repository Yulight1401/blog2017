<template>
  <div id="">
  <form class="col s12">
    <div class="row">
      <div class="input-field col s12">
        <input id="username" type="text" class="validate">
        <label data-error="用户名错误"  for="username">用户名</label>
      </div>
    </div>
    <div class="row">
      <div class="input-field col s12">
        <input id="password" type="password" class="validate">
        <label for="password" data-error="密码错误">密码</label>
      </div>
    </div>
    <div class="row" style="text-align:center">
  <a class="waves-effect waves-light btn" >登录</a>
    </div>
  </form>
  <div class="progress">
      <div class="indeterminate"></div>
  </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'login',
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
