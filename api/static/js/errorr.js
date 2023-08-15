document.getElementById('formularioconsulta').addEventListener('submit', async function(event) {
  event.preventDefault();

  try {
      const response = await fetch('http://127.0.0.1:8000/api/consultastd/');
      window.alert('USUARIO NO ENCONTRADO');
      return await response.json();

  } catch (error) {
      console.log('Error en la solicitud:', error);
  }
});

window.addEventListener("load", async () => {
  await initChart();
  
});