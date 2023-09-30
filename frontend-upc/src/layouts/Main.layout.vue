<script setup lang="ts">
import Navbar from "./Navbar/index.vue";
import Footer from "./Footer/Footer.vue";
</script>

<template>
  <div class="min-h-screen flex flex-col overflow-y-auto scrollbar">
    <div class="flex-grow">
      <Navbar />
      <main><router-view /></main>
    </div>
    <Footer />
  </div>
</template>


