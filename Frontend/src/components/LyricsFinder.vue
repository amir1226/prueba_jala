<template>
  <div class="mt-5">
    <form>
      <b-row class="justify-content-md-center mt-5">
        <b-col cols="12" md="3">
          <p class="h3">Artist</p>
        </b-col>
        <b-col cols="12" md="6">
          <b-form-input type="text" v-model="artist" placeholder="Enter text">
          </b-form-input>
        </b-col>
      </b-row>

      <b-row class="justify-content-md-center mt-3">
        <b-col cols="12" md="3">
          <p class="h3">Song</p>
        </b-col>
        <b-col cols="12" md="6">
          <b-form-input type="text" v-model="song" placeholder="Enter text">
          </b-form-input>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center mt-3">
        <b-col class="mt-3" md="4">
          <b-button variant="primary" @click="findLyric">Find Lyrics!</b-button>
        </b-col>
        <b-col class="mt-3" md="4">
          <b-button variant="secondary" @click="translateLyric"
            >Translate</b-button
          >
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center mt-3">
        <b-col sm="10">
          <div>
            <p class="h4">Lyrics</p>
            <b-form-textarea id="lyricArea" v-model="lyric"> </b-form-textarea>
          </div>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center mt-3">
        <b-col sm="10">
          <div>
            <p class="h4">Translate</p>
            <b-form-textarea id="translateArea" v-model="translate">
            </b-form-textarea>
          </div>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center mt-3">
        <translateFrame> </translateFrame>
      </b-row>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "lyricsFinder",
  components: {},
  data: function () {
    return {
      artist: "",
      song: "",
      lyric: "",
      translate: "",
    };
  },
  methods: {
    findLyric() {
      axios
        .get("https://api.lyrics.ovh/v1/" + this.artist + "/" + this.song)
        .then((result) => {
          this.lyric = result.data.lyrics;
        });
    },
  },
};
</script>

<style>
</style>