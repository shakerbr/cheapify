const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3001;
const DATA_DIR = path.join(__dirname, 'data');
const JSON_FILE = path.join(DATA_DIR, 'waitlist.json');
const CSV_FILE = path.join(DATA_DIR, 'waitlist.csv');

// Ensure data directory and files exist
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}

if (!fs.existsSync(JSON_FILE)) {
  fs.writeFileSync(JSON_FILE, JSON.stringify([], null, 2), 'utf8');
}

if (!fs.existsSync(CSV_FILE)) {
  const header = 'id,timestamp,role,contact,item,ip,user_agent\n';
  fs.writeFileSync(CSV_FILE, header, 'utf8');
}

const server = http.createServer((req, res) => {
  // Common CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const pathname = parsedUrl.pathname;

  // Health check
  if (pathname === '/api/health' || pathname === '/api/waitlist/health') {
    let count = 0;
    try {
      const data = JSON.parse(fs.readFileSync(JSON_FILE, 'utf8'));
      count = data.length;
    } catch {}
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', timestamp: new Date().toISOString(), total_entries: count }));
    return;
  }

  // POST /api/waitlist
  if (pathname === '/api/waitlist' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      if (body.length > 1e5) {
        req.destroy(); // 100KB max payload
      }
    });

    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        const contact = (payload.contact || '').trim();
        const role = payload.role === 'merchant' ? 'merchant' : 'shopper';
        const item = (payload.item || '').trim();

        if (!contact || contact.length < 3) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Valid phone number or contact is required' }));
          return;
        }

        const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';
        const userAgent = req.headers['user-agent'] || 'unknown';
        const timestamp = new Date().toISOString();
        const id = 'w_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);

        const newEntry = {
          id,
          timestamp,
          role,
          contact,
          item: item || null,
          ip,
          userAgent
        };

        // 1. Update JSON file
        let list = [];
        try {
          list = JSON.parse(fs.readFileSync(JSON_FILE, 'utf8') || '[]');
        } catch {
          list = [];
        }
        list.push(newEntry);
        fs.writeFileSync(JSON_FILE, JSON.stringify(list, null, 2), 'utf8');

        // 2. Append to CSV file
        const csvLine = `"${id}","${timestamp}","${role}","${contact.replace(/"/g, '""')}","${(item || '').replace(/"/g, '""')}","${ip.replace(/"/g, '""')}","${userAgent.replace(/"/g, '""')}"\n`;
        fs.appendFileSync(CSV_FILE, csvLine, 'utf8');

        console.log(`[${timestamp}] New waitlist entry: ${role} - ${contact} (Total: ${list.length})`);

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          success: true,
          message: 'Enrolled successfully in Cheapify early access',
          id,
          role,
          contact
        }));
      } catch (err) {
        console.error('Error processing waitlist submission:', err);
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Failed to process submission' }));
      }
    });
    return;
  }

  // GET /api/waitlist - View entries (supports ?key=cheapify2026 or ?format=csv)
  if (pathname === '/api/waitlist' && req.method === 'GET') {
    const key = parsedUrl.searchParams.get('key');
    const format = parsedUrl.searchParams.get('format');

    // Simple auth check for viewing entries
    if (key !== 'cheapify2026') {
      res.writeHead(401, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Unauthorized. Provide valid key.' }));
      return;
    }

    if (format === 'csv') {
      const csvData = fs.readFileSync(CSV_FILE, 'utf8');
      res.writeHead(200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="cheapify-waitlist.csv"'
      });
      res.end(csvData);
      return;
    }

    const jsonData = fs.readFileSync(JSON_FILE, 'utf8');
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(jsonData);
    return;
  }

  // Default 404
  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Cheapify Waitlist API server listening on port ${PORT}`);
});
