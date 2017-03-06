<template>
  <div id="sidenav" style="height:60px;">
  <ul id="slide-out" class="side-nav fixed">
 <li><div class="userView">
   <div class="background" >
     <img width=300 height=160 src="../../static/images/bg4.jpg">
   </div>
   <a href="#!user"><img class="circle" src="../../static/images/my.jpg"></a>
   <a href="#!name"><span class="white-text name">Yul</span></a>
   <a href="#!email"><span class="white-text email">Someone die in 20 , but burried in 80</span></a>
 </div></li>
 <li>
 <ul class="collapsible" data-collapsible="accordion">
 <li>
     <div class="collapsible-header "><i class="material-icons" ><svg style="width:24px;height:24px;position:relative;" viewBox="0 0 24 24">
        <path fill="#000000" d="M14,17H7V15H14M17,13H7V11H17M17,9H7V7H17M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z" />
    </svg></i>Articles</div>
     <div class="collapsible-body">
       <ul class="materialize-list">
         <router-link to="/article/1" tag="li" class="">FrontEnd</router-link>
         <router-link to="/article/2" tag="li" class="">BackEnd</router-link>
         <router-link to="/article/3" tag="li" class="">Ai</router-link>
         <router-link to="/article/4" tag="li" class="">Product</router-link>
         <router-link to="/article/5" tag="li" class="">Design</router-link>
         <router-link to="/article/6" tag="li" class="">Life</router-link>
         <router-link to="/article/7" tag="li" class="">Haskell</router-link>
       </ul>
     </div>
   </li>
   <li >
     <div class="collapsible-header"><i class="material-icons"><svg style="width:24px;height:24px" viewBox="0 0 24 24">
        <path fill="#000000" d="M17,12V7L12,2V7H7L2,12H7V17L12,22V17H17L22,12H17M12.88,12.88L12,15.53L11.12,12.88L8.47,12L11.12,11.12L12,8.46L12.88,11.11L15.53,12L12.88,12.88Z" />
    </svg></i>Album</div>
     <div class="collapsible-body">
     <ul class="materialize-list">
       <router-link to="/album/1" tag="li" class="">Life</router-link>
       <router-link to="/album/2" tag="li" class="">Photograph</router-link>
       <router-link to="/album/3" tag="li" class="">Painting</router-link>
      </ul>
     </div>
   </li>
   <li >
     <div class="collapsible-header"><i class="material-icons"><svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#000000" d="M16,9V7H12V12.5C11.58,12.19 11.07,12 10.5,12A2.5,2.5 0 0,0 8,14.5A2.5,2.5 0 0,0 10.5,17A2.5,2.5 0 0,0 13,14.5V9H16M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2Z" />
</svg></i>Music</div>
     <div class="collapsible-body">
     <ul class="materialize-list">
       <router-link to="/music" tag="li" class="">Songs</router-link>
       <router-link to="/mv" tag="li" class="">Mv</router-link>
      </ul>
     </div>
   </li>
   <li>
     <div class="collapsible-header"><i class="material-icons" ><svg style="width:24px;height:24px" viewBox="0 0 24 24">
        <path fill="#000000" d="M13.5,4A1.5,1.5 0 0,0 12,5.5A1.5,1.5 0 0,0 13.5,7A1.5,1.5 0 0,0 15,5.5A1.5,1.5 0 0,0 13.5,4M13.14,8.77C11.95,8.87 8.7,11.46 8.7,11.46C8.5,11.61 8.56,11.6 8.72,11.88C8.88,12.15 8.86,12.17 9.05,12.04C9.25,11.91 9.58,11.7 10.13,11.36C12.25,10 10.47,13.14 9.56,18.43C9.2,21.05 11.56,19.7 12.17,19.3C12.77,18.91 14.38,17.8 14.54,17.69C14.76,17.54 14.6,17.42 14.43,17.17C14.31,17 14.19,17.12 14.19,17.12C13.54,17.55 12.35,18.45 12.19,17.88C12,17.31 13.22,13.4 13.89,10.71C14,10.07 14.3,8.67 13.14,8.77Z" />
    </svg></i>Info</div>
     <div class="collapsible-body"><p>A poor boy, keep going</p></div>
   </li>
   <router-link to="/login" v-if="loginState" tag="li" class=""><div class="collapsible-header"><i class="material-icons" ><svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#000000" d="M19,3H5C3.89,3 3,3.89 3,5V9H5V5H19V19H5V15H3V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M10.08,15.58L11.5,17L16.5,12L11.5,7L10.08,8.41L12.67,11H3V13H12.67L10.08,15.58Z" />
</svg></i>Login</div></router-link>
<router-link to="/regist" tag="li" v-if="loginState" class=""><div class="collapsible-header"><i class="material-icons" ><svg style="width:24px;height:24px" viewBox="0 0 24 24">
<path fill="#000000" d="M15,14C12.33,14 7,15.33 7,18V20H23V18C23,15.33 17.67,14 15,14M6,10V7H4V10H1V12H4V15H6V12H9V10M15,12A4,4 0 0,0 19,8A4,4 0 0,0 15,4A4,4 0 0,0 11,8A4,4 0 0,0 15,12Z" />
</svg></i>Regist</div></router-link>
<router-link to="/info" tag="li" v-if="!loginState" class=""><div class="collapsible-header"><i class="material-icons" ><svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#000000" d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
</svg></i>Account</div></router-link>
   </ul>
 </li>
  </ul>
<a href="#" data-activates="slide-out" class="button-collapse " style="position:fixed;left:20px;top:10px;height:60px;z-index:200;"><i class="material-icons"><svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#BC8F8F" d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" />
</svg></i></a>
       </div>
</template>

<script>
/* eslint-disable */
import Cookie from '../common/cookie.js'

export default {
  name: 'sidenav',
  mounted:function (){
    $(".button-collapse").sideNav();
    $('.collapsible').collapsible();
    Cookie.get('user') == '' ? this.$store.commit('loginState', true) : this.$store.commit('loginState', false)
  },
  computed: {
    loginState: function (){
      return this.$store.state.login
    },
  },
  watch: {
    '$route' (to,from){
      //console.log(to)
      //alert(document.body.scrollWidth)
      this.$store.commit('loadingState', true)
      document.body.scrollWidth <= 1024 ? $('.button-collapse').sideNav('hide') : ()=>{}
    }
  },
  methods: {
    show: () => {
      $('.button-collapse').sideNav('show');
    },
  },
};
</script>

<style scoped>
*::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 0px;
	background-color: #F5F5F5;
}

*::-webkit-scrollbar
{
	width: 0px;
	background-color: #F5F5F5;
}

*::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #555;
}
.materialize-list li{
  width:100%;
  text-align:left;
  text-indent:21%;
  transition:all 0.2s ease-in-out;
}
.materialize-list li:hover{
  cursor:pointer;
  background-color:#EEEEEE;
}
.active{
 background-color:#bdbdbd!important;
}
</style>
