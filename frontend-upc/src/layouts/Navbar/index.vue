<script setup>
import { ref } from "vue";

var dropdown = ref(0);
</script>
<template>
  <header>
    <nav class="bg-white border-gray-200">
      <div class="flex flex-wrap justify-between items-center mx-auto">
        <router-link to="/" class="flex items-center">
          <img src="@/assets/Nuevo-logo.jpg" class="w-2/5"
        /></router-link>

        <div class="flex items-center lg:order-2">
          <router-link
            to="/consulta"
            href="#"
            class="bg-green-700 hover:font-bold hover:text-black hover:scale-110 mr-20 text-white focus:ring-4 font-medium rounded-lg text-base px-5 py-2.5 focus:outline-none transition-transform duration-300 ease-in-out"
            >Consulta
          </router-link>
          <button
            data-collapse-toggle="mobile-menu-2"
            type="button"
            class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200"
            aria-controls="mobile-menu-2"
            aria-expanded="false"
            @click="dropdown = !dropdown"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="w-6 h-6"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <svg
              class="hidden w-6 h-6"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>

          <div
            v-if="dropdown"
            class="mr-6 absolute mt-48 w-52 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none transition ease-out duration-100"
            role="menu"
            aria-orientation="vertical"
            aria-labelledby="user-menu-button"
            tabindex="-1"
          >
            <router-link
              id="user-menu-item-0"
              role="menuitem"
              tabindex="-1"
              to="/consulta"
              class="relative text-lg block px-4 py-2 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-red-700 lg:p-0"
              >Consultas</router-link
            >
            <router-link
              id="user-menu-item-0"
              role="menuitem"
              tabindex="-1"
              to="/inscripcion"
              class="relative text-lg block px-4 py-2 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-red-700 lg:p-0"
              >Inscripcion</router-link
            >
            <router-link
              id="user-menu-item-1"
              role="menuitem"
              tabindex="-1"
              to="/search"
              class="relative text-lg block px-4 py-2 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-red-700 lg:p-0"
              >Busqueda</router-link
            >
            <router-link
              id="user-menu-item-0"
              role="menuitem"
              tabindex="-1"
              to="/faq"
              class="relative text-lg block px-4 py-2 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-red-700 lg:p-0"
            >
              Preguntas frecuentes</router-link
            >
          </div>
        </div>
        <div
          class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
          id="mobile-menu-2"
        >
          <ul
            class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0"
          >
            <li>
              <router-link
                to="/consulta"
                class="text-xl font-bold block py-2 pr-4 pl-3 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-green-700 lg:p-0"
                >Home</router-link
              >
            </li>
            <li>
              <router-link
                to="/search"
                class="text-xl font-bold block py-2 pr-4 pl-3 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-green-700 lg:p-0"
                >Egresados</router-link
              >
            </li>
            <li>
              <router-link
                to="/inscripcion"
                class="text-xl font-bold block py-2 pr-4 pl-3 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-green-700 lg:p-0"
                >Inscription</router-link
              >
            </li>
            <li>
              <router-link
                to="/dash"
                class="text-xl font-bold block py-2 pr-4 pl-3 text-black border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-green-700 lg:p-0"
              >Dashboards</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>
