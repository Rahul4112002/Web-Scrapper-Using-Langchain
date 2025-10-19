# Web Scraper with LangChain

A compact LangChain-based web scraper and RAG (retrieval-augmented generation) demo. The project crawls web pages, extracts and cleans content, builds embeddings, and exposes a simple runner (`app.py`) to index data and query it with an LLM-backed retriever.

## Two-line summary
- LangChain-powered scraper that fetches, cleans, and embeds web content for RAG workflows.
- Includes a minimal `app.py` to run scraping, build a vector index, and ask questions over scraped content.

## Features

- Fetch and parse HTML pages (BeautifulSoup, requests/httpx).
- Text extraction and cleaning suitable for embedding.
- Create vector embeddings and a searchable index for retrieval.
- LLM-backed QA and summarization over retrieved documents (configurable model/provider).

## Repo structure

- `app.py` — main runner for scraping, indexing, and querying.
- `requirements.txt` — pinned Python dependencies used by the project.

> Note: This repository is intentionally minimal — extend it with crawler, splitter, or storage components as needed.

## Quick start (Windows)

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Upgrade pip and install dependencies:

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables (example using a `.env` file):

Create a `.env` file in the project root with the keys your LLM/provider requires. Example for OpenAI:

```
OPENAI_API_KEY=sk-...
```

4. Run the main script:

```cmd
python app.py
```

If the project includes a Streamlit interface (some setups do), you can run:

```cmd
streamlit run app.py
```

## Configuration and environment

- The project expects standard environment variables for your LLM provider (for example `OPENAI_API_KEY` for OpenAI).
- If the project uses Selenium for dynamic sites, ensure Chrome is installed. A compatible ChromeDriver is required — the `chromedriver-autoinstaller` package in `requirements.txt` can auto-install a matching driver at runtime.

## How it works (high level)

1. Crawl or fetch target URLs.
2. Extract and clean visible text from pages (HTML -> plain text).
3. Split long documents into chunks suitable for embedding.
4. Create embeddings and store them in a vector index.
5. On query, retrieve relevant chunks and pass them to an LLM to generate answers or summaries.

## Troubleshooting

- Dependency installation fails: try upgrading pip, then reinstall. On Windows, prefer the latest Python 3.11+ and ensure build tools are available for binary wheels.
- Chromedriver/Selenium issues: make sure Chrome is installed and versions match. `chromedriver-autoinstaller` should auto-download a compatible driver; run the script with network access.
- Missing API key errors: set your provider key in the environment or `.env` file and restart.
- LLM or embedding errors: check model names and provider credentials; consult provider docs for quota/rate limits.

## Extending the project

- Add a proper crawler with politeness (rate-limiting, robots.txt). Consider `scrapy` for large-scale crawling.
- Replace the vector store or embeddings backend (FAISS, Pinecone, Milvus, Chroma, etc.).
- Add a lightweight web UI (Streamlit or FastAPI) to make the RAG workflow interactive.

## License

This project is provided as-is. Add a license file if you plan to distribute or open-source it (e.g., MIT).

## Contact

For questions or improvements, open an issue or PR in the repository.
