<template>
  <div id="manage">
  <div class="progress" v-show='loading'>
      <div class="indeterminate"></div>
  </div>
  <div class="fixed-action-btn toolbar">
      <a class="btn-floating btn-large gray">
        <i class="large material-icons">mode_edit</i>
      </a>
      <ul>
        <li class="waves-effect waves-light"><a href="#!"><i class="material-icons">insert_chart</i></a></li>
        <li class="waves-effect waves-light"><a href="#!"><i class="material-icons">format_quote</i></a></li>
        <li class="waves-effect waves-light"><a href="#!"><i class="material-icons">publish</i></a></li>
        <li class="waves-effect waves-light"><a href="#!"><i class="material-icons">attach_file</i></a></li>
      </ul>
    </div>

  <div class="row">
<div class="col s12">
  <ul class="tabs">
    <li class="tab col s4"><a class="active" href="#user">用户</a></li>
    <li class="tab col s4"><a href="#article">文章</a></li>
    <li class="tab col s4"><a href="#comment">评论</a></li>
  </ul>
</div>
<div id="user" class="col s12">
<ul class="collection with-header">
  <li class="collection-item"><div>Alvin<a href="#!" class="secondary-content">查看&nbsp&nbsp</a></div></li>
</ul>
</div>
<div id="article" class="col s12">
<ul class="collection with-header">
  <li class="collection-item"><div>Alvin<a href="#!" class="secondary-content">查看&nbsp&nbsp</a></div></li>
</ul>
</div>
<div id="comment" class="col s12">
<ul class="collection with-header">
  <li class="collection-item"><div>Alvin<a href="#!" class="secondary-content">查看&nbsp&nbsp</a></div></li>
</ul>
</div>
</div>
  </div>
</template>

<script>
/* eslint-disable */
import Cookie from './common/cookie.js'
import {User,Comment,Article} from './common/http.js'

export default {
  name: 'manage',
  data: function () {
    return {
      loading: false,
    }
  },
  mounted: () =>{
    $('ul.tabs').tabs({
      onShow: function () {
      },
      swipeable: true,
    });
  },
  components: {
  },
  methods:{

  },
};
</script>

<style>

</style>
