import { defineStore } from "pinia";
import { axiosApi } from "@/plugins/axios";

export const useEgresadoStore = defineStore("egresado", {
  state: () => ({
    rqConsult: {},
  }),
  getters: {},
  actions: {
    async EgreconsultaByApi(ID_C_DOCUMENTO) {
      try {
        let { data } = await axiosApi.get(`api/Egresados/${ID_C_DOCUMENTO}/`);
        this.rqConsult = data;
      } catch (error) {
        throw error;
      }
    },
    async EgredeleteByApi(ID_C_DOCUMENTO) {
      try {
        await axiosApi.delete(`api/Egresados/${ID_C_DOCUMENTO}/`);
      } catch (error) {
        throw error;
      }
    },
    async EgreinscriptionaByApi(concatInfo) {
      try {
        var { data } = await axiosApi.post(`api/inscripcion_egresados/`, {
          concatInfo,
        });
        this.rqConsult = data;
      } catch (error) {
        throw error;
      }
    },
    async EgreditionByApi(concatInfo) {
      try {
        //Ya aquí configuras lo que vas a enviar
        console.log(concatInfo);
        try {
          var { data } = await axiosApi.post(`api/change_egresados/`, {
            concatInfo,
          });
          this.rqConsult = data;
        } catch (error) {
          throw error;
        }
      } catch (error) {
        throw error;
      }
    },
  },
});
