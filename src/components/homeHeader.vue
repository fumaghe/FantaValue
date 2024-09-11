<script>
export default {
    data() {
        return {
            navbarItems: [
                {
                    name: 'Home',
                    url: '/',
                    selected: true
                },
                {
                    name: 'Listone',
                    url: '/listone',
                    selected: false
                },
                {
                    name: 'Asta',
                    url: '/asta',
                    selected: false
                },
                {
                    name: 'MyTeams',
                    url: '/myteams',
                    selected: false
                }
            ],
            isOffCanvasOpen: false
        }
    },
    methods: {
        toggleOffCanvas() {
            this.isOffCanvasOpen = !this.isOffCanvasOpen;
        },
        selectItem(selectedItem) {
            this.navbarItems.forEach(item => {
                item.selected = false
            })

            selectedItem.selected = true
        }
    }
}
</script>

<template>
    <div class="container border-bottom">
        <div class="row h-100">
            <div class="col-100 d-flex justify-content-between align-items-center p-10">
                <h1 class="title fs-40">Fanta<span class="text-orange">Value</span></h1>
                <img src="../assets/Logo.png" alt="logo" class="logo">
                <div class="navbar-items d-flex align-items-center">
                    <!-- Navbar Links -->
                    <ul class="d-flex list-unstyled navbar-list">
                        <li v-for="(item, index) in navbarItems" :key="index">
                            <router-link :to="item.url" class="fs-s" :class="{'text-orange': item.selected, 'label-orange': item.name === 'Login'}" @click.native="selectItem(item)">{{ item.name }}</router-link>
                        </li>
                    </ul>
                    <!-- Burger Menu Icon -->
                    <button class="menu-icon" @click="toggleOffCanvas()">
                        <i class="fa-solid fa-bars"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
    <!-- Off-canvas menu -->
    <div :class="{'offcanvas-open': isOffCanvasOpen}" class="offcanvas">
        <div class="offcanvas-content">
            <button class="close-btn" @click="toggleOffCanvas">&times;</button>
            <ul class="list-unstyled">
                <li v-for="(item, index) in navbarItems" :key="index">
                    <router-link :to="item.url" @click.native="toggleOffCanvas" :class="{'text-orange': item.active}">{{ item.name }}</router-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.container {
    position: fixed;
    z-index: 1000;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    height: 100px;
    background-color: white;
}

.h-100 {
    height: 100%;
}

/* Styles for the navbar links */
.list-unstyled a {
    text-decoration: none;
    color: black;
    margin: 0px 10px;
    font-weight: 700;
}

/* Style for the Login button */
.label-orange {
    color: white !important;
    background-color: #FE4C10;
    border-radius: 10px;
    padding: 5px 10px;
}

.logo {
    width: auto;
    height: 100px;
    display: none;
}

/* Default state: hide the menu icon and show navbar links */
.menu-icon {
    display: none;
}


/* Media query: when screen width is less than 768px */
@media (max-width: 768px) {
    .border-bottom {
        border: 0;
    }
    /* Hide the navbar links */
    .navbar-list {
        display: none;
    }
    
    /* Show the menu icon */
    .menu-icon {
        display: block;
        background: none;
        border: none;
        font-size: 24px;
        cursor: pointer;
    }

    .logo {
        display: block;
    }

    .title {
        display: none;
    }
}

/* Off-canvas styles */
.offcanvas {
    position: fixed;
    top: 0;
    right: -100%;
    width: 250px;
    height: 100%;
    background-color: #333;
    color: white;
    z-index: 10000;
    transition: right 0.3s ease-in-out;
    padding: 20px;
}

.offcanvas-open {
    right: 0;
}

.offcanvas-content li {
    margin: 20px 0;
}

.offcanvas-content a {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

/* Close button inside the off-canvas */
.close-btn {
    font-size: 30px;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    margin-bottom: 20px;
}

@media (min-width: 768px) {
    .container {
        height: 60px;
    }
}
</style>
