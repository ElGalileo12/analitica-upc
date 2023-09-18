const routes = [
  {
    path: "/",
    component: () => import("../layouts/Main.layout.vue"),
    children: [
      {
        path: "",
        name: "home",
        component: () => import("../pages/Home.view.vue"),
      },
      {
        path: "/consulta",
        name: "consulta",
        component: () => import("../pages/Consulta/Consulta.view.vue"),
      },
      {
        path: "/inscripcion",
        name: "inscripcion",
        component: () => import("../pages/Inscripcion/Inscripcion.view.vue"),
      },
    ],
  },

  {
    path: "/:catchAll(.*)*",
    component: () => import("../pages/ErrorView.vue"),
  },
];

export default routes;
