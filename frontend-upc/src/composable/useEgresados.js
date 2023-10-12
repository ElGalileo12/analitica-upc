import { storeToRefs } from "pinia";
import { useEgresadoStore } from "../store/egresados";

export const useEgresadoConsulta = () => {
  const useConsultaApi = useEgresadoStore();
  const { rqConsult } = storeToRefs(useConsultaApi);
  const { EgredeleteByApi, EgreconsultaByApi } = useConsultaApi;

  return { EgredeleteByApi, EgreconsultaByApi, rqConsult };
};
