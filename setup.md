# Setup Guide

## 1. Get a free API key

1. Go to https://www.alphavantage.co/support/#api-key
2. Enter your email → you get a free API key instantly
3. Free tier = 25 requests/day, which is plenty to start

## 2. Run n8n

**Option A — Docker (recommended):**
```bash
docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

**Option B — Node.js:**
```bash
npx n8n
```

Open http://localhost:5678 and create your local account.

## 3. Import the workflow

1. In n8n, click **+ New workflow**
2. Click the **⋯** menu (top right) → **Import from file**
3. Select `n8n/daily-stock-analysis.json` from this repo
4. Open the **Get Stock Price** node and replace `YOUR_API_KEY_HERE` with your real key
5. Click **Execute workflow** to test it
6. Toggle **Active** (top right) to run it on schedule

## 4. Add a notification (optional next step)

Add one more node after "Analyze":
- **Gmail** node → email yourself the `summary` field
- or **Telegram** node → message yourself
- or **Slack** node → post to a channel

## 5. Run the Python script (optional)

```bash
pip install requests pandas
export ALPHAVANTAGE_API_KEY=your_key_here    # Windows: set ALPHAVANTAGE_API_KEY=your_key_here
python scripts/analyze.py AAPL
```

## Keeping the repo updated

Whenever you change the workflow in n8n:
1. Menu (⋯) → **Download** to export the .json
2. Replace the file in `n8n/` and commit:
```bash
git add n8n/
git commit -m "Update workflow"
git push
```
