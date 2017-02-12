<template>
  <div id="" class="col s12" >
  <div class="col s12" style="text-align:center">
  <div class="preloader-wrapper small active" style="" v-if="loading">
    <div class="spinner-layer spinner-gray-only">
      <div class="circle-clipper left">
        <div class="circle"></div>
      </div><div class="gap-patch">
        <div class="circle"></div>
      </div><div class="circle-clipper right">
        <div class="circle"></div>
      </div>
    </div>
  </div>
  </div>
  <ul class="collapsible popout " data-collapsible="expandable">
  <li v-for="item in Datas">
    <div class="collapsible-header">{{item.name}}<span class="badge"><a v-on:click.stop="reComment" v-bind:data-id="item.id" v-bind:data-fid="item.id" v-bind:data-usname="item.name" class="waves-effect waves-teal btn-flat">回复</a></span> <span class="badge">评论数：{{item.for}}</span><span class="badge" >发布于：{{item.create}}</span></div>

    <div class="collapsible-body">
    <p>{{item.content}}</p>
    <hr></hr>

    <ul class="collection">
    <li class="collection-item avatar" v-for="its in item.sonData">
      <span class="title">{{its.name}} </span>
      <br>
      {{its.content}}
      <br><span class="badge">评论数：{{its.for}}</span><span class="badge" >发布于：{{its.create}}</span>
      <a class="secondary-content"><span class="badge"><a v-on:click.stop="reComment" v-bind:data-id="its.id" v-bind:data-fid="item.id" v-bind:data-usname="its.name" class="waves-effect waves-light btn">回复</a></a>
    </li>
    </ul>
  </li>

  </ul>
  </div>
</template>

<script>
/* eslint-disable */
import {Comment} from '../common/http.js'

export default {
  name: 'comment',
  data: function () {
    return{
      Datas:[],
      loading:true
    }
  },
  created : function () {
    this.getData()
  },
  props :['articleId','render'],
  mounted: function () {
    $('.collapsible').collapsible();
    $('.parallax').parallax();
    this.getData()
  },
  watch:{
    'render': function(){
      this.getData()
    },
    '$route': function(to,from){
      this.getData()
    }
  },
  computed: {
  },
  methods: {
    getData : function () {
      let vm = this
      let fData = []
      Comment.getByarticle({id:vm.articleId},function(data,status){
        fData = data.data
        fData.length == 0 ? vm.loading=false : null ;
        for( let item in fData){
        console.log(item,fData.length)
        Comment.getByson({id:fData[item].id},function(data,status){
          let tempData = data.data
          fData[item].sonData = tempData
          item == fData.length-1 ? function(){vm.Datas = fData;vm.loading=false}() : () => {}
        },function(err){
          Materialize.toast('获取子评论错误:'+err.statusText, 4000)
        })
        }
        },function(err){
        Materialize.toast('获取文章评论错误:'+err.statusText, 4000)
      })
    },
    reComment: function () {
      this.$store.commit('commentState',{type:'comment',id:event.target.dataset.id, name:event.target.dataset.usname, fid:event.target.dataset.fid})
      $('#modal1').modal('open')
    }
  },
  components: {
  }
};
</script>

<style scoped>
.center{
display:block;
text-align:center!important;
}
.content{
  font-size:16px;
  text-indent:32px;
  font-weight:light;
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
</style>
