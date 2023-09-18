import axios from "axios";

let configApi = {
 // baseURL: "https://us-central1-plateidentifier.cloudfunctions.net/api/v1",
  baseURL: "http://127.0.0.1:8000/",
};
/* let configFirebase = {
  baseURL:
    process.env.VUE_APP_FIREBASE_URL +
    "token?key=" +
    process.env.VUE_APP_FIREBASE_API_KEY,
};
 */
const axiosApi = axios.create(configApi);

/* axiosApi.interceptors.request.use(
  function (config) {
    if (Cookies.get("auth")) {
      let cookies = JSON.parse(Cookies.get("auth"));
      config.headers.Authorization = "Bearer " + cookies.idToken;
    }
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
axiosApi.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error) {
    // Do something with response error
    return Promise.reject(error);
  }
); */

export { axiosApi };
