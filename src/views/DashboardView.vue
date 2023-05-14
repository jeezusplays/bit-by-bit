<script setup>
import { RouterView } from "vue-router";
import { RouterLink } from "vue-router";
</script>

<template>
    <div class="d-flex flex-row h-100 p-0 m-0">
        <div class="d-flex flex-column p-0 m-0">
            <div class="collapse show collapse-horizontal h-100" id="sidebar">
                <div class="p-3 h-100 sidebar text-white bg-dark" style="width: fit-content">
                    <div class="d-flex justify-content-center mb-3 align-self-center w-100 text-white text-decoration-none">
                        <span class="py-2 mx-3">
                            <img src="../assets/logos/white_full_logo.png" alt="" style="width: 100px; height: 100px" />
                        </span>
                        <!-- <button class="btn-close btn-close-white ms-3 d-block d-md-none" type="button"
                            data-bs-toggle="collapse" data-bs-target="#sidebar" aria-controls="sidebar" aria-expanded="true"
                            aria-label="Close"></button> -->
                    </div>
                    <div class="d-flex mx-3 my-4 grow">
                        <img :src="profile" class="border-rounded rounded-circle border border-4" alt=""
                            style="width: 56px; height: 56px; object-fit: cover" />
                        <div class="text-start ms-3">
                            <span> {{ name }}</span>
                            <br />
                            <span> {{ email }}</span>
                        </div>
                    </div>
                    <ul class="navbar-nav nav nav-pills flex-column mb-auto">
                        <li class="nav-item w-100 text-start">
                            <RouterLink :to="'/'" class="nav-link text-colour-hover px-3 py-2" aria-current="page">
                                <font-awesome-icon icon="fa-solid fa-house" class="me-3" size="md" />
                                <text class="pp-fat-text">Dashboard</text>
                            </RouterLink>
                        </li>
                        <li class="nav-item w-100 text-start">
                            <RouterLink :to="'/'" class="nav-link text-colour-hover px-3 py-2" aria-current="page">
                                <font-awesome-icon icon="fa-solid fa-map" class="me-3" size="md" />
                                <text class="pp-fat-text">Something 1</text>
                            </RouterLink>
                        </li>
                        <li class="nav-item w-100 text-start">
                            <RouterLink :to="'/'" class="nav-link text-colour-hover px-3 py-2" aria-current="page">
                                <font-awesome-icon icon="fa-solid fa-star" class="me-3" size="md" />
                                <text class="pp-fat-text">Something 2</text>
                            </RouterLink>
                        </li>
                        <li class="nav-item w-100 text-start">
                            <RouterLink :to="'/'" class="nav-link text-colour-hover px-3 py-2" aria-current="page">
                                <font-awesome-icon icon="fa-solid fa-user" class="me-3" size="md" />
                                <text class="pp-fat-text">Profile</text>
                            </RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="d-flex flex-column flex-fill p-0 m-0" id="main-view">
            <div id="main-component">
                <nav class="navbar sticky-top navbar-expand-md px-4 py-3">
                    <div class="container-fluid">
                        <button class="navbar-toggler d-block" type="button" data-bs-toggle="collapse"
                            data-bs-target="#sidebar" aria-controls="sidebar" aria-expanded="true"
                            aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <ul class="navbar-nav justify-content-end ms-auto my-auto">
                            <li class="nav-item ms-auto">
                                <a class="nav-link pp p-0 pointer">Logout</a>
                            </li>
                        </ul>
                    </div>
                </nav>
                <RouterView />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DashboardNav",
    data() {
        return {
            name: localStorage["name"] ? localStorage["name"] : "Gojo Satoru",
            email: localStorage["email"] ? localStorage["email"] : "gojosatoru@gmail.com",
            profile: localStorage["profilepic"] ? localStorage["profilepic"] : '../src/assets/gojo_satoru.png'
        };
    },
    mounted() {

    },
    computed: {

    },
    methods: {

    },
};
</script>
<style lang=""></style>