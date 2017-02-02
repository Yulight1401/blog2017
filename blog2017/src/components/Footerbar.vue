<template>
  <div id="footer">
  <footer class="page-footer grey darken-">
        <div class="container">
          <div class="row">
            <div class="col l6 s12">
              <h5 class="white-text"></h5>
              <p class="grey-text text-lighten-4">Stay foolish,Stay hungry</p>
            </div>
          </div>
        </div>
        <div class="footer-copyright">
          <div class="container">
          © 2017 Copyright Yul
          <a class="grey-text text-lighten-4 right" href="#!"></a>
          </div>
        </div>
      </footer>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'footerbar',
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style scoped>

</style>
