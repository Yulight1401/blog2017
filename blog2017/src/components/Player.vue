<template>
  <div id="" class="col l4 m6 s12" style="margin:0 auto;">
  <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=auto height=86 src="//music.163.com/outchain/player?type=2&id=386844&auto=1&height=66"></iframe>
  </div>
</template>

<script>
/* eslint-disable */
import card from './Card'

export default {
  name: 'player',
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
  components: {
    card
  }
};
</script>

<style>
</style>
