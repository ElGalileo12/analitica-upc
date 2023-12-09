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
        path: "/edition_egresados",
        name: "edition_egresados",
        component: () => import("../pages/Edition/Edition_egre.vue"),
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
        path: "/inscripcion_egresados",
        name: "inscripcion_egresados",
        component: () => import("../pages/Inscripcion/Inscripcion_egre.view.vue"),
      },
      {
        path: "/dashStu",
        name: "dashboard",
        component: () => import("../pages/Dashboard/dash_1.vue"),
      },
      {
        path: "/dashGra",
        name: "dashboardGra",
        component: () => import("../pages/Dashboard/dash_2.vue"),
      },
      {
        path: "/dashPre",
        name: "dashboardPre",
        component: () => import("../pages/Dashboard/dash_3.vue"),
      },
    ],
  },

  {
    path: "/:catchAll(.*)*",
    component: () => import("../pages/ErrorView.vue"),
  },

];

export default routes;
