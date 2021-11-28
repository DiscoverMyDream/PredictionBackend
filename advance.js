const express=require('express');

var advancedRouter = express.Router();

 
//Import PythonShell module.
const {PythonShell} =require('python-shell');
 
//Router to handle the incoming request.
advancedRouter
.get("/", function(req, res, next){
    //Here are the option object in which arguments can be passed for the python_test.js.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
          /*scriptPath: 'path/to/my/scripts',*/ //If you are having python_test.py script in same folder, then it's optional.
        args: [req.query.marks,req.query.totalMarks,req.query.category] //An argument which can be accessed in the script using sys.argv[1]
    };
     
 
    PythonShell.run('jee_advanced.py', options, function (err, result){
          if (err) throw err;
          // result is an array consisting of messages collected
          //during execution of script.
          console.log('result: ', result.toString());
          res.send(result)
    });
});
 
//Creates the server on default port 8000 and can be accessed through localhost:8000
module.exports = advancedRouter