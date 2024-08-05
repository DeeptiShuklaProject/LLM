// server.js
const express = require('express');
const axios = require('axios');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.use(express.json());

app.post('/run-model', async (req, res) => {
    const { model_name, prompt, max_length } = req.body;

    exec(`python3 llama_mistral.py "${model_name}" "${prompt}" ${max_length}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return res.status(500).send(`Error: ${error.message}`);
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
            return res.status(500).send(`Stderr: ${stderr}`);
        }
        res.send(stdout);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

