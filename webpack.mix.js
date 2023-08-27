const mix = require('laravel-mix');
require('laravel-mix-modernizr');

mix.options({
    fileLoaderDirs: {
        fonts: 'assets/fonts',
        images: 'assets/images'
    }
});


mix.copyDirectory('./src/public', './assets/public/');


// common files for dashboard and public site
mix.js('./src/common/js/app.js', './assets/common/js/common.js')
    .sass('./src/common/scss/app.scss', './assets/common/css/common.css');


mix.disableNotifications();