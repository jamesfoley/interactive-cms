var gulp = require('gulp'),
    browser_sync = require('browser-sync'),
    sass = require('gulp-sass'),
    auto_prefixer = require('gulp-autoprefixer'),
    size = require('gulp-size'),
    watch = require('gulp-watch');

gulp.task('serve', function(){
  browser_sync({
    proxy: "127.0.0.1:8000",
    notify: false,
    open: false
  });

  watch('./cms/static/manage/scss/**/*.scss', function(){
    gulp.start('styles')
  })

});

gulp.task('styles', function(){
  return gulp.src('./cms/static/manage/scss/**/*.scss')
    .pipe(sass({
      errLogToConsole: true,
      precision: 10,
      sourceComments: true,
      stats: true
    }))
    .on('error', function(e){
      console.log(e);
    })
    .pipe(auto_prefixer())
    .pipe(gulp.dest('./cms/static/manage/css/'))
    .pipe(browser_sync.reload({
      stream: true
    }))
    .pipe(size({
      title: 'styles'
    }));
});

gulp.task('default', ['serve', 'build']);
gulp.task('build', ['styles']);
