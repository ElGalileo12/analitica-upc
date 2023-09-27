import { storeToRefs } from "pinia";
import { useConsultaStore } from "../store/consulta";

export const useConsulta = () => {
  const useConsultaApi = useConsultaStore(); //Se crea una instancia

  const { rqConsult } = storeToRefs(useConsultaApi); //Se usa para acceder a getters y state
  const { consultaByApi, inscriptionaByApi } = useConsultaApi; // Se usa para acceder a los actions

  return { consultaByApi, inscriptionaByApi, rqConsult }; //se retorna para poder usarlos de manera global en el proyecto
};
