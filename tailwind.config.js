/** @type {import('tailwindcss').Config} */
module.exports = {
   content: ["./templates/**/*.{html, css}"],
   theme: {
      extend: {
         spacing: {
            "25vh": "25vh",
            "50vh": "50vh",
            "60vh": "60vh",
            "75vh": "75vh",
         },
      },
   },
   plugins: [],
};
