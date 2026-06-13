# Stock Trading Analyst

An automated stock analysis project powered by **n8n** workflows and **Python** scripts.
## Workflow in action
   ![n8n workflow](workflow-screenshot.png)

## What it does

- Fetches daily stock prices automatically (via n8n on a schedule)
- Calculates simple indicators (daily % change, moving averages)
- Sends a daily summary alert (email, Telegram, or Slack)

## Project structure

```
stock-trading-analyst/
├── n8n/        # n8n workflow exports (.json) — import these into n8n
├── scripts/    # Python analysis scripts
├── data/       # Sample data (small CSVs only)
└── docs/       # Setup guides and notes
```

## Quick start

1. **Run n8n locally** (Docker):
   ```bash
   docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
   ```
   Then open http://localhost:5678

2. **Import the workflow**: in n8n, create a new workflow → menu (⋯) → *Import from file* → choose `n8n/daily-stock-analysis.json`

3. **Add your API key**: get a free key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and paste it into the HTTP Request node

4. **Activate the workflow** (toggle in top-right of n8n)

See `docs/setup.md` for the full guide.

## Important

- Never commit API keys. Use n8n credentials or a `.env` file (already in `.gitignore`).
- This project is for learning/analysis only — not financial advice.
