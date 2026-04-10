

# 💹 Financial Assistant with Phidata

A multi-agent AI financial assistant built with [Phidata](https://phidata.com), [Groq](https://groq.com), and real-time financial tools. It combines a **Web Search Agent** and a **Financial Data Agent** to deliver stock analysis, analyst recommendations, and latest news — all in one response.

---

## 🧠 How It Works

```
User Query
    │
    ▼
Multi Agent (Coordinator)
    ├──► Web Search Agent  ──► DuckDuckGo  ──► Latest News & Sources
    └──► Financial Agent   ──► YFinance    ──► Stock Price, Fundamentals, Recommendations
    │
    ▼
Combined Structured Report
```

---

## 🚀 Features

- 📈 Real-time stock prices and fundamentals
- 📊 Analyst recommendations in table format
- 📰 Latest financial news with sources
- 🔍 Web search for broader market context
- 🤖 Multi-agent orchestration with Phidata
- ⚡ Fast inference powered by Groq (llama-3.3-70b-versatile)
- 🖥️ CLI mode and Playground UI mode

---

## 📁 Project Structure

```
financial-assistant/
├── agents.py              # All agent definitions (websearch, financial, multi)
├── financial_agent.py     # CLI entry point
├── playground.py          # Phidata Playground UI entry point
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore             # Keeps .env safe from GitHub
└── README.md              # This file
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/financial-assistant.git
cd financial-assistant
```

### 2. Create a virtual environment
```bash
conda create -n finance_agent python=3.11 -y
conda activate finance_agent
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```

Open `.env` and fill in your keys:
```env
GROQ_API_KEY=gsk_your_groq_key_here
PHI_API_KEY=phi_your_phi_key_here   # optional, only for Playground UI
```

| Key | Required | Where to get it |
|-----|----------|-----------------|
| `GROQ_API_KEY` | ✅ Yes | https://console.groq.com/keys |
| `PHI_API_KEY` | ⚡ Optional | https://phidata.app (for visual UI only) |

---

## ▶️ Usage

### CLI Mode
```bash
python financial_agent.py
```

Or pass a custom query:
```bash
python financial_agent.py "Summarise analyst recommendations for Apple"
python financial_agent.py "What is the latest news on Tesla stock?"
python financial_agent.py "Compare NVIDIA and AMD fundamentals"
```

### Playground UI Mode
```bash
python playground.py
```

- **Without PHI_API_KEY** → opens Swagger UI at `http://localhost:7777/docs`
- **With PHI_API_KEY** → connects to visual UI at `https://phidata.app`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Phidata](https://phidata.com) | Multi-agent orchestration framework |
| [Groq](https://groq.com) | Ultra-fast LLM inference |
| [Llama 3.3 70B](https://groq.com) | Language model for all agents |
| [YFinance](https://pypi.org/project/yfinance/) | Stock data, fundamentals, recommendations |
| [DuckDuckGo](https://pypi.org/project/duckduckgo-search/) | Web search for news |
| [FastAPI](https://fastapi.tiangolo.com/) | Playground REST API |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |

---

## 📌 Example Queries

```bash
python financial_agent.py "Summarise analyst recommendations for NVIDIA"
python financial_agent.py "What are the latest news and stock price for Microsoft?"
python financial_agent.py "Give me the fundamentals of Amazon stock"
python financial_agent.py "Compare Apple and Google analyst recommendations"
```

---

## ⚠️ Important Notes

- Never commit your `.env` file — it is listed in `.gitignore`
- Use `.env.example` as a template for collaborators
- Groq API keys starting with `gsk_` should never be shared publicly
- The `llama-3.3-70b-versatile` model is the recommended Groq model for tool use

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ using Phidata and Groq.
