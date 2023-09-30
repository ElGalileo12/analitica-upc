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
        path: "/edition",
        name: "edition",
        component: () => import("../pages/Edition/Edition.view.vue"),
      },
      {
        path: "/consulta_egresados",
        name: "consulta_egresados",
        component: () => import("../pages/Consulta/ConsultaEgresado.view.vue"),
      },
      {
        path: "/inscripcion",
        name: "inscripcion",
        component: () => import("../pages/Inscripcion/Inscripcion.view.vue"),
      },
      {
        path: "/dashStu",
        name: "dashboard",
        component: () => import("../pages/Dashboard/dash_1.vue"),
      },
    ],
  },

  {
    path: "/:catchAll(.*)*",
    component: () => import("../pages/ErrorView.vue"),
  },
];

export default routes;
