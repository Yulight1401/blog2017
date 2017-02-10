<template>
  <div id="" class="col s12">
  <ul class="collapsible popout " data-collapsible="expandable">
  <li v-for="item in Datas">
    <div class="collapsible-header">{{item.name}}<span class="badge"><a v-on:click.stop="reComment" v-bind:data-id="item.id" class="waves-effect waves-teal btn-flat">回复</a></span> <span class="badge">评论数：{{item.for}}</span><span class="badge" >发布于：{{item.create}}</span></div>

    <div class="collapsible-body">
    <p>{{item.content}}</p>
    <hr></hr>

    <ul class="collection">
    <li class="collection-item avatar" v-for="its in item.sonData">
      <span class="title">{{its.name}} </span>
      <br>
      {{its.content}}
      <br><span class="badge">评论数：{{its.for}}</span><span class="badge" >发布于：{{its.create}}</span>
      <a class="secondary-content"><span class="badge"><a v-on:click.stop="reComment" v-bind:data-id="item.id" class="waves-effect waves-light btn">回复</a></a>
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
      SDatas:[]
    }
  },
  props :['articleId'],
  mounted: function () {
    $('.collapsible').collapsible();
    $('.parallax').parallax();
  },
  created: function(){
    this.getByarticle()
  },
  watch: {
    '$route' : function (to, from){

    }
  },
  computed: {
  },
  methods: {
    getByarticle: function () {
      let vm=this
      let arrayS
      Comment.getByarticle({id:vm.articleId},function(data,status){
        vm.SDatas = data.data
        vm.SDatas.forEach(function(item,index){
          vm.getByson(item,index)
        })
        },function(err){
        Materialize.toast('获取文章评论错误:'+err.statusText, 4000)
      })
    },
    getByson: function (item,index) {
      let vm=this
      let SDatas=[]
      Comment.getByson({id:item.id},function(data,status){
        SDatas = data.data
        vm.SDatas[index].sonData=SDatas
        vm.Datas=vm.SDatas
        console.log(JSON.stringify(vm.Datas))
      },function(err){
        Materialize.toast('获取子评论错误:'+err.statusText, 4000)
      })
    },
    reComment: function () {
      this.$store.commit('commentState',{type:'comment',id:event.target.dataset.id})
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
