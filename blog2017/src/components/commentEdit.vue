<template>
  <div id="comment-modal">
  <a class="modal-trigger waves-effect waves-light btn" href="#modal1">Modal</a>

<!-- Modal Structure -->
<div id="modal1" class="modal modal-fixed-footer">
  <div class="modal-content">
    <h4>Modal Header</h4>
    <p>A bunch of text</p>
  </div>
  <div class="modal-footer">
    <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat ">Agree</a>
  </div>
</div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'comment-modal',
  mounted: () => {
    $('.modal').modal();
  }
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
