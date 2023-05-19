<template>
    <div class="plan d-flex flex-column container m-3 mx-auto">
        <div class="d-flex flex-column flex-sm-row mt-4">
            <h3 class="flex-col flex-shrink-1">Learning Journeys</h3>
            <div class="dropdown flex-col d-flex align-items-center ms-3">
                <button class="btn btn-secondary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown"
                    aria-expanded="false">
                    Dropdown button
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
            </div>
            <button type="button" class="btn btn-primary flex-col ms-auto shadow">Get a mentor</button>
        </div>
        <br>

        <div class="row flex-shrink-1 flex-sm-grow-1 g-3">
            <div class="col col-12 col-sm-4 d-flex">
                <div class="container-fluid border rounded px-4 pt-1">
                    <h4 class="mt-2">Skills</h4>
                    <div class="btn-group-vertical mb-2 w-100" role="group" aria-label="Vertical radio toggle button group">
                        <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio1" autocomplete="off" checked>
                        <label class="btn btn-outline-secondary rounded mt-2 " for="vbtn-radio1">Skill 1</label>

                        <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio2" autocomplete="off">
                        <label class="btn btn-outline-secondary rounded mt-2 " for="vbtn-radio2">Skill 2</label>

                        <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio3" autocomplete="off">
                        <label class="btn btn-outline-secondary rounded mt-2 " for="vbtn-radio3">Skill 3</label>
                    </div>
                </div>
            </div>
            <div class="col col-12 col-sm-8 d-flex">
                <div class="container-fluid border rounded px-4 pt-1">
                    <div class="d-flex flex-sm-row mt-2">
                        <h3 class="flex-col flex-shrink-1">Courses (20)</h3>
                        <div class="dropdown flex-col ms-3 d-flex align-items-center">
                            <button class="btn btn-secondary dropdown-toggle btn-sm" type="button"
                                data-bs-toggle="dropdown" aria-expanded="true"> Dropdown button
                            </button>
                            <ul class="dropdown-menu" data-popper-placement="bottom-start"
                                style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(0px, 32.8px, 0px);">
                                <li><a class="dropdown-item" href="#">Action</a></li>
                                <li><a class="dropdown-item" href="#">Another
                                        action</a></li>
                                <li><a class="dropdown-item" href="#">Something else
                                        here</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 mt-2 mb-3 g-3">
                        <div class="col">
                            <div class="overflow-hidden border rounded">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png" class="card-img-top img-fluid" alt="...">
                                <div class="card-body p-3">
                                  <h5>Card title</h5>
                                  <p class="card-text text-secondary">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                  <a href="#" class="btn btn-primary">Go somewhere</a>
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="overflow-hidden border rounded">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png" class="card-img-top img-fluid" alt="...">
                                <div class="card-body p-3">
                                  <h5>Card title</h5>
                                  <p class="card-text text-secondary">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                  <a href="#" class="btn btn-primary">Go somewhere</a>
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="overflow-hidden border rounded">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png" class="card-img-top img-fluid" alt="...">
                                <div class="card-body p-3">
                                  <h5>Card title</h5>
                                  <p class="card-text text-secondary">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                  <a href="#" class="btn btn-primary">Go somewhere</a>
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="overflow-hidden border rounded">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png" class="card-img-top img-fluid" alt="...">
                                <div class="card-body p-3">
                                  <h5>Card title</h5>
                                  <p class="card-text text-secondary">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                  <a href="#" class="btn btn-primary">Go somewhere</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: "PlanLJ",
    data() {
        return {
            learning_journeys: [{
                job: 'Software Engineer',
                skills: [
                    {
                        name: 'OOAD',
                        courses: [{
                            name: "course 1",
                            progress: "In-progress"
                        }]
                    },
                    {
                        name: 'Frontend',
                        courses: [{
                            name: "course 2",
                            progress: "Completed"
                        }]
                    },
                    {
                        name: 'Backend',
                        courses: [{
                            name: "course 3",
                            progress: "None"
                        }]
                    },

                ]
            }],
            user: "Samuel Chung"
        }
    },
    methods: {

    }
}
</script>

<style scoped>
.plan {
    min-height: 80vh;
}
</style>