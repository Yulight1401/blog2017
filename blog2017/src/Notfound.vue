<template>
  <div id="not_found">
  <svg id="404_svg" viewBox="0 0 600 300">

<!-- Symbol -->
<symbol id="s-text">
<text text-anchor="middle" x="50%" y="50%" dy=".35em"> 404 </text>
</symbol>

<!-- Duplicate symbols -->
<use xlink:href="#s-text" class="text"></use>
<use xlink:href="#s-text" class="text"></use>
<use xlink:href="#s-text" class="text"></use>
<use xlink:href="#s-text" class="text"></use>
<use xlink:href="#s-text" class="text"></use>

</svg>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'Notfound',
  mounted: () =>{
    document.title='404 Error'
  },
  components: {
  },
};
</script>

<style >

.text {
fill: none;
stroke-width: 4;
stroke-linejoin: round;
stroke-dasharray: 70 330;
stroke-dashoffset: 0;
-webkit-animation: stroke 6s infinite linear;
animation: stroke 6s infinite linear;
}

.text:nth-child(5n + 1) {
stroke: #bdbdbd;
-webkit-animation-delay: -1.2s;
animation-delay: -1.2s;
}
.text:nth-child(5n + 2) {
stroke: #757575;
-webkit-animation-delay: -2.4s;
animation-delay: -2.4s;
}

.text:nth-child(5n + 3) {
stroke: #424242;
-webkit-animation-delay: -3.6s;
animation-delay: -3.6s;
}

.text:nth-child(5n + 4) {
stroke: #56D9CD;
-webkit-animation-delay: -4.8s;
animation-delay: -4.8s;
}

.text:nth-child(5n + 5) {
stroke: #212121;
-webkit-animation-delay: -6s;
animation-delay: -6s;
}

@-webkit-keyframes stroke {
100% {
stroke-dashoffset: -400;
}
}

@keyframes stroke {
100% {
stroke-dashoffset: -400;
}
}

/* Other styles */
#not_found {
height: 100%;
}

#not_found {
background: #fafafa;
background-size: .2em 100%;
font: 14.5em/1 Open Sans, Impact;
text-transform: uppercase;
margin: 0;
}

#404_svg {
position: absolute;
width: 100%;
height: 100%;
}
</style>
