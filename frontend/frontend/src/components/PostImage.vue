<template>
  <div>
    <img :src="require(`@/assets/img/${filename}`)" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PostImage",
  props: {
    filename: String,
  },
});
</script>
