<template>
<div class="container m-3 mx-auto">
    <h4>{{user}}</h4>
    <br>
    <!-- Replace the above in script tag below -->
    <div class="row" style="text-align:center">
        <h5 class="col" style="text-align: right;">Top courses for </h5><h5 class="text-primary col" style="text-align: left;">{{ search_term }}</h5>
        <p class="text-secondary">{{ items.length }} courses available</p>
    </div>

</div>
  <div class="container h-100">
    <div class="row align-items-center h-100">
      <div v-for="item in items" :key="item.id" class="card col-md-4 col-sm-6 rounded border-0 p-3">
        <img class="card-img-top rounded-4" :src="item.image_480x270" alt="Card image cap">
        <div class="overlay-body glass-morphic-overlay">
            <div class="row">
            <p class="col-8 h6 card-text text-truncate p-3 mx-2">{{item.visible_instructors[0].title}}</p>
            <p style="font-style: italic;" class="card-text font-weight-light text-light col-3 p-3">{{ item.price }}</p>
            </div>
        </div>
        <div class="card-body">
            <p class="h5 card-title">{{ item.title }}</p>
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
    if (sessionStorage.getItem('clientId') != null || sessionStorage.getItem('clientSecret') != null) {
      this.getAPIResponse();
    } else {
      this.items = sampleResponse.results;
      console.warn("The API credentials are not set in session or environment variables. Using sample response instead.")
    }

},methods:{
    getUdemyCourses(){// Get the client ID and secret from session variables
        const clientId = sessionStorage.getItem('clientId');
        const clientSecret = sessionStorage.getItem('clientSecret');
        const api_endpoint = `https://udemy.com/api-2.0/courses/?search=${this.search_term}`

        // Encode the client ID and secret in base64
        const base64Auth = window.btoa(clientId + ':' + clientSecret);

        // Set up the request headers
        const headers = {
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Basic ' + base64Auth,
            'Content-Type': 'application/json'
        };

        // Set up the request options
        const options = {
            method: 'GET',
            headers: headers
        };

        // Send the request to the API endpoint
        fetch(api_endpoint, options)
        .then(response => response.json())
        .then(data => {
            this.items = data.results;
        })
        .catch(error => {
            console.error(error);
        });
        }
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

    /* Glassmorphism settings */
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
    border-width: medium;
    border-radius: 10px;
    height:3.7em;
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(240, 240, 240, 0.3);
    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);
    z-index: 1;
    transform: translateY(-50%);
    }

    .overlay-body {
    position: relative;
    z-index: 2;
    margin-top: -30px;
    }

</style>