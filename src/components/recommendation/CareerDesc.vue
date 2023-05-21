<template>
<div class="container m-3 mx-auto">
    <h4 class= "text-primary">{{user}}</h4>
    <br>

    <div class="row">
        <h2 class="col-md-9" style="padding-bottom: 30px">About Being A Web Developer</h2>
        <div class="col-md-3">
            <div class="d-flex justify-content-end">
                <router-link
                    to="/Plan"
                    custom v-slot="{navigate}">
                        <button @click="navigate" role="link" type="button" class="btn btn-primary btn-lg">Become a Web Developer</button>
                </router-link>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-md-6 mx-auto">
            <h5 class="text-justify text-primary"> Job description </h5>
            <p class="text-justify" style="padding-bottom: 30px"> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam quod expedita doloribus magni veritatis tempore suscipit porro, quidem consequatur exercitationem neque a nulla fugiat error dignissimos adipisci voluptates? Odit, commodi. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam quod expedita doloribus magni veritatis tempore suscipit porro, quidem consequatur exercitationem neque a nulla fugiat error dignissimos adipisci voluptates? Odit, commodi </p>

            <h5 class="text-justify text-primary"> Qualifications </h5>
            <p class="text-justify">
                <ul style="padding-bottom: 30px">
                    <li>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</li> 
                    <li>Aperiam quod expedita doloribus magni veritatis tempore suscipit porro</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</li>
                    <li>Aperiam quod expedita doloribus magni veritatis tempore suscipit porro</li> 
                    
                </ul>
            </p>

        </div>

        <div class="col-md-1 mx-auto"></div>

        <div class="col-md-5">
            <h5 class="text-justify text-primary"> Industry: </h5> Technology <br>
            <h5 class="text-justify text-primary"> Relevance to you: </h5> 98% <br>
            <h5 class="text-justify text-primary"> Average Salary: </h5> $4000 / month <br>
            <h5 class="text-justify text-primary"> Number of openings: </h5> 97 Openings <br>
            <h5 class="text-justify text-primary"> Top hiring companies: </h5> 
                <ul>
                    <li> Apple </li>
                    <li> Samsung </li>
                    <li> Microsoft </li>
                    <li> Google </li>
                </ul>
        </div>
    </div>


    <div class="row">
        <h5 class="text-justify text-primary"> Top Skills for Web Developer </h5>
            <div class="col-md-6 mx-auto">
            <!-- Use v-for for the first 4 skill items  -->
                <div class="alert alert-primary" role="alert">
                    <strong> Web Design </strong> <br>
                    32 Courses Available
                </div>
                <div class="alert alert-warning" role="alert">
                    <strong> Python </strong> <br>
                    30 Courses Available
                </div>
                <div class="alert alert-success" role="alert">
                    <strong> PHP </strong> <br>
                    50 Courses Available       
                </div>
                <div class="alert alert-danger" role="alert">
                    <strong> Javascript </strong> <br>
                    10 Courses Available
                </div>
            </div>


        <div class="col-md-6 mx-auto">
            <!-- Use v-for for the next 4 skill items  -->
            <div class="alert alert-primary" role="alert">
                <strong> Creativity </strong> <br>
                1 Course Available
            </div>
            <div class="alert alert-warning" role="alert">
                <strong> CSS </strong> <br>
                    20 Courses Available
            </div>
            <div class="alert alert-success" role="alert">
                <strong> HTML </strong> <br>
                    22 Courses Available     
            </div>
            <div class="alert alert-danger" role="alert">
                <strong> Problem-Solving </strong> <br>
                    1 Course Available
            </div>
        </div>

        <!-- This pagination is for when there are more than 8 skills, users can scroll to see-->
        <div class="d-flex justify-content-center">
            <ul class="pagination" >
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                <a class="page-link" href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
                </li>
            </ul>
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
    .col-md-6 {
    box-sizing: border-box;
    }
    .text-justify{
        text-align: justify;
        display: inline-block
    }

    .boxy {
        margin-left: 10px;
    }
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