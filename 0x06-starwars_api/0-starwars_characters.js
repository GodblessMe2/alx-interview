#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, _, body) => {
    if (err) console.log(err)
    const charactersURL = JSON.parse(body).characters;
    const charactersByName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if(promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
       });
      })
    );
    Promise.all(charactersByName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
