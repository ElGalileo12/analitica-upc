<script setup lang="ts">
import Navbar from "./Navbar/index.vue";

</script>

<template>
  <div class="bg-white font-poppins relative">
    <Navbar />
    <main><router-view /></main>
  </div>
</template>
