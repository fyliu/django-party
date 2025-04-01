const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:8000",
    env: {
            'username': '',
            'password': ''
        },
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
