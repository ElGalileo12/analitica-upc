import { defineStore } from "pinia";
import { axiosApi } from "@/plugins/axios";

export const useConsultaStore = defineStore("payment", {
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
    async deleteByApi(ID_C_DOCUMENTO) {
      try {
        await axiosApi.delete(`api/Estudiante/${ID_C_DOCUMENTO}/`);
      } catch (error) {
        throw error;
      }
    }
  },
});