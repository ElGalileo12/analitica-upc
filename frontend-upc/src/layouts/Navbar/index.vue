<template>
  <header>
    <!-- Nav-bar -->
    <nav class="navbar navbar-expand-lg">
      <img src="@/assets/logo.png" width="100" height="100" class="px-4"/>
      <a class="navbar-brand" href="#">Projecto institucional </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      <div class="ex" >
        <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <a class="nav-link" href="/home">Home <span class="sr-only"></span></a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false">
                  Estudiantes
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item" href="/inscripcion">Inscripcion</a>
                  <a class="dropdown-item" href="/consulta">Consulta de datos</a>
                  <a class="dropdown-item" href="/dash">DashBoards</a>
                </div>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false">
                  Egresados
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item" href="/inscripcion">Inscripcion</a>
                  <a class="dropdown-item" href="/consulta">Consulta de datos</a>
                  <a class="dropdown-item" href="/dash">DashBoards</a>
                </div>
              </li>
              <li class="nav-item active">
                <a class="nav-link" href="Home#Quienes">Quienes Somos<span class="sr-only"></span></a>
              </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<style>

*{
    margin: 0; 
    padding: 0;
    border: 0;
    font-size: 100%;
    vertical-align: baseline;
}

body{
    font-family: "Nunito",sans-serif;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
}


.navbar {
    background-color: #1056DC;
    width: 100%;
    z-index: 100;
}
.ex{
    margin-left: 25rem;
}
.navbar-brand {
    margin-left: 1rem;
    color: #ffffff;
    display: flex;
    font-family:"Handlee", cursive;
    font-weight: bold;
}
.navbar-nav.mr-auto li{
    padding-right: 23px;
    padding-left:  20px;
}
.navbar-nav.mr-auto li a{
    font-family: "Handlee", cursive;
    font-weight: bold;
    display: block;
    color: #fdfdfd;
    text-transform: none;
    font-size: 18px;
    
}

.navbar-nav.mr-auto li a:hover{
    color: #889fca; 
}

.dropdown-menu{
    align-items: center;
    background-color: #1056DC;
    width: 100%;
    z-index: 100;
}
.navbar-nav.mr-auto li .dropdown-item{
 text-transform: none;
 color: #ffffff;
}
</style>