import { storeToRefs } from "pinia";
import { useConsultaStore } from "../store/consulta";

export const useConsulta = () => {
  const useConsultaApi = useConsultaStore();

  const { rqConsult } = storeToRefs(useConsultaApi);
  const { consultaByApi } = useConsultaApi;

  return { consultaByApi, rqConsult };
};

export const useDeleteConsulta = () => { 
  const useDeleteApi = useConsultaStore();

  const { deleteByApi } = useDeleteApi;

  return { deleteByApi };
};

