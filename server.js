const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Serve the index.html file for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/download', async (req, res) => {
  const { url } = req.body;
  // Implement your video download logic here
  // For now, we'll just send a dummy response
  res.send('Video download logic not implemented');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
