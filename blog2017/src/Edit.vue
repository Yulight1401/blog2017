<template>
  <div id="edit" class='row'>
  <form class="col s12 m6 l6">
  <ul class="collapsible" data-collapsible="accordion">
    <li>
      <div class="collapsible-header">配置</div>
      <div class="collapsible-body" style="padding:2%;"><div class="row">
      <div class="file-field input-field">
      <div class="btn">
        <span>图片</span>
        <input type="file" accept="image/*" v-on:change="postImg(1)">
      </div>
      <div class="file-path-wrapper">
        <input class="file-path validate" v-model='imgsrc' type="text">
      </div>
    </div>
      </div>
        <div class="row">
          <div class="input-field col s12">
            <input id="username" type="text" v-model='title' class="validate">
            <label for="username" >标题</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input id="author" type="text" v-model='author' class="validate">
            <label for="author">作者</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input id="subtitle" type="text" v-model='subtitle' class="validate">
            <label for="subtitle">副标题</label>
          </div>
        </div>
        <div class="row">
            <select class="input-field col s12" v-model='articleclass'>
            <option v-for="option in options" v-bind:value="option.value">
            {{ option.text }}
            </option>
            </select>
          <label>类别</label>
        </div>
        </div>
    </li>
  </ul>
      <div class="row">
    <div class="input-field col s12">
        <textarea id="textarea1" v-model='content' class="materialize-textarea" v-on:drop="postImg(2)" ></textarea>
        <label for="textarea1">内容(Markdown)</label>
      </div>
    </div>
    <div class="row" style="text-align:center">
  <a class="waves-effect waves-light btn"  v-on:click="commit">上传</a>
    </div>
  </form>

  <div class="col s12 m6 l6">
  <div id='preview' class="col s12 card" >
  <div class="center flow-text" style="text-align:center;">
  <h4 >{{title}}</h4>
  <h6 class="author">{{author}}</h6>
  <h6 class="subtitle">{{subtitle}}</h6>
  </div>
  <hr></hr>
  <div id='pre_content' class=" content" v-html="precontent">
  </div>
  </div>
  <div class="col s12">
  <div class="parallax-container">
      <div class="parallax"><img v-bind:src='imgsrc'></div>
  </div>
  </div>
  </div>
  </div>
</template>

<script>
/* eslint-disable */
import Md from './common/markdown.js'
import {Article,User,Album} from './common/http.js'
import Cookie from './common/cookie.js'
import SQLDT from './common/sqldatetime.js'

export default {
  name: 'edit',
  data: function () {
   return {
    title: '',
    subtitle: '',
    imgsrc: '../static/images/bg4.jpg',
    author: '',
    articleclass: '1',
    content: ' ',
    create:'',
    id: '',
    options: [
      { text: '前端', value: '1' },
      { text: '后端', value: '2' },
      { text: 'AI', value: '3' },
      { text: '产品', value: '4' },
      { text: '设计', value: '5' },
      { text: '生活', value: '6' },
      { text: '函数式', value: '7' },
    ],
  }
  },
  computed: {
    precontent:function () {
        return Md.toHTML(this.content)
    }
  },
  mounted:function () {
    $('select').material_select();
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $(window).bind('beforeunload',function(){return '您输入的内容尚未保存，确定离开此页面吗？';});
    this.$route.params.type == 'revise' ? this.getArticle(this.$route.params.id) : null ;
  },
  watch: {
    '$route': function (to, from) {
      this.$route.params.type == 'revise' ? this.getArticle(this.$route.params.id) : null ;
    }
  },
  components: {
  },
  methods: {
    postImg: function (type) {
      let vm = this
      let fileObj
      type == 1 ? fileObj = event.target.files[0] : function(){event.preventDefault(); fileObj = event.dataTransfer.files[0]}()
      if(fileObj != undefined && fileObj.value != ''){
        Album.postImg(fileObj,(text) => {
          let Json=JSON.parse(text)
          Json.status == 'success' ? function () {type == 1 ? vm.imgsrc = '../static/images/'+Json.url : vm.content += "![]("+"../static/images/"+Json.url+")" }(): Materialize.toast('上传失败', 4000,'',function(){})
        })
      }else{
        Materialize.toast('你上传的是假文件', 4000,'',function(){})
      }
    },
    commit: function () {
      this.$route.params.type == 'revise' ? this.reviseArticle() : this.postArticle()  ;
    },
    postArticle: function () {
      this.articleclass=$('select')[0].value
      let vm = this
      let userData, token = ''
      let articleData = {title: vm.title, subtitle: vm.subtitle, img: vm.imgsrc, author: vm.author, create: SQLDT(), update: SQLDT(), content: vm.content, class: vm.articleclass,counts: '0'}
      Cookie.get('user') == '' ? function() {Materialize.toast('需要再次登录', 4000);vm.$router.push('/login')}() :userData = JSON.parse(Cookie.get('user'))
      User.login(userData,function(data,status){
        token = data['access_token']
        Article.create(articleData,token,function(data,status){
          data.status == 'success' ? Materialize.toast('发表成功', 4000) :Materialize.toast('发表失败：'+data.info, 4000)
        },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
        })
      },function(err){
        Materialize.toast('错误:'+err.statusText, 4000)
      })
    },
    reviseArticle: function () {
      this.articleclass=$('select')[0].value
      let vm = this
      let userData, token = ''
      let articleData = {id:vm.id,title: vm.title, subtitle: vm.subtitle, img: vm.imgsrc, author: vm.author, create: vm.create, update: SQLDT(), content: vm.content, class: vm.articleclass}
      Cookie.get('user') == '' ? function() {Materialize.toast('需要再次登录', 4000);vm.$router.push('/login')}() :userData = JSON.parse(Cookie.get('user'))
      User.login(userData,function(data,status){
        token = data['access_token']
        Article.revise(articleData,token,function(data,status){
          data.status == 'success' ? Materialize.toast('修改成功', 4000) :Materialize.toast('发表失败：'+data.info, 4000)
          },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
          })
    },function(err){
      Materialize.toast('错误:'+err.statusText, 4000)
    })
    },
    getArticle: function (id) {
      let vm = this
      Article.getOne({id:id},function (datas){
        let data=datas.data
        datas.status == 'error' ? function(){Materialize.toast('你改到了假文章,自动跳转...', 4000);vm.$router.push('/edit/create/0')}() : function(){
        vm.title = data.title
        vm.subtitle = data.subtitle
        vm.author = data.author
        vm.content = data.content
        vm.imgsrc = data.img
        vm.create = data.create
        vm.articleclass = data.class
        vm.id = data.id
        }();
      },function(err){
        Materialize.toast('假的:'+err.statusText, 4000)
      })
    }
  }
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
img{
  max-width:100%;
}
.parallax-container {
      height: 165px;
}
</style>
