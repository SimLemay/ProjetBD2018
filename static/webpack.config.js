const webpack = require('webpack');

const config = {
    entry: __dirname + '/js/index.js',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.css'],
        alias: {
            jquery: "jquery/src/jquery"
        }
    },
    module: {

        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: './[name].[ext]',
                        outputPath: 'fonts/',    // where the fonts will go
                        publicPath: '../static/dist/fonts/'     // override the default path
                    }
                }]
            }
        ]
    }
};

module.exports = config;

