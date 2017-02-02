<template>
  <div id="loader">
  <div class="preloader-wrapper active">
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
</template>

<script>
/* eslint-disable */

export default {
  name: 'loader',
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style scoped>
#loader{
  position:relative;
  width:20%;
  left:50%;
  overflow:hidden;
  margin-left:-24px;
}
</style>
