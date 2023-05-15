<template>
<div class="container m-3 mx-auto">
    <h4>{{user}}</h4>
    <!-- Replace the above in script tag below -->
    <div class="row" style="text-align:center">
        <h5 class="col" style="text-align: right;">Top courses for </h5><h5 class="text-primary col" style="text-align: left;">{{ search_term }}</h5>
        <p class="text-secondary">{{ items.length }} courses available</p>
    </div>

</div>
  <div class="container h-100">
    <div class="row align-items-center h-100">
      <div v-for="item in items" :key="item.id" class="card rounded col-md-4 col-sm-6 border-0 p-3">
        <img class="card-img-top rounded" :src="item.image_480x270" alt="Card image cap">
        <div class="overlay-body glass-morphic-overlay">
            <p class="card-text m-2">{{item.visible_instructors[0].title}}</p>
        </div>
        <div class="card-body">
            <p class="h5 card-title">{{ item.title }}</p>
            <p class="card-text">{{ item.price }}</p>
            <p class="card-text description">{{ item.headline }}</p>
            <!-- <span> -->
                <a :href="`http://www.udemy.com${item.url}`" target="_blank" class="btn btn-primary rounded-5">View course ↗</a>
            <!-- </span> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sampleResponse from './sample_response.json'

export default {
  name: "AppHome",
  data() {
    return {
      items: [],
      search_term: 'Web Design',
      user: "Samuel Chung"
    }
  },
  mounted() {
    this.items = sampleResponse.results;
}

}
</script>

<style>
    .description {
    height: 5em; /* set the maximum height to 400px */
    line-height:1.2em;
    overflow: hidden;
    text-overflow: ellipsis; /* hide any content that exceeds the maximum height */
    /* white-space: nowrap; */
    }
    .card-title {
    height: 2.4em; /* set the maximum height to 400px */
    line-height: 1.2em; 
    overflow: hidden;
    text-overflow: ellipsis; /* hide any content that exceeds the maximum height */
    white-space: nowrap;
    }

    .glass-morphic-image {
    position: relative;
    }

    .glass-morphic-image img {
    display: block;
    width: 100%;
    height: auto;
    }

    .glass-morphic-overlay {
    color:white;
    border-color: antiquewhite;
    border-radius: 10px;
    height:3.5em;
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    z-index: 1;
    transform: translateY(-50%);
    }

    .overlay-body {
    position: relative;
    z-index: 2;
    margin-top: -30px;
    }

</style>