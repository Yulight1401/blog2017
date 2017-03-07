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
        <li class="waves-effect waves-light"><a href=".#/edit/create/0"><i class="material-icons">insert_chart</i></a></li>
        <li class="waves-effect waves-light"><a href=".#/edit/create/0"><i class="material-icons">format_quote</i></a></li>
        <li class="waves-effect waves-light"><a href=".#/edit/create/0"><i class="material-icons">publish</i></a></li>
        <li class="waves-effect waves-light"><a href=".#/edit/create/0"><i class="material-icons">attach_file</i></a></li>
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
<ul class="collection with-header"  >
  <li class="collection-item" v-for="(user,index) in allUsers"  ><div>{{user.name}}<a  class="secondary-content" style="color:green" v-bind:data-index='index' v-on:click="getUser">查看&nbsp&nbsp</a><a class="secondary-content" style="color:red" v-on:click = "openModal" v-bind:data-index='user.id' name="user">删除&nbsp&nbsp</a></div></li>
</ul>
</div>
<div id="article" class="col s12">
<ul class="collection with-header">
  <li class="collection-item" v-for="article in allArticles" ><div>{{article.title}}<a v-bind:href="'.#/articleone/'+article.id" class="secondary-content" style="color:green" >查看&nbsp&nbsp</a><a v-bind:href="'.#/edit/revise/'+article.id" class="secondary-content" style="color:green" >修改&nbsp&nbsp</a><a  class="secondary-content" style="color:red"  v-on:click = "openModal" v-bind:data-index='article.id' name="article">删除&nbsp&nbsp</a></div></li>
</ul>
</div>
<div id="comment" class="col s12">
<ul class="collection with-header" >
  <li class="collection-item" v-for="(comment,index) in allComments" ><div>{{comment.content}}<a class="secondary-content" style="color:green" v-bind:data-index='index' v-on:click="getComment">查看&nbsp&nbsp</a><a class="secondary-content" style="color:red" v-on:click = "openModal" v-bind:data-index='comment.id' name="comment">删除&nbsp&nbsp</a></div></li>
</ul>
</div>
</div>
<div id="modal4" class="modal">
    <div class="modal-content">
      <h4>确认删除?</h4>
      <p>删除后无法撤回</p>
    </div>
    <div class="modal-footer">
      <a v-on:click="deleteObj" style="color:red;cursor:pointer;" class=" modal-action modal-close waves-effect waves-green btn-flat">确定</a>
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
      allArticles: [],
      allComments: [],
      allUsers: [],
      token: '',
      name: '',
      index: ''
    }
  },
  mounted () {
    let vm = this
    let token = '',userData
    Cookie.get('user') == '' ? function() {Materialize.toast('需要再次登录', 4000);vm.$router.push('/login')}() :userData = JSON.parse(Cookie.get('user'))
    User.login(userData,function(data,status){
      vm.token = data['access_token']
      vm.getAllarticles()
      vm.getAlluser()
      vm.getAllcomment()
    },function(err){
      Materialize.toast('错误:'+err.statusText, 4000)
    })
    $('ul.tabs').tabs({
      onShow: function () {
      },
      swipeable: true,
    });
    $('.modal').modal();
  },
  components: {
  },
  methods:{
    getAllarticles () {
      let vm = this
      Article.getAlls({},vm.token,function(data,status){
          vm.allArticles = data.data
        },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
        })
      },
    getAllcomment () {
      let vm = this
      Comment.getAll({},vm.token,function(data, status){
          vm.allComments = data.data
        },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
        })
    },
    getAlluser () {
      let vm = this
      User.getAll({},vm.token,function(data,status){
          vm.allUsers = data.data
        },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
        })
    },
    openModal(){
      $('#modal4').modal('open');
      let vm = this
      vm.index = event.target.dataset.index
      vm.name = event.target.name
    },
    deleteObj () {
      let vm = this
      switch (vm.name) {
        case 'article':
          vm.deleteArticle()
          break;
        case 'comment' :
          vm.deleteComment()
          break;
        case 'user' :
          vm.deleteUser()
          break;
        default:
      }
    },
    deleteArticle () {
      let vm = this
      let index = vm.index
      Article.delete({ id: index },vm.token,function(data, status){
        data.status == 'success' ? Materialize.toast('删除成功:'+data.code, 4000) :Materialize.toast('删除失败:'+data.info, 4000)
        vm.getAllarticles()
      },function(err){
        Materialize.toast('错误:'+err.statusText, 4000)
      })
    },
    deleteUser () {
      let vm = this
      let index = vm.index
      User.delete({ id:index },vm.token,function(data, status){
        data.status == 'success' ? Materialize.toast('删除成功:'+data.code, 4000) :Materialize.toast('删除失败:'+data.info, 4000)
        vm.getAlluser()
      },function(err){
        Materialize.toast('错误:'+err.statusText, 4000)
      })
    },
    deleteComment () {
      let vm = this
      let index = vm.index
      Comment.delete({ id:index },vm.token,function(data, status){
        data.status == 'success' ? Materialize.toast('删除成功:'+data.code, 4000) :Materialize.toast('删除失败:'+data.info, 4000)
        vm.getAllcomment()
      },function(err){
        Materialize.toast('错误:'+err.statusText, 4000)
      })
    },
    getUser(){
      let index = event.target.dataset.index
      let vm = this
      Materialize.toast(JSON.stringify(vm.allUsers[index]) , 4000)
    },
    getComment(){
      let index = event.target.dataset.index
      let vm = this
      Materialize.toast(JSON.stringify(vm.allComments[index]) , 4000)
    }
  },
};
</script>

<style>

</style>
