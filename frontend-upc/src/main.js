import { createApp } from "vue";
import { createPinia } from "pinia";
import Flicking from "@egjs/vue3-flicking";
import "./style.css";
import router from "./routes/index";
import App from "./App.vue";

import "@egjs/vue3-flicking/dist/flicking.css";

const app = createApp(App);
const pinia = createPinia();

app.component("Flicking", Flicking);
createApp(App).use(router).use(pinia).mount("#app");
