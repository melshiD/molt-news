#!/usr/bin/env node

const http = require('http');
const https = require('https');
const url = require('url');

const OPENAI_API_KEY = process.env.OPENAI_API_KEY || '';
const PORT = 8766;

function callOpenAI(prompt, count = 4) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: "dall-e-3",
            prompt: prompt,
            n: 1,  // DALL-E 3 only supports n=1
            size: "1792x1024",
            quality: "standard"
        });

        const options = {
            hostname: 'api.openai.com',
            port: 443,
            path: '/v1/images/generations',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Length': data.length
            }
        };

        const req = https.request(options, (res) => {
            let responseData = '';

            res.on('data', (chunk) => {
                responseData += chunk;
            });

            res.on('end', () => {
                try {
                    const parsed = JSON.parse(responseData);
                    if (parsed.error) {
                        reject(new Error(parsed.error.message));
                    } else {
                        resolve(parsed);
                    }
                } catch (e) {
                    reject(e);
                }
            });
        });

        req.on('error', (e) => {
            reject(e);
        });

        req.write(data);
        req.end();
    });
}

async function generateMultiple(prompt, count) {
    const promises = [];
    for (let i = 0; i < count; i++) {
        // Add variation to each prompt
        const variations = [
            prompt,
            prompt + ', artistic interpretation',
            prompt + ', bold colors',
            prompt + ', subtle texture'
        ];
        promises.push(callOpenAI(variations[i % variations.length]));
    }
    
    const results = await Promise.all(promises);
    return results.map(r => r.data[0].url);
}

const server = http.createServer(async (req, res) => {
    const parsedUrl = url.parse(req.url, true);
    
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    if (parsedUrl.pathname === '/og/api/generate' && req.method === 'POST') {
        let body = '';
        
        req.on('data', chunk => {
            body += chunk.toString();
        });
        
        req.on('end', async () => {
            try {
                const { prompt, count = 4 } = JSON.parse(body);
                
                if (!prompt) {
                    res.writeHead(400, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ error: 'Prompt required' }));
                    return;
                }
                
                console.log(`Generating ${count} images for: ${prompt}`);
                const images = await generateMultiple(prompt, count);
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ images }));
                
            } catch (error) {
                console.error('Error:', error);
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    } else {
        res.writeHead(404);
        res.end('Not found');
    }
});

server.listen(PORT, () => {
    console.log(`✓ OG API server running on http://localhost:${PORT}`);
    console.log(`  Frontend: http://localhost:8765/og/`);
});
