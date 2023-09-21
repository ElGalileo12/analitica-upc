<template>
<div class="sectionfour">
      <div class="col-lg-6 mx-5">
        <h1>Contactanos</h1>
        <p class="parrafo_1">Estudiante: Andres Camilo Reyes Galindo</p>
        <p class="parrafo">Correo: acamiloreyes@unicesar.edu.co</p>
      </div>
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
    </div>
</template>
<style>
.sectionfour{
    text-align: center;
    padding-top: 1rem;
    display: flex;
    align-items: center;
    background-color: #306de0;
    height: 30vh;
    padding-right: 150px;
}

.sectionfour li a{
    margin-top: -2rem;
    font-family: "Handlee", cursive;
    font-weight: bold;
    display: block;
    color: #fdfdfd;
    text-transform: none;
    font-size: 18px;
    
}
.sectionfour p{
    font-family: "Handlee", cursive;
    font-weight: bold;
    display: block;
    color: #fdfdfd;
    text-transform: none;
    font-size: 18px;
    padding-top: 10px;
    
}
.sectionfour li a:hover{
    color: #889fca; 
}

.sectionfour h1{
    margin-top: -4rem;
    color: #f7f7f7;
    font-weight: bold;
    font-family: "Handlee", cursive;
    font-size: 40px;

}

.sectionfour h1::before{
    content: "\f0e0"; /* Código Unicode del icono de corazón en Font Awesome */
    font-family: "Font Awesome 5 Free"; /* Nombre de la fuente de Font Awesome */
    margin-top: 11px; /* Añade margen a la derecha del icono para separarlo del texto */
    margin-right: 5px;
}

.sectionfour p.parrafo_1::before{
    content: "\f007"; /* Código Unicode del icono de corazón en Font Awesome */
    font-family: "Font Awesome 5 Free"; /* Nombre de la fuente de Font Awesome */
    margin-top: 11px; /* Añade margen a la derecha del icono para separarlo del texto */
    margin-right: 5px;
    margin-bottom: 0px;
}

.sectionfour p.parrafo::before{
    content: "\e4e8"; /* Código Unicode del icono de corazón en Font Awesome */
    font-family: "Font Awesome 5 Free"; /* Nombre de la fuente de Font Awesome */
    margin-top: 11px; /* Añade margen a la derecha del icono para separarlo del texto */
    margin-right: 5px;
    margin-bottom: 0px;
}


.sectionfour p.parrafo{
    font-family: "Nunito",sans-serif;
    color: #f8f8f8;
    margin-top: -1rem;
    margin-bottom: 0px;

}

.sectionfive{
    color: #ffffff;
    background: #306de0;
    margin-top: -61px;
    margin-bottom: -18px;
}
</style>