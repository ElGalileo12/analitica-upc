import { defineStore } from "pinia";
import { axiosApi } from "@/plugins/axios";

export const useStudentStore = defineStore("student", {
  state: () => ({
    rqConsult: {},
  }),
  getters: {},
  actions: {
    async consultaByApi(ID_C_DOCUMENTO) {
      try {
        let { data } = await axiosApi.get(`api/Estudiante/${ID_C_DOCUMENTO}/`);
        this.rqConsult = data;
      } catch (error) {
        throw error;
      }
    },
    async editionByApi(concatInfo) {
      try {
        //Ya aquí configuras lo que vas a enviar
        console.log(concatInfo);
        try {
          var { data } = await axiosApi.post(`api/inscripcion/`, {
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
    async deleteByApi(ID_C_DOCUMENTO) {
      try {
        await axiosApi.delete(`api/Estudiante/${ID_C_DOCUMENTO}/`);
      } catch (error) {
        throw error;
      }
    },
    async inscriptionaByApi(concatInfo) {
      try {
        var { data } = await axiosApi.post(`api/inscripcion/`, {
          concatInfo,
        });
        this.rqConsult = data;
      } catch (error) {
        throw error;
      }
    },
  },
});
