<template>
  <div id="">
    <div class="col s12 m6 l4">
    <div class="card small sticky-action">
    <div class="card-image waves-effect waves-block waves-light">
      <img class="activator"  src="../../static/images/bg4.jpg">
    </div>
    <div class="card-content">
      <span class="card-title activator grey-text text-darken-4">Card Title<i class="material-icons right">more_vert</i></span>
      <p><router-link to="/articleone" tag="a">阅读</router-link></p>
    </div>
    <div class="card-reveal">
      <span class="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
      <p>Here is some more information about this product that is only revealed once clicked on.</p>
    </div>
  </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'card',
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style>
</style>
