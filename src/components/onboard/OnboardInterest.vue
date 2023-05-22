<template>
  
  <div class="container-fluid vh-100 d-flex">
    <div class="container m-auto">
      <h1 class="justify-content-center text-center">
        What are some careers you are interested in?
      </h1>
      <div class="justify-content-center mt-5">
        <h3>Input Careers</h3>
        <input class="form-control form-control-lg" type="text" id="career-input" v-model="careerInput" 
        @keyup.enter="addCareer">
      </div>
      <div class="career-list">
        <div v-for="career in careers" :key="career.id" class="career rounded-pill px-3"
          :class="[isSelected(career) ? 'bg-dark text-white' : 'bg-light border-1 text-dark']"
          @click="toggleSelected(career)">
          {{ career.name }}
          <font-awesome-icon v-if="!isSelected(career)" class="ms-2" :icon="['fas', 'plus']" />
        </div>
        </div>
      <!-- button -->
      <div style="margin-top: 100px" class="d-flex flex-row">
        <!-- <button class="button btn btn-light">Previous</button> -->
        <router-link to="/onboard/skill" custom v-slot="{ navigate }">
          <button @click="navigate"  role="link" type="button" class="button btn btn-light ms-auto">Next</button>
        </router-link>
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
        {id: 2, name: "Graphic Designer"},
        {id: 3, name: "Marketing Manager"},
        {id: 4, name: "Data Analyst"},
        {id: 5, name: "Project Manager"}
      ],
      careerInput: "",
      selectedCareers: [],
    };
  },
  methods: {

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
      addCareer() {
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

<style>
.careers {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.careers div {
  flex-basis: calc(33.33% - 10px);
}

.career {
  cursor: pointer;
  border: 1px solid #ccc;
  padding: 5px;
  /* border-radius: 5px; */
}

.career.selected {
  background-color: #252627;
  color: #fff;
}

.career-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}</style>
  
