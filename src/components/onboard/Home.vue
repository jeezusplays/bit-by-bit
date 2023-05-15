<template>
    <div class="container" style="margin-left: 100px;margin-right:100px">
        <h1 class="justify-content-center" style="margin: 100px">What are your interested careers?</h1>
        <label for="interests">Enter your interested careers:</label>
        <input type="text" id="interests" v-model="userInput" @input="updateRecommendedCareers">
        <select v-model="selectedCareer">
            <option v-for="career in recommendedCareers" :value="career">{{ career }}</option>
        </select>
    </div>
    <div>
        hello
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userInput: "",
        recommendedCareers: [],
        selectedCareer: ""
      };
    },
    methods: {
      updateRecommendedCareers() {
        // Make an API call or use a local list of careers to get recommended options based on user input
        const matchingCareers = ["Web Developer", "Graphic Designer", "Marketing Manager", "Data Analyst", "Project Manager"].filter(career => {
          return career.toLowerCase().includes(this.userInput.toLowerCase());
        });
        this.recommendedCareers = matchingCareers;
        this.selectedCareer = matchingCareers[0];
      }
    }
  };
  </script>
  