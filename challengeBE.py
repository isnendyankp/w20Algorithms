# In the JavaScript file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/rest-get-simple and then print to the console the hobbies property in the following format: ITEM1, ITEM2, ...

# Example Output
# running, painting

# Template
const https = require('https');

https.get('https://coderbyte.com/api/challenges/json/rest-get-simple', (resp) => {
  
  let data = '';

#   // parse json data here...
  
  console.log(resp);

});

#  Solution
const https = require('https');

https.get('https://coderbyte.com/api/challenges/json/rest-get-simple', (resp) => {

    let data = '';

    # // parse json data here...
    resp.on('data', (chunk) => {
        data += chunk;
    });

    resp.on('end', () => {
        let jsonData = JSON.parse(data);
        console.log(jsonData.hobbies.join(', '));
    });

});
