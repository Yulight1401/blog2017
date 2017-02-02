<template>
  <div id="imageslist" class="row center">
  <div class="col s12 m6 l4">
  <img class="materialboxed" width="650" src="../../static/images/bg.jpg">
  <img class="materialboxed" width="650" src="../../static/images/bg2.jpg">
  </div>
  <div class="col s12 m6 l4">
  <img class="materialboxed" width="650" src="../../static/images/bg3.jpg">
  <img class="materialboxed" width="650" src="../../static/images/bg4.jpg">
  </div>
  <div class="col s12 m6 l4">
  <img class="materialboxed" width="650" src="../../static/images/bg5.jpg">
  <img class="materialboxed" width="650" src="../../static/images/bg3.jpg">
  <img class="materialboxed" width="650" src="../../static/images/bg4.jpg">
  </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'album',
  mounted:() =>{
    $('.materialboxed').materialbox();
    Materialize.showStaggeredList('#staggered-test')
  },
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
  components: {

  }
};
</script>

<style scoped>
img{
width:300px;
height:auto;
margin:0 auto;
padding:0px 0 5px 0;
}
</style>
