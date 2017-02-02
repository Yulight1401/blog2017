<template>
  <div id="">
  <div class="fixed-action-btn ">
    <a class="btn-floating btn-large grey waves-effect" href="#modal1">
      <i class="large material-icons">mode_edit</i>
    </a>
  </div>
  <div class="card article">
    <div class="center flow-text" style="text-align:center;">
    <h4 >最新博客发布</h4>
    <h6 class="author">Yul</h6>
    <h6 class="subtitle">耗时10天，翻天覆地</h6>
    </div>
    <hr></hr>
    <div class="flow-text content">
      新版博客重新启动
    <p>  细节：</p>
实现用户数据库，只用包括名字，密码，github主页，（头像）。文章：大图，标题，简介，作者，内容，首次上传时间，阅读次数，更新时间,类别。后台：一个良好写作体验的富文本编辑器，包括预览，上传图片等。评论表，fatherid(如果是字评论，对应父评论id),_id,son(是否是字评论),name,content,updatetime。登录的接口需要在回应头设置cookie，发布文章时，后端检查cookie。
    </div>
    <hr></hr>
    <div class="foot"><span class="badge" data-badge-caption="阅读">4</span><span class="badge" >2017-1-1 12:00:03</span></div>
    </div>
    <div class="parallax-container">
        <div class="parallax"><img src="../../static/images/bg4.jpg"></div>
      </div>
    <ul class="collapsible popout " data-collapsible="expandable">
  <li>
    <div class="collapsible-header">Yul <span class="badge"><i class="material-icons"><svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#888888" d="M12.1,18.55L12,18.65L11.89,18.55C7.14,14.24 4,11.39 4,8.5C4,6.5 5.5,5 7.5,5C9.04,5 10.54,6 11.07,7.36H12.93C13.46,6 14.96,5 16.5,5C18.5,5 20,6.5 20,8.5C20,11.39 16.86,14.24 12.1,18.55M16.5,3C14.76,3 13.09,3.81 12,5.08C10.91,3.81 9.24,3 7.5,3C4.42,3 2,5.41 2,8.5C2,12.27 5.4,15.36 10.55,20.03L12,21.35L13.45,20.03C18.6,15.36 22,12.27 22,8.5C22,5.41 19.58,3 16.5,3Z" />
</svg>
<svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="#888888" d="M12,21.35L10.55,20.03C5.4,15.36 2,12.27 2,8.5C2,5.41 4.42,3 7.5,3C9.24,3 10.91,3.81 12,5.08C13.09,3.81 14.76,3 16.5,3C19.58,3 22,5.41 22,8.5C22,12.27 18.6,15.36 13.45,20.03L12,21.35Z" />
</svg>
</i>124</span><span class="badge" >发布于：2017-6-18 16:00</span></div>
    <div class="collapsible-body">
    <p>THis</p>
    <hr></hr>
    <ul class="collection">
    <li class="collection-item avatar">
      <span class="title">Title</span>
      <p>First Line <br>
         Second Line
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
    <li class="collection-item avatar">
      <span class="title">Title</span>
      <p>First Line <br>
         Second Line
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
    <li class="collection-item avatar">
      <i class="material-icons circle green">insert_chart</i>
      <span class="title">Title</span>
      <p>First Line <br>
         Second Line
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
    <li class="collection-item avatar">
      <i class="material-icons circle red">play_arrow</i>
      <span class="title">Title</span>
      <p>First Line <br>
         Second Line
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
  </ul>
  </li>
  <li>
    <div class="collapsible-header">Yul</div>
    <div class="collapsible-body"><p>Lorem ipsum dolor sit amet.</p></div>
  </li><li>
    <div class="collapsible-header">Yul</div>
    <div class="collapsible-body"><p>Lorem ipsum dolor sit amet.</p></div>
  </li>
</ul>
  <inputpanel></inputpanel>
  </div>
</template>

<script>
/* eslint-disable */
import inputpanel from './inputPanel'

export default {
  name: 'article',
  mounted: () => {
    $('.collapsible').collapsible();
    $('.parallax').parallax();
  },
  methods: {
    show: () => {
      console.log('???');
      $('.button-collapse').sideNav('show');
    },
  },
  components: {
    inputpanel,
  }
};
</script>

<style scoped>
.center{
display:block;
text-align:center!important;
}
.content{
  font-size:16px;
  text-indent:32px;
  font-weight:light;
}
.card{
  padding:8px;
}
.author{
  color:#616161;
}
.subtitle{
  color:#424242;
  margin-bottom:10px;
}
.foot{
  height:30px;
  line-height:30px;
}
.parallax-container {
      height: 165px;
}
</style>
