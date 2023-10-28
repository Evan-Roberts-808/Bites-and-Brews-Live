const fetch = require('node-fetch');

const pingSupabase = async () => {
    try {
        const supabaseUrl = 'https://ltnnixolasteqaakpkor.supabase.co';
        const apiKey = process.env.SUPABASE_API_KEY;

        const response = await fetch(`${supabaseUrl}/rest/v1/recipes`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'apikey': apiKey
            }
        });
        const data = await response.json();
        console.log('Ping successful:', data);
    } catch (error) {
        console.error('Error pinging Supabase:', error);
    }
};

export default function handler(req, res) {
    const { headers } = req;
    const { CRON_SECRET } = process.env;
  
    if (headers.authorization !== `Bearer ${CRON_SECRET}`) {
      return res.status(401).end('Unauthorized');
    }

    // Call the pingSupabase function here
    pingSupabase()
        .then(() => res.status(200).send('Ping sent to Supabase.'))
        .catch((error) => {
            console.error('Error sending ping to Supabase:', error);
            res.status(500).send('Internal Server Error');
        });
}