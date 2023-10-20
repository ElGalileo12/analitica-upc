/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        quattro: "'Quattrocento Sans', sans-serif",
        roboto: "'Roboto', sans-serif",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
