<template>
  <div class="float-child">
    <PostImage :filename="image" />
    <div class="float-child">
      <center><button @click="onUpvote()" class="btn">+1</button></center>
    </div>
    <div class="float-child">
      <center>
        <h1>{{ score }}</h1>
      </center>
    </div>
    <div class="float-child">
      <center><button @click="onDownvote()" class="btn">-1</button></center>
    </div>
  </div>
</template>

<script lang="ts">
import PostImage from "./PostImage.vue";
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  name: "MyPost",
  methods: {
    onUpvote() {
      this.updateScore(1);
    },
    onDownvote() {
      this.updateScore(-1);
    },
    getScore() {
      const path = "http://localhost:5050/score/";
      axios
        .get(path, {
          params: {
            post_id: this.post_id,
          },
        })
        .then((res) => {
          this.score = res.data.score;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    updateScore(value: number) {
      const path = "http://localhost:5050/score/";
      axios
        .post(path, {
          post_id: this.post_id,
          val: String(value),
        })
        .then(() => {
          this.getScore();
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  data: function () {
    return {
      score: 0,
      post_id: 0,
    };
  },
  created: function () {
    console.log("Post created");
    this.post_id = Number(this.id);
    this.getScore();
  },
  props: {
    image: String,
    id: String,
    likes: Number,
  },
  components: {
    PostImage,
  },
});
</script>
