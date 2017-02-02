<template>
  <div id="">
  <div class="parallax-container">
    <div class="parallax"><img src="../../static/images/bg.jpg"></div>
  </div>

  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'parallax',
  mounted: () => {
    $('.parallax').parallax();
  },
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style>
.parallax-container{
  height:150px;
}
</style>
