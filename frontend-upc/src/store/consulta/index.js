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
        //let { data } = await axiosApi.get(`/api/get_chart/`);
        this.rqConsult = data;
      } catch (error) {
        throw error;
      }
    },
    async inscriptionaByApi(concatInfo) {
      try {
        console.log(concatInfo);
        var { data } = await axiosApi.post(`api/Estudiante/`, {
          concatInfo,
        },
        
        );
        console.log(data);
      } catch (error) {
        throw error;
      }
    },
  },
});
