<script setup>
import { RouterView } from "vue-router";
import { RouterLink } from "vue-router";
</script>

<template>
    <nav class="navbar sticky-top navbar-expand-md px-4 py-3" id="navbar">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="../assets/logos/white_full_logo.png" width="100" alt="">
            </a>
            <button class="navbar-toggler navbar-dark" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
                aria-controls="offcanvasNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div class="offcanvas-header">
                    <a class="navbar-brand" href="#">
                        <img src="../assets/logos/white_logo.png" width="50" alt="">
                    </a>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <ul class="navbar-nav justify-content-end ms-auto mb-2 mb-lg-0">
                        <li class="nav-item ms-auto" v-if="isNotOnboarding">
                            <a onclick="return false" href="#home" class="nav-link pp px-4">Home</a>
                        </li>
                        <li class="nav-item ms-auto " v-if="isNotOnboarding">
                            <a onclick="return false" href="#profile" class="nav-link pp px-4 ">Profile</a>
                        </li>
                        <li class="nav-item ms-auto" v-if="isNotOnboarding">
                            <a onclick="return false" href="#career" class="nav-link pp px-4 ">Career</a>
                        </li>
                        <li class="nav-item ms-auto" v-if="isNotOnboarding">
                            <a onclick="return false" href="#skills" class="nav-link pp px-4 ">Skills</a>
                        </li>
                        <li class="nav-item ms-auto" v-if="isNotOnboarding">
                            <a onclick="return false" href="#plan" class="nav-link pp px-4 ">Plan</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
    <RouterView />
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {
            currentPage: 'dashboard'
        };
    },
    mounted() {

    },
    computed: {
        isNotOnboarding() {
            return this.currentPage != 'onboarding'
        }

    },
    methods: {

    },
};
</script>
<style lang=""></style>

<style>
.nav-item .nav-link.pp {
  color: #FFFFFF;
  font-weight: 700;
}

.nav-item .nav-link.pp::after {
  content: "";
  width: 0px;
  height: 2px;
  display: block;
  transition: 300ms;
}

.nav-item .nav-link.pp:hover {
  display: inline-block;
  color: #BB0A21;
}

.nav-item .nav-link.pp:hover::after {
  width: 100%;
}

.nav-item.active .nav-link.pp::after {
  width: 100%;
}

.navbar {
  --bs-navbar-toggler-focus-width: 0rem;
  background-color: #252627;

}

#offcanvasNavbar {
    background: #252627;
}

.dropdown-menu.show {
  padding: 0px;
  position: absolute;
  right: 0;
  left: initial !important;
}

.dropdown-menu[data-bs-popper] {
  left: initial;
}

.navbar-collapse.collapse.show ul {
  margin-top: 1rem;
}

.dropdown-item {
  transition: 300ms;
}
</style>
