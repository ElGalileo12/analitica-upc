<script setup lang="ts">
import Navbar from "./Navbar/index.vue";
import Footer from "./Footer/Footer.vue";

</script>

<template>
  <div class="bg-white font-poppins relative">
    <Navbar />
    <main><router-view /></main>
  </div>
  <div></div>
    <Footer/>
</template>
