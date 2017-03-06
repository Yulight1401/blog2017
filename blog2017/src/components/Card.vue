<template>
  <div id="">
    <div class="col s12 m6 l4">
    <div class="card small sticky-action">
    <div class="card-image waves-effect waves-block waves-light">
      <img class="activator" v-bind:src="imgSrc" >
    </div>
    <div class="card-content" >
      <span class="card-title activator grey-text text-darken-4">{{articleData.title}}<i class="material-icons right">more_vert</i></span>
      <p style="position:absolute;bottom:18px;width:78%;background-color:white;"><router-link v-bind:to="articleSrc" tag="a">阅读</router-link></p>
    </div>
    <div class="card-reveal">
      <span class="card-title grey-text text-darken-4">{{articleData.title}}<i class="material-icons right">close</i></span>
      <p>{{articleData.subtitle}}</p>
    </div>
  </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'card',
  props: {
    articleData:{
      type: Object,
      default: function () {
        return {
          title: "",
          subtitle: "",
          img: "../static/images/bg4.jpg",
          articlesrc: "",
          id: ""
        }
      }
    }
  },
  computed: {
    imgSrc: function () {
      return "../"+this.articleData.img
    },
    articleSrc: function () {
      return "/articleone/"+this.articleData.id
    }
  },
  methods: {

  },
};
</script>

<style>
</style>
