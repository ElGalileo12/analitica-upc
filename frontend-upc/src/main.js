import { createApp } from "vue";
import { createPinia } from "pinia";
import Flicking from "@egjs/vue3-flicking";
import "./style.css";
import router from "./routes/index";
import App from "./App.vue";
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const app = createApp(App);
const pinia = createPinia();
createApp(App).use(router).use(pinia).use(VueSweetalert2).mount("#app");
