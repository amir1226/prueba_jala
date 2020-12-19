<template>
  <div id="app">
    <lyricsFinder />
  </div>
</template>

<script>
import LyricsFinder from "./components/LyricsFinder.vue";
export default {
  name: "App",
  components: {
    LyricsFinder,
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
