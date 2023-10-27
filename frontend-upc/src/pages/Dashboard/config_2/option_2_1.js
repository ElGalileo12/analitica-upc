import { ref } from "vue";
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2_1 = async () => {
  try {
    let { data } = await axiosApi.get(`/api/get_chart_2_1/`);
    return data;
  } catch (ex) {
    console.error(ex);
  }
};

export const config_2_1 = ref({
  
  title: {
    text: "Estrato Socioeconomico",
    right: "25%",
    top: "5%",
  },
  legend: {
    right: "-20%",
    top: "0%",
    orient: "center",
  },
  tooltip: {
    trigger: "item",
    formatter: "{b}: {c} ",
  },
  xAxis: {
    type: "category",
    data: ["Estrato 1", "Estrato 2", "Estrato 3", "Estrato 4", "Estrato 5"],
  },
  yAxis: {
    type: "value",
  },

  series: [
    {
      data: [{ value: 1 }, { value: 1 }],
      type: "bar",
      top: "0%",
      showBackground: "true",
      label: {
        show: 'true',
        position: 'top',
        fontSize: 16
    },
      backgroundStyle: {
        color: "rgba(180, 180, 180, 0.2)",
      },
    },
  ],
});
