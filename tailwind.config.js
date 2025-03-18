/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './party/templates/party/**/*.html',
    './party/static/party/js/**/*.js',
    './party/static/party/src/**/*.css',
  ],
  theme: {
    fontFamily: {
      sans: ["Roboto"] // setting the default font-family
    },
    extend: {
      fontFamily: {
        "roboto": ["Roboto", "sans-serif"], // making possible to use classes font-roboto and font-dancing-script
        "dancing-script": ["Dancing Script", "cursive"],
      },
    },
  },
  plugins: [],
}
