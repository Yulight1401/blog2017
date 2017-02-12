<template>
  <!-- Modal Structure -->
  <div id="modal1" class="modal bottom-sheet">
    <div class="modal-content">
    <form class="col s12">
      <div class="row">
        <div class="input-field col s12">
          <textarea id="textarea1" class="materialize-textarea" length="120"  v-model="content"></textarea>
          <label for="textarea1" >评论</label>
        </div>
      </div>
    </form>
    </div>
    <div class="modal-footer">
      <a v-on:click.stop="validContent" class=" modal-action modal-close waves-effect waves-green btn-flat">发表</a>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import {Comment,User} from '../common/http.js'
import Cookie from '../common/cookie.js'
import SQLDT from '../common/sqldatetime.js'

export default {
  name: 'inputpanel',
  data: function (){
    return{
      content: "",
    }
  },
  mounted:() => {
    $('input#input_text, textarea#textarea1').characterCounter();
    $('.modal').modal();
  },
  methods: {
    createComment: function () {
      let vm = this
      let userData,commentData,token
      Cookie.get('user') == '' ? function() {Materialize.toast('需要再次登录', 4000);vm.$router.push('/login')}() :userData = JSON.parse(Cookie.get('user'))
      vm.$store.state.commentData.type == 'article' ? commentData = {name:userData.username,fatherid:'-1',sonid:vm.$store.state.commentData.id,create:SQLDT(),title:'',content:vm.content,for:0}:
      function(){
        commentData = {name:userData.username+' 回复 ['+vm.$store.state.commentData.name+']',fatherid:vm.$store.state.commentData.fid,sonid:'-1',create:SQLDT(),title:'',content:vm.content,for:0}
        Comment.count({id:vm.$store.state.commentData.id},function(){},function(){})
      }()
      User.login(userData,function(data,status){
        token = data['access_token']
        Comment.create(commentData,token,function(data,status){
          Materialize.toast('评论成功', 4000)
          vm.$emit('commit')
          $('#modal1').modal('close')
        },function(err){
          Materialize.toast('错误:'+err.statusText, 4000)
          $('#modal1').modal('close')
        })
      },function(){})
    },
    validContent: function () {
      let vm=this
      vm.content.length >5 ? vm.createComment() :Materialize.toast('评论过短', 4000)
    }
  },
};
</script>

<style>
</style>
