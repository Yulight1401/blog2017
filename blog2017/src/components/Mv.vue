<template>
  <div id="" class="col l12 m12 s12">
  <div class="video-container">
        <iframe width="auto" height="480" src="//www.youtube.com/embed/Q8TXgCzxEnw?rel=0" frameborder="0" allowfullscreen></iframe>
      </div>
      <div class="video-container">
            <iframe width="auto" height="480" src="https://www.youtube.com/embed/IwL3l6rcUJ0" frameborder="0" allowfullscreen></iframe>          </div>
          <div class="video-container">
                <iframe width="auto" height="480" src="https://www.youtube.com/embed/p1mrRVA92Do" frameborder="0" allowfullscreen></iframe>              </div>
      <div class="video-container">
        <iframe width="auto" height="480" src="https://www.youtube.com/embed/wdypZWuoKvQ" frameborder="0" allowfullscreen></iframe>
      </div>
      <div class="video-container">
        <iframe width="auto" height="480" src="https://www.youtube.com/embed/LbuuTeGGwnY" frameborder="0" allowfullscreen></iframe>
      </div>
    </div>
</template>

<script>
/* eslint-disable */
import card from './Card'

export default {
  name: 'mv',
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
