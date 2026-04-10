# financial_agent.py — CLI runner for the multi-agent financial assistant

from agent import build_websearch_agent, build_financial_agent, build_multi_agent
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Validate required environment variables
required_keys = ["GROQ_API_KEY"]
missing = [k for k in required_keys if not os.getenv(k)]
if missing:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing)}\n"
        "Please check your .env file."
    )

# Build agents
websearch_agent = build_websearch_agent()
financial_agent = build_financial_agent()
multi_agent    = build_multi_agent(websearch_agent, financial_agent)


def run(query: str, stream: bool = True):
    """Run a query through the multi-agent financial assistant."""
    print(f"\n{'='*60}")
    print(f"  Query: {query}")
    print(f"{'='*60}\n")
    multi_agent.print_response(query, stream=stream)


if __name__ == "__main__":
    import sys

    # Accept an optional CLI argument, else use a default query
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else (
        "Summarise analyst recommendations and latest news for NVIDIA (NVDA)."
    )
    run(query)