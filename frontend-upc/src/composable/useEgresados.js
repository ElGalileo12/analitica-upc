import { storeToRefs } from "pinia";
import { useEgresadoStore } from "../store/egresados";

export const useEgresadoConsulta = () => {
  const useConsultaApi = useEgresadoStore();
  const { rqConsult } = storeToRefs(useConsultaApi);
  const { EgredeleteByApi, EgreconsultaByApi, EgreinscriptionaByApi, EgreditionByApi } = useConsultaApi;

  return { EgredeleteByApi, EgreconsultaByApi, EgreinscriptionaByApi, EgreditionByApi, rqConsult };
};
