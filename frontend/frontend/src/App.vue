<template>
  <div id="app">
    <center><MyHeader title="BlinkPad Internship Project" /></center>
    <div class="float-container">
      <MyPost id="1" image="test.jpeg" />
      <MyPost id="2" image="test.jpeg" />
    </div>
    <div class="float-container">
      <MyPost id="3" image="test1.jpeg" />
      <MyPost id="4" image="test1.jpeg" />
    </div>
  </div>
</template>

<script lang="ts">
//import posts from "./data/posts.json";
import { defineComponent } from "vue";
import MyHeader from "./components/MyHeader.vue";
import MyPost from "./components/MyPost.vue";

export default defineComponent({
  name: "App",
  components: {
    MyHeader,
    MyPost,
  },
});
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: "Poppins", sans-serif;
}
.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.float-container {
  border: 3px solid #fff;
  padding: 20px;
}
.float-child {
  width: 50%;
  height: 100%;
  float: left;
  padding: 20px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.95);
}
.btn-block {
  display: block;
  width: 100%;
}
img {
  float: left;
  width: 300px;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
}
</style>
