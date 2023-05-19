<template>
  <!-- <div class="container" style="margin-left: 100px;margin-right:100px">
        <h1 class="justify-content-center" style="margin: 100px">What are your interested careers?</h1>
        <label for="interests">Enter your interested careers:</label>
        <input type="text" id="interests" v-model="userInput" @input="updateRecommendedCareers">
        <select v-model="selectedCareer">
            <option v-for="career in recommendedCareers" :value="career">{{ career }}</option>
        </select>
    </div> -->
  <!-- form -->
  
  <div class="container-fluid vh-100 d-flex">
    <div class="container m-auto">
      <h1 class="justify-content-center text-center">
        What are some careers you are interested in?
      </h1>
      <div class="justify-content-center mt-5">
        <h3>Input careers</h3>
        <input class="form-control form-control-lg" type="text" id="career-input" v-model="careerInput" @keyup.enter="addCareer">
      </div>
      <div class="career-list">
          <div v-for="career in careers" :key="career.id" class="career" :class="{ 'selected': isSelected(career) }" @click="toggleSelected(career)">
            {{ career.name }}
          </div>
        </div>
      <!-- button -->
      <div style="margin-top: 100px" class="d-flex flex-row">
        <!-- <button class="button btn btn-light">Previous</button> -->
        <button class="button btn btn-light ms-auto">Next</button>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "OnboardInterest",
  data() {
    return {
      careers:[
        {id: 1, name: "Web Developer"},
        {id: 2, name: "Graphic Designer"}
      ],
      careerInput: "",
      recommendedCareers: [],
      selectedCareers: [],
    };
  },
  methods: {
    updateRecommendedCareers() {
      // Make an API call or use a local list of careers to get recommended options based on user input
      const matchingCareers = [
        "Web Developer",
        "Graphic Designer",
        "Marketing Manager",
        "Data Analyst",
        "Project Manager",
      ].filter((career) => {
        return career.toLowerCase().includes(this.careerInput.toLowerCase());
      });
      this.recommendedCareers = matchingCareers;
      this.selectedCareer = matchingCareers[0];
    },

    isSelected(career) {
        return this.selectedCareers.includes(career);
      },
      toggleSelected(career) {
        if (this.isSelected(career)) {
          this.selectedCareers = this.selectedSkills.filter(selectedCareer => selectedCareer !== career);
        } else {
          this.selectedCareers.push(career);
        }
      },
      addSkill() {
        if (this.careerInput.trim() !== '') {
          const newCareer = { id: this.careers.length + 1, name: this.careerInput.trim() };
          this.careers.push(newCareer);
          this.selectedCareers.push(newCareer);
          this.careerInput = '';
        }
      }
  },
};
</script>
