import { storeToRefs } from "pinia";
import { useConsultaStore } from "../store/consulta";

export const useConsulta = () => {
  const useConsultaApi = useConsultaStore();

  const { rqConsult } = storeToRefs(useConsultaApi);
  const { consultaByApi, inscriptionaByApi } = useConsultaApi;
  const { deleteByApi } = useConsultaApi;

  return { deleteByApi, consultaByApi, inscriptionaByApi, rqConsult };
};

//EGRESADOS
export const EgreuseConsulta = () => {
  const useConsultaApi = useConsultaStore();

  const { rqConsult } = storeToRefs(useConsultaApi);
  const { EgreconsultaByApi } = useConsultaApi;
  const { EgredeleteByApi } = useConsultaApi;

  return { EgredeleteByApi, EgreconsultaByApi, rqConsult };
};

