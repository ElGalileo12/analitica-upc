import { storeToRefs } from "pinia";
import { useStudentStore } from "../store/consulta";

export const useStudent = () => {
  const useConsultaApi = useStudentStore();
  const { rqConsult } = storeToRefs(useConsultaApi);
  const { deleteByApi, editionByApi, consultaByApi, inscriptionaByApi } =
    useConsultaApi;

  return {
    deleteByApi,
    editionByApi,
    consultaByApi,
    inscriptionaByApi,
    rqConsult,
  };
};
