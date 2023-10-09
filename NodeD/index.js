const express = require("express");
const app = express();

app.get("/", async (req, res) => {
  const response = await fetch("http://127.0.0.1:5004");
  const data = await response.json();
  res.send(data);
});

app.listen(5001);
