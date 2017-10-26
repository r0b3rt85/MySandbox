// Required models
const http = require('http');
const fs = require('fs');

const hostname = 'localhost';
const port = 3000;

// App or Website Setup
fs.readFile('index.html', (err, html) => {
  if(err){
    throw err;
  }

  // Server Setup
  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.write(html);
    res.end();
  });

  // Listener
  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
  });
});
