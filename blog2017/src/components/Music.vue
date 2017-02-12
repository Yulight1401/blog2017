<template>
  <div id="" class="row">
    <player></player>
    <div id="" class="col l4 m6 s12" style="margin:0 auto;">
    <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=auto height=86 src="//music.163.com/outchain/player?type=2&id=5183847&auto=0&height=66"></iframe>
    </div>
    <div id="" class="col l4 m6 s12" style="margin:0 auto;">
    <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=auto height=86 src="//music.163.com/outchain/player?type=2&id=412187573&auto=0&height=66"></iframe>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import player from './Player'

export default {
  name: 'articleone',
  mounted:function () {
    document.title = "Yul's Music"
    this.$store.commit('loadingState',false)
  },
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
  components: {
    player,
  }
};
</script>

<style>
</style>
