/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        quattro: "'Quattrocento Sans', sans-serif",
        roboto: "'Roboto', sans-serif",
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),
    require("tw-elements/dist/plugin"),
    require("@tailwindcss/forms"),
  ],
};
