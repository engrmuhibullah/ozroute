<div align="center">
  <a href="https://youtu.be/If7Xeozh17Q">
    <img src="https://img.youtube.com/vi/If7Xeozh17Q/0.jpg" alt="OmniRoute GitHub: Free Unlimited AI Access Just Dropped">
  </a>
  <h3>📺 <a href="https://youtu.be/If7Xeozh17Q">Watch the full tutorial on YouTube</a></h3>
</div>

<div align="center">

# 🚀 OmniRoute AI Explorer

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI SDK](https://img.shields.io/badge/OpenAI-SDK-green.svg)](https://pypi.org/project/openai/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)

**A lightweight, unified dashboard and reporting tool powered by OmniRoute — The Free AI Gateway.**

Connect to 237+ AI providers through a single endpoint. Generate code, chat with models, and automate beautiful Markdown reports—all while saving up to 95% of your tokens using OmniRoute's built-in compression.

*(Note: To install the core OmniRoute gateway itself, please clone the [official OmniRoute repo](https://github.com/diegosouzapw/OmniRoute) or install via `npm install -g omniroute`)*

</div>

---

## ⚡ Quick Start (Windows PowerShell)

You can run this entire project locally in under 2 minutes.

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Generate a Markdown Report
Programmatically generate an automated report via OmniRoute:
```powershell
python generate_report.py
```

### 3. Launch the Visual Interface
Start the Streamlit explorer to chat interactively with OmniRoute:
```powershell
streamlit run app.py
```

---

## 🛠️ Tech Stack

- **Python**: Core logic and scripting.
- **Streamlit**: Fast, responsive frontend for the visual AI explorer.
- **OpenAI SDK**: Communicates natively with OmniRoute via its OpenAI-compatible `/v1` endpoint.

---

## 📂 File Explanations

- `README.md`: The document you are reading; setup and project overview.
- `requirements.txt`: Contains minimal dependencies (`openai`, `streamlit`).
- `app.py`: The visual Streamlit dashboard for interactive OmniRoute querying.
- `generate_report.py`: A command-line script that queries OmniRoute to generate a formatted Markdown report.
- `outputs.md`: The generated visual report showing AI analysis results.

---

## 🎯 5 Use Cases

1. **Unified AI Benchmarking**: Test different models (via OmniRoute's `auto` routing) on the same prompt without changing API keys.
2. **Automated Code Reviews**: Use `generate_report.py` in a CI/CD pipeline to generate markdown PR reviews.
3. **Token-Optimized Chats**: Chat through `app.py` leveraging OmniRoute's Caveman compression for cost savings.
4. **Resilient AI Pipelines**: Build scripts that never fail due to rate limits by utilizing OmniRoute's 4-tier fallback system.
5. **Local-First Development**: Develop AI features locally against `localhost:20128` without worrying about cloud latency or internet drops.

---

## 🚀 5 Future Features

1. **Multi-Model Comparison View**: A split-screen UI in Streamlit to compare answers from two different models simultaneously.
2. **Cost & Token Analytics Panel**: Visualize the token savings achieved by OmniRoute's compression in real-time.
3. **Custom System Prompt Library**: Allow users to save and load different system prompts for coding, writing, or analysis.
4. **PDF/Document Parsing**: Upload documents in Streamlit and have OmniRoute process and summarize them.
5. **Streaming Report Generation**: Stream the markdown report generation live to the console instead of waiting for the full response.

---
<div align="center">
<i>Keywords: OmniRoute, OpenAI, Streamlit, LLM, Generative AI, AI Gateway, Python, Open Source, Coding Agents, Build In Public, Software Engineering, Developer Tools, Machine Learning, Data Science</i>
</div>
