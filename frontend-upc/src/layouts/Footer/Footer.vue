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

  <footer class="bg-green-700">
    <div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
      <div class="md:flex md:justify-between">
        <div class="flex flex-shrink-0 items-center">
          <img src="@/assets/logocarre.png" width="250" height="250" class="px-4" />
          <img src="@/assets/logoacre.png" width="150" height="150" class="px-4" />
        </div>
        <div class="grid grid-cols-2 gap-8 sm:gap-16 sm:grid-cols-2">
          <div>
            <h2 class="teme mb-3 text-base font-semibold text-white uppercase">
              Contactenos
            </h2>
            <ul class="text-white-400 font-medium temeTwo">
              <li class="icon mb-2">
                <i class="fa-solid fa-users mr-2" style="color: #ffffff;"></i>
                <h2> Semillero TRIAC</h2>
              </li>
              <li class="icon mb-2">
                <i class="fa-solid fa-envelope mr-3" style="color: #ffffff;"></i>
                <h2>   acamiloreyes@unicesar.edu.co</h2>
              </li>
              <li class="icon mb-2">
                <i class="fa-solid fa-bolt mr-3" style="color: #ffffff;"></i>
                <h2> Ing. Electronica - Acreditada por alta calidad</h2>
              </li>
              <li class="icon mb-2">
                <i class="fa-solid fa-city mr-2" style="color: #ffffff;"></i>
                <h2>Valledupar - Cesar</h2>
              </li>
              <li>
                <i class="fa-solid fa-envelope mr-2" style="color: #ffffff;"></i>
                <router-link
                  to="https://www.unicesar.edu.co"
                  class="hover:underline hover:text-white"
                >
                   Universidad popular del cesar
                </router-link>
              </li>
            </ul>
          </div>
          <div class="ml-20">
            <h2 class="teme mb-3 text-base font-semibold text-white uppercase">
              Recursos
            </h2>
            <ul class="text-gray-950 font-medium temeTwo">
              <li class="mb-4">
                <i class="fa-solid fa-pen mr-2" style="color: #ffffff;"></i>
                <router-link to="/inscripcion" class="hover:underline hover:text-white"
                  >Inscripción</router-link
                >
              </li>
              <li class="mb-4">
                <i class="fa-solid fa-magnifying-glass mr-2" style="color: #ffffff;"></i>
                <router-link to="/Consulta" class="hover:underline hover:text-white"
                  >Consulta</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
      <hr
        class="my-6 border-gray-950 sm:mx-auto dark:border-gray-950 lg:my-8"
      />
      <div class="sm:flex sm:items-center sm:justify-center">
        <span class="text-sm text-gray-950 sm:text-center"
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
  font-weight: 300;
}

.icon.mb-2 {
  display: flex;
  align-items: center;
  margin-bottom: 2px; /* Ajusta el valor según tus necesidades */
}

</style>
