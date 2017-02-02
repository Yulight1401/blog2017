<template>
  <div id="" class="row">
    <player></player>
    <player></player>
    <player></player>
  </div>
</template>

<script>
/* eslint-disable */
import player from './Player'

export default {
  name: 'articleone',
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
