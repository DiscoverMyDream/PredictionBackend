var createError = require('http-errors');
var express = require('express');
var path = require('path');
var app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
const indexRouter = require('./index')
const mainsRouter = require('./mains')
var advancedRouter = require('./advance')
const satRouter = require('./college_prediction')
const gradeRouter = require('./gradeConvert')

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
  });

app.use('/', indexRouter);
app.use('/mainspredict',mainsRouter)
app.use('/advancepredict',advancedRouter)
app.use('/satpredict',satRouter)
app.use('/gradeConvert',gradeRouter)

app.use(function(req, res, next) {
    next(createError(404));
  });
  
  // error handler
  app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};
  
    // render the error page
    res.status(err.status || 500);
    res.render('error');
  });
  
  const port=8000;
  app.listen(port, ()=>console.log(`Server connected to ${port}`));