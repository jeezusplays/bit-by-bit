<template lang="">
    <div class="container-fluid px-5">
      <br />
      <div class="row">
        <h2 class="text-start">Dashboard</h2>
      </div>
  
      <div class="row m-3">
        <div class="col p-3">
          <h4 class="text-start">Market</h4>
          <p class="sub-text">View the current market data relevant to your career</p>
          <ul id="data_table" class="text-center">
            Insert data table here
          </ul>
        </div>
      </div>

      <hr>
  
      <div class="row m-3">
        <div class="col p-3">
          <h4 class="text-start">Skills in Demand</h4>
          <div class="form-group px-4 mb-3">
            <!-- <span class="fa fa-search form-control-feedback"></span> -->
            <input type="text" class="form-control" placeholder="Search">
          </div>

          <ul id="data_table" class="text-center">
            Insert data table here
          </ul>

          <hr>

          <h6 class="text-center">Top 5 Skills</h6>
          <div class="row">
            <div class="col-sm-6 mb-2">
              <div class="card flex-row">
                <font-awesome-icon icon="fa-computer" class="mx-4" size="xl" />
                <div class="card-body">
                  <p class="card-text"><b>Web Design</b><br>{{courseNumber}} courses available</p>
                </div>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="card flex-row">
                <font-awesome-icon icon="fa-computer" class="mx-4" size="xl" />
                <div class="card-body">
                  <p class="card-text"><b>Web Design</b><br>{{courseNumber}} courses available</p>
                </div>
              </div>
            </div>
          </div>

        </div>
        <div class="col p-3 border rounded">
          <h4 class="text-start">Top Hiring Companies & Industries</h4>
          <ul id="data_table" class="text-center">
            Insert data table here
          </ul>
        </div>
      </div>
    </div>
  </template>
  
<script>
export default {
  name: "dashboard",
  data() {
    return {
      courseNumber: 0,
    };
  },
  mounted() {

  },
  methods: {

  },
};
</script>
<style>
.sub-text {
  color: #737373;
}

.form-control-feedback {
  position: absolute;
  z-index: 2;
  display: block;
  width: 2.375rem;
  height: 2.375rem;
  line-height: 2.375rem;
  text-align: center;
  pointer-events: none;
  color: #aaa;
}

.card {
  flex-direction: row;
  align-items: center;
}

.card img {
  width: 30%;
  border-top-right-radius: 0;
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-title {
  font-weight: bold;
}
</style>
  