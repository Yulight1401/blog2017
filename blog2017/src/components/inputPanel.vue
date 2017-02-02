<template>
  <!-- Modal Structure -->
  <div id="modal1" class="modal bottom-sheet">
    <div class="modal-content">
    <form class="col s12">
      <div class="row">
        <div class="input-field col s12">
          <textarea id="textarea1" class="materialize-textarea" length="120"></textarea>
          <label for="textarea1">评论</label>
        </div>
      </div>
    </form>
    </div>
    <div class="modal-footer">
      <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">发表</a>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'inputpanel',
  mounted:() => {
    $('input#input_text, textarea#textarea1').characterCounter();
    $('.modal').modal();
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
</style>
