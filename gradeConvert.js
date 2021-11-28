const express=require('express');

const cors = require('./cors'); 
const bodyParser = require('body-parser');
const gradeRouter = express.Router();
gradeRouter.use(bodyParser.json());
//Import PythonShell module.
const {PythonShell} =require('python-shell');
 
//Router to handle the incoming request.

gradeRouter
//.options(cors.corsWithOptions, (req, res) => { console.log("Hello");res.sendStatus(200); })
.get("/", (req, res, next)=>{
    //Here are the option object in which arguments can be passed for the python_test.js.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
          /*scriptPath: 'path/to/my/scripts',*/ //If you are having python_test.py script in same folder, then it's optional.
        args: [req.query.cgpa] //An argument which can be accessed in the script using sys.argv[1]
    };
     
 
    PythonShell.run('grade_convertor.py', options, function (err, result){
          if (err) throw err;
          // result is an array consisting of messages collected
          //during execution of script.
          console.log('result: ', result.toString());
          res.send(result)
    });
});
 
//Creates the server on default port 8000 and can be accessed through localhost:8000
module.exports = gradeRouter;