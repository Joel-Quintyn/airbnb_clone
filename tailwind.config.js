/** @type {import('tailwindcss').Config} */
module.exports = {
   content: ["./templates/**/*.{html, css}"],
   theme: {
      extend: {
         spacing: {
            "25vh": "25vh",
            "50vh": "50vh",
            "75vh": "75vh",
         },
         minHeight: {
            "50vh": "50vh",
            "75vh": "75vh",
         },
         borderWidth: { 1.5: "1.5px" },
      },
   },
   plugins: [],
};
