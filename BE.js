// Back-end Challenge In the JavaScript file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/rest-get-simple and then print to the console the hobbies property in the following format: ITEM1, ITEM2, ...

Example Output
running, painting

// Example Output
running, painting

// template
const https = require('https');

https.get('https://coderbyte.com/api/challenges/json/rest-get-simple', (resp) => {
  
  let data = '';

  // parse json data here...
  
  console.log(resp);

});

// Solution
const https = require('https');

https.get('https://coderbyte.com/api/challenges/json/rest-get-simple', (resp) => {
    
    let data = '';
    
    resp.on('data', (chunk) => {
        data += chunk;
    });
    
    resp.on('end', () => {
        let hobbies = JSON.parse(data).hobbies;
        console.log(hobbies.join(', '));
    });
    
    }).on("error", (err) => {
        console.log("Error: " + err.message);
    });

// Output
running, painting




