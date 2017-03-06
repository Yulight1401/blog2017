<template>
  <div id="" class="row">
  <div style="display:none">
    <img v-bind:src = "imgSrc"/>
  </div>
  <div class="fixed-action-btn ">
    <a class="btn-floating btn-large grey waves-effect" v-on:click="articleComment">
      <i class="large material-icons">mode_edit</i>
    </a>
  </div>
  <div class="card article col s12">
    <div class="center flow-text" style="text-align:center;">
    <h4 >{{artData.title}}</h4>
    <h6 class="author">{{artData.author}}</h6>
    <h6 class="subtitle">{{artData.subtitle}}</h6>
    </div>
    <hr></hr>
    <div class="Mycontent" id='parsecontent' v-html="parsecontent">
    </div>
    <hr></hr>
    <div class="foot"><span class="badge" data-badge-caption="">阅读量：{{artData.counts}}</span><span class="badge" >更新于：{{artData.update}}</span><span class="badge" >发布于：{{artData.create}}</span></div>
    </div>
    <div class="parallax-container col s12">
        <div class="parallax"><img v-bind:src = "imgSrc"></div>
    </div>
    <comment v-bind:articleId="artData.id" v-bind:render="render"></comment>
    <inputpanel v-on:commit="renderComment"></inputpanel>
  </div>
</template>

<script>
/* eslint-disable */
import inputpanel from './inputPanel'
import comment from './comment'
import Md from '../common/markdown.js'
import {Article} from '../common/http.js'

export default {
  name: 'article',
  data: function () {
    return{
      artData:{
        id: 1,
        content:'  ',//由于刚开始content为undefiend所以会引起slice属性不存在的bug
      },
      parsecontent: '',
      render:0,
      loading:true
    }
  },
  mounted: function () {
    $('.parallax').parallax();
    let vm = this
    vm.getArticle()
    vm.countArt()
  },
  computed: {
    imgSrc: function () {
      return '../'+this.artData.img
    }
  },
  watch: {
    '$route' : function (to, from){
    let vm = this
    Article.getOne(to.params,function(data,status){
      vm.artData = data.data
    },function(err){
      Materialize.toast('获取文章信息错误：'+err.statusText, 4000)
    })
    }
  },
  methods: {
    renderComment: function () {
       this.render++
    },
    getArticle: function () {
    let vm = this
    Article.getOne(this.$route.params,function(data,status){
      vm.artData = data.data
      vm.$store.commit('loadingState',false)
      vm.parsecontent = Md.toHTML(vm.artData.content)
      document.title = data.data.title
      document.subtitle = data.data.subtitle
      setTimeout(function(){
      $('#parsecontent img').addClass('materialboxed mx_width')
      $('.materialboxed').materialbox()
      vm.render++
      },100)
      },function(err){
      Materialize.toast('获取文章信息错误：'+err.statusText, 4000)
    })
    },
    countArt: function () {
      Article.count(this.$route.params,function(){
        console.log('')
      },function(err){
        Materialize.toast('文章计数错误：'+err.statusText, 4000)
      })
    },
    articleComment: function () {
      let vm=this
      this.$store.commit('commentState',{type:'article',id:this.$route.params.id})
      $('#modal1').modal('open')
    }
  },
  components: {
    inputpanel,
    comment,
  }
};
</script>

<style>
.center{
display:block;
text-align:center!important;
}
.Mycontent{
  font-size:16px;
  text-indent:32px;
  font-weight: normal;
  max-width: 100%;
  overflow: hidden;
}
.card{
  padding:8px;
}
.author{
  color:#616161;
}
.subtitle{
  color:#424242;
  margin-bottom:10px;
}
.foot{
  height:30px;
  line-height:30px;
}
.parallax-container {
      height: 125px;
}
.mx_width{
  max-width:100%;
  margin:0 auto;
}
</style>
