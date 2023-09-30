<template>
  <!-- <div class="sectionfour">

      <div class="col-lg-6">
        <ul class="nav justify-content-center">
          <i class="fa-solid fa-house" style="color: #ffffff; margin-top: -21px;"></i>
          <li class="nav-item"><a href="/home" class="nav-link px-2 text-body-secondary">Home</a></li>\
          <i class="fa-solid fa-magnifying-glass" style="color: #ffffff; margin-top: -21px"></i>
          <li class="nav-item"><a href="Home#sectiontwo" class="nav-link px-2 text-body-secondary">Features</a></li>
          <i class="fa-solid fa-building-columns" style="color: #ffffff; margin-top: -21px"> </i>
          <li class="nav-item"><a href="https://www.unicesar.edu.co" class="nav-link px-2 text-body-secondary">University</a></li>
          <i class="fa-solid fa-people-group" style="color: #ffffff;margin-top: -21px;"></i>
          <li class="nav-item"><a href="Home#Quienes" class="nav-link px-2 text-body-secondary">About us</a></li>
        </ul>
      </div>
    </div>
    <div class="sectionfive">
      <p class="text-center text-body-secondary border-top pt-3 my-3">© 2023 Company, Inc</p>
    </div> -->

  <footer class="bg-gray-800">
    <div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
      <div class="md:flex md:justify-between">
        <div class="flex flex-shrink-0 items-center">
          <img src="@/assets/logo.png" width="130" height="130" class="px-4" />
          <router-link to="/" class="text-2xl text-white"
            >Proyecto institucional
          </router-link>
        </div>
        <div class="grid grid-cols-2 gap-8 sm:gap-32 sm:grid-cols-2">
          <div>
            <h2 class="teme mb-3 text-base font-semibold text-white uppercase">
              Contactenos
            </h2>
            <ul class="text-gray-400 font-medium temeTwo">
              <li class="mb-4">
                <h2 class="hover:underline hover:text-white">Andres Camilo Reyes Galindo</h2>
              </li>
              <li class="mb-4">
                <h2 class="hover:underline hover:text-white">acamiloreyes@unicesar.edu.co</h2>
              </li>
              <li>
                <router-link
                  to="https://www.unicesar.edu.co"
                  class="hover:underline hover:text-white"
                >
                  Universidad popular del cesar
                </router-link>
              </li>
            </ul>
          </div>
          <div>
            <h2 class="teme mb-3 text-base font-semibold text-white uppercase">
              Recursos
            </h2>
            <ul class="text-gray-400 font-medium temeTwo">
              <li class="mb-4">
                <router-link to="/inscripcion" class="hover:underline hover:text-white"
                  >Inscripción</router-link
                >
              </li>
              <li class="mb-4">
                <router-link to="/Consulta" class="hover:underline hover:text-white"
                  >Consulta</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
      <hr
        class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8"
      />
      <div class="sm:flex sm:items-center sm:justify-center">
        <span class="text-sm text-gray-400 sm:text-center"
          >© 2023 <a href="#" class="hover:underline"> Copyright 2023</a> -
          Reservados todos los derechos.
        </span>
      </div>
    </div>
  </footer>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap");

.teme {
  font-family: "Roboto", sans-serif;
}
.temeTwo {
  font-family: "Roboto", sans-serif;
  font-weight: 400;
}
</style>
