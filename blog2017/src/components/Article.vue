<template>
  <div id="">
  <transition-group name="list" >
  <card v-for="item in artDatas" v-bind:articleData ="item" v-bind:key="item"></card>
  </transition-group>
  </div>
</template>

<script>
/* eslint-disable */
import card from './Card'
import {Article} from '../common/http.js'

export default {
  name: 'article',
  data: function () {
    return {
      artDatas:[]
    }
  },
  mounted: function () {
    let vm = this
    Article.getAll(this.$route.params,function(data,status){
      vm.artDatas = data.data
    },function(err){
      Materialize.toast('获取文章信息错误：'+err.statusText, 4000)
    })
  },
  watch :{
    '$route' : function (to, from){
      let vm = this
      Article.getAll(to.params,function(data,status){
        vm.artDatas = data.data
      },function(err){
        Materialize.toast('获取文章信息错误：'+err.statusText, 4000)
      })
      }
  },
  methods: {

  },
  components: {
    card
  }
};
</script>

<style>
.list-item {
  display: inline-block;
  margin-right: 0px;
}
.list-enter-active, .list-leave-active {
  transition: all 0.5s;
}
.list-enter, .list-leave-to /* .list-leave-active for <2.1.8 */ {
  opacity: 0;
  transform: translateY(20px);
}
.list-move{
  transition: transform 0.5s;
}
</style>
