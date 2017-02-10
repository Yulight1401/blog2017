<template>
  <div id="manage">
  <div class="row">
<div class="col s12">
  <ul class="tabs">
    <li class="tab col s4"><a class="active" href="#test1">用户</a></li>
    <li class="tab col s4"><a href="#test2">文章</a></li>
    <li class="tab col s4"><a href="#test4">评论</a></li>
  </ul>
</div>
<div id="test1" class="col s12">Test 1</div>
<div id="test2" class="col s12">Test 2</div>
<div id="test4" class="col s12">Test 4</div>
</div>
  </div>
</template>

<script>
/* eslint-disable */
window.$ = window.jQuery = require('jquery');

export default {
  name: 'manage',
  mounted: () =>{
    $('ul.tabs').tabs();
  },
  components: {
  },
};
</script>

<style>
body::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

body::-webkit-scrollbar
{
	width: 2px;
	background-color: #F5F5F5;
}

body::-webkit-scrollbar-thumb
{
	border-radius: 1px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #555;
}
.slide-fade-enter-active {
  transition: all 0.8s ease;
}
.slide-fade-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for <2.1.8 */ {
  transform: translateY(30px);
  opacity: 0;
}
</style>
