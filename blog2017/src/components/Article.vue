<template>
  <div id="">
  <card></card>
  <card></card>
  <card></card>
  <div class="col s12 l12 m12">
  <ul class="pagination center">
  <li class="disabled"><a href="#!"><i class="material-icons">chevron_left</i></a></li>
  <li class="active"><a href="#!">1</a></li>
  <li class="waves-effect"><a href="#!">2</a></li>
  <li class="waves-effect"><a href="#!">3</a></li>
  <li class="waves-effect"><a href="#!">4</a></li>
  <li class="waves-effect"><a href="#!">5</a></li>
  <li class="waves-effect"><a href="#!"><i class="material-icons">chevron_right</i></a></li>
  </ul>
  </div>
  </div>
</template>

<script>
/* eslint-disable */
import card from './Card'

export default {
  name: 'music',
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
