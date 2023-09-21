<template>
<div class="container-fluid">
    <div class="row align-items-center"></div>
            <div class="col-lg-6 text-justify text-lg-left">
              <h1 class="title">Proyecto institucional</h1>
                <p>
                  Este software, desarrollado especialmente para asistir a los investigadores y profesionales de la educación,
                  ofrece una herramienta extraordinariamente eficaz para comprender en profundidad los múltiples factores que
                  contribuyen a la deserción de los estudiantes en el prestigioso programa de Ingeniería Electrónica de la
                  Universidad Popular del César.
                </p>
            </div>
            <div class="col-lg-6 text-center text-lg-right">
                  <img src="../assets/g1.png"  alt="">
            </div>
    </div>

  <!-- Facilities Start -->
    <div class="sectiontwo pb-3" id="sectiontwo">
        <h1></h1>
          <div class="row">
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 32px;">
                      <div class="pl-4">
                          <h4>Compromiso con la Excelencia Educativa </h4>
                          <p class="m-0">Buscamos la mejora constante en la educación.</p>
                      </div>
                  </div>
              </div>
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 30px;">
                      <div class="pl-4">
                          <h4>Accesibilidad y Usabilidad</h4>
                          <p class="m-3">Nuestra interfaz es amigable y fácil de usar.</p>
                      </div>
                  </div>
              </div>
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 34px;">
                      <div class="pl-4">
                        <h4>Análisis de Datos Avanzados </h4>
                        <p class="m-0">Utilizamos técnicas estadísticas y algoritmos sofisticados.</p>
                      </div>
                  </div>
              </div>
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 30px;">
                      <div class="pl-4">
                          <h4>Enfoque Basado en Datos</h4>
                          <p class="m-0">Tomamos decisiones informadas mediante análisis detallados.</p>
                      </div>
                  </div>
              </div>
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 30px;">
                      <div class="pl-4">
                          <h4>Enfoque Multidimensional</h4>
                          <p class="m-0">Analizamos factores diversos que afectan la deserción.</p>
                      </div>
                  </div>
              </div>
              <div class="col-lg-4 col-md-6 pb-1">
                  <div class="d-flex bg-light  border-top rounded mb-4" style="padding: 13px;">
                      <div class="pl-3">
                          <h4>Mejora en la Retención Estudiantil</h4>
                          <p class="m-3">Contribuye a aumentar la retención y el éxito académico de los estudiantes.</p>
                      </div>
                  </div>
              </div>
          </div>
      </div>



  <section class="sectionthree" id="Quienes">
    <div class="recuadro bg-light rounded" id="recuadro" style="height: 500px; margin-left: 30px; margin-right: 30px;">
      <h1 class="text-center">Quienes Somos?</h1>
      <p class="pb-3">
        Somos un grupo de estudiantes apasionados de Ingeniería Electrónica de la Universidad Popular del César, unidos por un propósito común: contribuir de manera significativa en la lucha contra la deserción estudiantil. Con el apoyo invaluable de la Vicerrectoría Académica y el Semillero de Tratamiento de Señales, hemos formado un equipo de 10 estudiantes comprometidos, respaldados por el conocimiento y la experiencia del Ingeniero José Ramón Inglesias y la Ingeniera Omaira Tapia.
        Nuestra misión es utilizar nuestros conocimientos y habilidades en ingeniería para desarrollar un proyecto institucional que aborde de manera efectiva el desafío de la deserción estudiantil. Creemos que la educación es la clave para un futuro mejor, y estamos decididos a hacer nuestra parte para garantizar que cada estudiante tenga la oportunidad de alcanzar su máximo potencial.
        Juntos, estamos trabajando en la implementación de un enfoque innovador y basado en datos para comprender y prevenir la deserción estudiantil en nuestra universidad. A través de análisis de datos avanzados, modelos de pronóstico y estrategias de retención estudiantil, estamos comprometidos en mejorar la calidad de la educación y proporcionar un entorno enriquecedor para todos los que forman parte de nuestra comunidad académica.
        Nuestra visión es ser un faro de cambio en la lucha contra la deserción estudiantil, no solo en nuestra institución, sino también como un ejemplo inspirador para otras instituciones educativas.
      </p>
  </div>
  </section>
</template>

<style>


.container-fluid{
    height: 80vh;
}
.container-fluid, .sectiontwo, .sectionthree{
    width: 100%;
    padding-right: 15px;
    padding-left: 15pxpx;
    margin-right: auto;
    margin-left: auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    color: aliceblue;
    background:  url(../assets/cool-background.jpg) center no-repeat;
    background-attachment: fixed;
    background-size: cover;
}

.container-fluid h1{
    font-family: "Handlee", cursive;
    font-weight: bold;
    font-size: 60px;
    padding-left: 70px;
}
.container-fluid p{
    font-weight: bold;
    padding-left: 50px;
}

.sectiontwo div.d-flex, .sectionthree div.recuadro{
    box-shadow: 0 .125rem .125rem rgba(0,0,0,0.5)!important;
}

.sectiontwo h4{
    color: #306de0;
    font-weight: bold;
    font-family: "Handlee", cursive;
    font-size: 25px;
    text-align: center;
}

.sectiontwo p{
    color: #000000;
    font-size: 15px;
    text-align: center;
}

.sectionthree{
    text-align: justify;
    padding-top: 20px;
    color: rgb(255, 255, 255);
    text-transform: none;
    /**background:  url(img/cool-background.png) center no-repeat;
    background-attachment: fixed;
    background-size: cover;**/
    height: 100vh; 
    }

.sectionthree h1{
    color: #3570df;
    padding-top: 3rem;
    font-family: "Handlee", cursive;
    font-weight: bold;
    font-size: 70px;
    margin-bottom: 0.1rem;
    padding-top: 20px;
}

.sectionthree p{
    color: #000000;
    margin-left: 10rem;
    margin-right: 10rem;
    padding-bottom: 15rem;
}
</style>