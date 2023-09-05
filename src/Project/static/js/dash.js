const getOptionChart = async () => {
  try {

    const response = await fetch("http://127.0.0.1:8000/api/get_chart/"); 
    const response_2 = await fetch("http://127.0.0.1:8000/api/get_chart_2/");
    const response_3 = await fetch("http://127.0.0.1:8000/api/get_chart_3/");
    const response_4 = await fetch("http://127.0.0.1:8000/api/get_chart_4/");
    const response_5 = await fetch("http://127.0.0.1:8000/api/get_chart_5/");   
    const data = await response.json();
    const data_2 = await response_2.json();
    const data_3 = await response_3.json();
    const data_4 = await response_4.json();
    const data_5 = await response_5.json();
    //const chartD = data.chart;
    //const chartD_2 = data.chart_2;

    return { data, data_2,data_3,data_4,data_5  };

  } catch (ex) {
    console.error(ex);
  }
};

const initChart = async () => {
  const myChart = echarts.init(document.getElementById("chart"));
  const myChart_2 = echarts.init(document.getElementById("chart2"));
  const myChart_3 = echarts.init(document.getElementById("chart3"));
  const myChart_4 = echarts.init(document.getElementById("chart4"));
  const myChart_5 = echarts.init(document.getElementById("chart5"));


  const options = await getOptionChart();
    
    myChart.setOption(options.data);   // Configura el primer gráfico
    myChart_2.setOption(options.data_2); // Configura el segundo gráfico
    myChart_3.setOption(options.data_3); // Configura el tercer gráfico
    myChart_4.setOption(options.data_4); // Configura el cuarto gráfico
    myChart_5.setOption(options.data_5); // Configura el cuarto gráfico
 
  
  //myChart_2.setOption(options.chartD_2); // Configura el segundo gráfico
  //myChart.setOption(option);
  //myChart.resize();
};


window.addEventListener("load", async () => {
  
  await initChart();

});