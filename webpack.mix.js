const mix = require('laravel-mix');
require('laravel-mix-modernizr');

mix.options({
    fileLoaderDirs: {
        fonts: 'assets/fonts',
        images: 'assets/images'
    }
});


mix.copyDirectory('./src/public', './assets/public/')




mix.disableNotifications();