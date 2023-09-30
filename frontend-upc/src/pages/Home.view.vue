<script setup>
import homeHeader from "../components/header/home.header.vue";
import defaultCard from "../components/card/default.card.vue";
import otherInfo from "../components/other/info.other.vue";
</script>

<template>
  <div class="container-fluid py-10">
    <homeHeader />
    <defaultCard />
    <otherInfo />
  </div>
</template>

<style>
.container-fluid,
.sectiontwo,
.sectionthree {
  background: url(../assets/cool-background.jpg) center no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
