# agents.py — defines all agents (imported by both CLI and playground)

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


def build_websearch_agent() -> Agent:
    return Agent(
        name="Web Search Agent",
        role="Search the web for financial news and general information",
        tools=[DuckDuckGo()],
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "You are an independent web search agent.",
            "Always cite the source URL for every piece of information you provide.",
            "Focus on recent, relevant financial news.",
            "Never delegate tasks to other agents.",
        ],
        show_tool_calls=True,
        markdown=True,
    )


def build_financial_agent() -> Agent:
    return Agent(
        name="Financial Data Agent",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
            )
        ],
        instructions=[
            "You are an independent financial data agent.",
            "Always display numerical data in well-formatted markdown tables.",
            "Only call one tool at a time.",        # ← fixes the function call error
            "Wait for tool results before calling another tool.",
        ],
        show_tool_calls=True,
        markdown=True,
    )


def build_multi_agent(websearch_agent: Agent, financial_agent: Agent) -> Agent:
    return Agent(
        name="Financial Assistant",
        team=[websearch_agent, financial_agent],
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "You are a senior financial assistant coordinating a team of specialised agents.",
            "Delegate web/news queries to the Web Search Agent.",
            "Delegate stock data, price, fundamentals, and recommendations to the Financial Data Agent.",
            "Combine results into a clear, structured report with:",
            "  1. Executive summary",
            "  2. Key financial metrics (table)",
            "  3. Analyst recommendations (table)",
            "  4. Latest news highlights (with sources)",
            "  5. Brief investment outlook",
            "Always use markdown tables for structured data.",
        ],
        show_tool_calls=True,
        markdown=True,
    )