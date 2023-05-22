<template>
<div class="container m-3 mx-auto">
    <h4>{{user}}</h4>
    <br>

    <div class="row">
        <h2 class="col" >Top Recommended Careers For You </h2>
        <p class="text-secondary"> Number of results: 6 {{}}</p>
    </div>

    <div class="d-flex align-items-center">

        <p class="text-secondary" style="padding-top: 12px"> Filter by: </p>

        <div class="dropdown" style="padding: 5px"> 
            <button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Relevance
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">High to Low</a></li>
                <li><a class="dropdown-item" href="#">Low to High</a></li>
            </ul>
        </div>

        <div class="dropdown" style="padding: 5px">
            <button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Openings
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">High to Low</a></li>
                <li><a class="dropdown-item" href="#">Low to High</a></li>
            </ul>
        </div>

        <div class="dropdown" style="padding: 5px">
            <button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Industry
            </button>
            <ul class="dropdown-menu">
                <!-- use v-for here -->
                <li><a class="dropdown-item" href="#">v-for used here</a></li>
            </ul>
        </div>
    </div>


    <div class="row" style="margin-top: 30px">
        <div class="col-sm-4">
            <div class="card text-center">
            <div class="card-body">
                <h5 class="card-title">UI/UX Designer</h5> 
                <hr>
                <p class="card-text">Estimated Salary: $2000 / month</p>
                <p class="card-text">Relevance: 90% </p>
                <p class="card-text">Number of openings: 90 </p>
                <strong class="card-text">Industry: Technology </strong>
                <br><br>
                <router-link
                    to="/CareerDesc"
                    custom v-slot="{navigate}">
                    <button @click="navigate" role="link" type="button" class="btn btn-primary">View Career ↗</button>
                </router-link>
            </div>
            </div>
        </div>

        <div class="col-sm-4">
            <div class="card text-center">
            <div class="card-body">
                <h5 class="card-title">Web Developer</h5>
                <hr>
                <p class="card-text">Estimated Salary: $2000 / month</p>
                <p class="card-text">Relevance: 90% </p>
                <p class="card-text">Number of openings: 90 </p>
                <strong class="card-text">Industry: Technology </strong>
                <br><br>
                <router-link
                    to="/CareerDesc"
                    custom v-slot="{navigate}">
                    <button @click="navigate" role="link" type="button" class="btn btn-primary">View Career ↗</button>
                </router-link>            
            </div>
            </div>
        </div>

        <div class="col-sm-4">
            <div class="card text-center">
            <div class="card-body">
                <h5 class="card-title">Researcher</h5>
                <hr>
                <p class="card-text">Estimated Salary: $2000 / month</p>
                <p class="card-text">Relevance: 90% </p>
                <p class="card-text">Number of openings: 90 </p>
                <strong class="card-text">Industry: Technology </strong>
                <br><br>
                <router-link
                    to="/CareerDesc"
                    custom v-slot="{navigate}">
                    <button @click="navigate" role="link" type="button" class="btn btn-primary">View Career ↗</button>
                </router-link>            
            </div>
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
  methods:{

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