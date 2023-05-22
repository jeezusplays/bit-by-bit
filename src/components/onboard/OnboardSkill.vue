<template>
  <div class="container-fluid vh-100 d-flex">
    <div class="container m-auto">
      <h1 class="justify-content-center text-center">
        What are some industry skills you possess?
      </h1>
      <div class="justify-content-center mt-5">
        <h3>Input skills</h3>
        <input class="form-control form-control-lg" type="text" id="skill-input" v-model="skillInput"
          @keyup.enter="addSkill">
      </div>
      <div class="skill-list">
        <div v-for="skill in skills" :key="skill.id" class="skill rounded-pill px-3"
          :class="[isSelected(skill) ? 'bg-dark text-white' : 'bg-light border-1 text-dark']"
          @click="toggleSelected(skill)">
          {{ skill.name }}
          <font-awesome-icon v-if="!isSelected(skill)" class="ms-2" :icon="['fas', 'plus']" />
        </div>
      </div>
      <!-- button -->
      <div style="margin-top: 100px" class="d-flex flex-row">
        <!-- <button class="button btn btn-light">Previous</button>
        <button class="button btn btn-light ms-auto">Next</button> -->
        <router-link to="/onboard/interest" custom v-slot="{ navigate }">
          <button @click="navigate"  role="link" type="button" class="button btn btn-light">Previous</button>
        </router-link>
        <router-link to="/recommendcareers" custom v-slot="{ navigate }">
          <button @click="navigate"  role="link" type="button" class="button btn btn-light ms-auto">Next</button>
        </router-link>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "OnboardSkill",
  data() {
    return {
      skills: [
        { id: 1, name: 'Programming' },
        { id: 2, name: 'Graphic Design' },
        { id: 3, name: 'Project Management' },
        { id: 4, name: 'Communication' },
        { id: 5, name: 'Data Analysis' }
      ],
      selectedSkills: [],
      skillInput: ''
    }
  },
  methods: {

    isSelected(skill) {
      return this.selectedSkills.includes(skill);
    },
    toggleSelected(skill) {
      if (this.isSelected(skill)) {
        this.selectedSkills = this.selectedSkills.filter(selectedSkill => selectedSkill !== skill);
      } else {
        this.selectedSkills.push(skill);
      }
    },
    addSkill() {
      if (this.skillInput.trim() !== '') {
        const newSkill = { id: this.skills.length + 1, name: this.skillInput.trim() };
        this.skills.unshift(newSkill);
        this.selectedSkills.unshift(newSkill);
        this.skillInput = '';
      }
    }
  }
};
</script>
  
<style>
.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.skills div {
  flex-basis: calc(33.33% - 10px);
}

.skill {
  cursor: pointer;
  border: 1px solid #ccc;
  padding: 5px;
  /* border-radius: 5px; */
}

.skill.selected {
  background-color: #252627;
  color: #fff;
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}</style>
  