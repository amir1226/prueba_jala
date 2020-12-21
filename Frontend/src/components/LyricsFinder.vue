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
        <b-col class="mt-3">
          <p class="h4" v-if="lyric !== ''">
            Song has {{ words }} words and {{ lines }} lines
          </p>
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
      words: 0,
      lines: 0,
    };
  },
  methods: {
    findLyric() {
      let theArtist = this.artist.toLowerCase();
      let theSong = this.song.toLowerCase();
      axios
        .get("https://api.lyrics.ovh/v1/" + theArtist + "/" + theSong)
        .then((result) => {
          this.lyric = result.data.lyrics;
          this.count_words_and_lines();
        });
    },
    count_words_and_lines() {
      let theLyric = this.lyric;
      let send = {
        text: theLyric,
      };
      axios.post("http://127.0.0.1:8000/stats", send).then((result) => {
        this.words = result.data.words;
        this.lines = result.data.lines;
      });
    },
    translateLyric() {
      let theArtist = this.artist.toLowerCase();
      let theSong = this.song.toLowerCase();
      let theLyric = this.lyric;

      let send = {
        artist: theArtist,
        song: theSong,
        foreignLyric: theLyric,
      };

      axios
        .post("http://127.0.0.1:8000/translatelyric", send)
        .then((result) => {
          this.translate = result.data.translate;
        });
    },
  },
};
</script>

<style>
</style>