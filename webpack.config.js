var HtmlWebpackPlugin = require('html-webpack-plugin'),
    webpack = require('webpack'),
    pathUtil = require('path');

module.exports = {
  entry: {
    app: ['./js/app.js']
  },
  output: {
    path: __dirname + '/assets/js',
    filename: '[name].min.js'
  },
  resolveLoader: {
    modules: ['closure-loader', pathUtil.resolve(__dirname, 'node_modules')]
  },
  module: {
    rules: [

      {
        test: /google-closure-library\/closure\/goog\/base/,
        use: [
          'imports-loader?this=>{goog:{}}&goog=>this.goog',
          'exports-loader?goog',
        ],
      },
      {
        test: /google-closure-library\/closure\/goog\/.*\.js/,
        loader: 'closure-loader',
        options: {
          paths: [
            pathUtil.resolve(__dirname, 'node_modules/google-closure-library/closure/goog'),
          ],
          es6mode: true,
        },
        exclude: [/google-closure-library\/closure\/goog\/base\.js$/],
      },
      {
        test: /\/js\/.*\.js/,
        loaders: ['closure-loader'],
        exclude: [/node_modules/, /test/],
      },
    ]
  },
  plugins: [
    new webpack.ProvidePlugin({
      goog: 'google-closure-library/closure/goog/base',
    }),
  ],
};
