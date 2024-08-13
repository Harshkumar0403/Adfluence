const { defineConfig } = require('@vue/cli-service')

module.exports = {
  configureWebpack: {
    watchOptions: {
      ignored: /node_modules/,
      aggregateTimeout: 300,
      poll: 1000,
    },
  },
  devServer: {
    hot: true,
  },
};