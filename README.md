# 📊 Stock Market Query Agent using LangGraph

This project is an AI-powered **Stock Analysis Agent** that uses LangGraph and Retrieval-Augmented Generation (RAG) to answer natural language queries about stock performance. The agent extracts the stock ticker, retrieves financial and news data, performs analysis, and returns a user-friendly response — all driven by an autonomous workflow graph.

---

## Features

- Ticker extraction from user queries using LLMs  
- Financial data retrieval via custom scraping tools  
- Latest news scraping using **Firecrawl**  
- RAG pipeline for storing and querying stock information  
- LLM-based response generation using LLaMA 3 (via Groq)  
- LangGraph-powered modular execution and routing  
- HTML-formatted output for UI-friendly integration

---

## 📁 Project Structure

```bash
.
├── .DS_Store
├── .gitignore
├── agent.py              # Main graph-based agent logic
├── main.py               # Entry point (run agent from CLI)
├── requirements.txt      # Dependencies
├── scraping.py           # Firecrawl & stock data scraping logic
├── tools.py              # Custom tools (RAG class, Ticker extractor, etc.)
