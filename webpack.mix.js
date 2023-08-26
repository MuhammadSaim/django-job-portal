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
mix.js('./src/common/js/app.js', './assets/common/common.js');


mix.disableNotifications();