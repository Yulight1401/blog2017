<template>
  <div id="app2">
    <!-- Navbar goes here -->

    <!-- Page Layout here -->
    <div class="row">

      <div class="col l3"> <!-- Note that "m4 l3" was added -->
        <!-- Grey navigation panel

              This content will be:
          3-columns-wide on large screens,
          4-columns-wide on medium screens,
          12-columns-wide on small screens  -->
          <sidenav></sidenav>
      </div>

      <div class="col s12 m12 l9"> <!-- Note that "m8 l9" was added -->
        <!-- Teal page content

              This content will be:
          9-columns-wide on large screens,
          8-columns-wide on medium screens,
          12-columns-wide on small screens  -->
          <loader v-if="false"></loader>
          <div class="row">
          <transition name="slide-fade">
          <router-view></router-view>
          </transition>
          </div>
          <footerbar></footerbar>
      </div>

    </div>

  </div>
</template>

<script>
/* eslint-disable */
import sidenav from './components/Sidenav';
import footerbar from './components/Footerbar'
import card from './components/Card'
import loader from './components/Loader'
import parallax from './components/parallax'
import carousel from './components/Carousel'
window.$ = window.jQuery = require('jquery');

export default {
  name: 'app',
  mounted: () =>{
    $('.carousel').carousel();
    $('.parallax').parallax();
  },
  components: {
    sidenav,
    footerbar,
    card,
    loader,
    carousel,
    parallax
  },
};
</script>

<style>
.slide-fade-enter-active {
  transition: all 0.8s ease;
}
.slide-fade-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for <2.1.8 */ {
  transform: translateY(30px);
  opacity: 0;
}
</style>
