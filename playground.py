# playground.py — serves the Phidata Playground UI

from agent import build_websearch_agent, build_financial_agent, build_multi_agent
from phi.playground import Playground, serve_playground_app
import phi.api
from dotenv import load_dotenv
import os

load_dotenv()

# Required for Phidata Playground authentication
load_dotenv(override=True)
 
# PHI_API_KEY must be set as an environment variable — phi reads it internally
# via os.getenv("PHI_API_KEY"). Do NOT try to set phi.api.api_key directly.
if not os.getenv("PHI_API_KEY"):
    raise EnvironmentError(
        "PHI_API_KEY is not set.\n"
        "Get your key at https://phidata.app and add it to your .env file."
    )

# Build agents
websearch_agent = build_websearch_agent()
financial_agent = build_financial_agent()
multi_agent     = build_multi_agent(websearch_agent, financial_agent)

# All three are available in the Playground dropdown
App = Playground(agents=[multi_agent, websearch_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:App", reload=True)