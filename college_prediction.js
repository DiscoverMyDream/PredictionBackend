const express=require('express');

const satRouter = express.Router();

//Import PythonShell module.
const {PythonShell} =require('python-shell');
const dataset = {
  'California Institute of Technology':'caltechData.csv',
      'Harvard University':'harvardDataset.csv',
      'Washington University in St Louis':'washingtonUniversityData.csv',
      'Duke University':'dukeUniversityData.csv',
      'University of Chicago':'chicagoUniversityData.csv',
      'Stanford University':'stanfordUniversityData.csv',
      'Massachusetts Institute of Technology':'massachussetIntituteData.csv',
      'Yale University':'yaleUniversityData.csv',
      'Princeton University':'princetonUniversityData.csv',
      'Cornell University':'cornellUniversityData.csv',
      'Johns Hopkins University':'johnsHopkinsData.csv',
      'Rice University':'riceUniversityData.csv',
      'Dartmouth College':'dartmouthCollegeData.csv',
      'Vanderbilt University':'vanderbiltUniversityData.csv',
      'Columbia University in the City of New York':'columbiaUniversityData.csv',
      'University of Notre Dame':'notreDameUniversityData.csv',
      'Brown University':'brownUniversityData.csv',
      'University of Pennsylvania':'pennsylvanaUniversityData.csv',
      'Carnegie Mellon University':'carneigeMellonData.csv'
}
//Router to handle the incoming request.


satRouter
//.options(cors.corsWithOptions, (req, res) => { console.log("Hello");res.sendStatus(200); })
.get("/", (req, res, next)=>{
    //Here are the option object in which arguments can be passed for the python_test.js.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
          /*scriptPath: 'path/to/my/scripts',*/ //If you are having python_test.py script in same folder, then it's optional.
        //args: [req.query.dataset,req.query.marks,req.query.gpa] //An argument which can be accessed in the script using sys.argv[1]
        args: [dataset[req.query.clg],req.query.marks,req.query.gpa]
    };
     
 
    PythonShell.run('college_predictor.py', options, function (err, result){
          if (err) throw err;
          // result is an array consisting of messages collected
          //during execution of script.
          console.log('result: ', result.toString());
          res.send(result)
    });
});
 
module.exports= satRouter
//Creates the server on default port 8000 and can be accessed through localhost:8000
