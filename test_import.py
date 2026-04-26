import sys
import os

# Test if 'packages' can be imported from root
try:
    from packages.core.engine import SuperAgentHarness
    print("Import Successful!")
    agent = SuperAgentHarness()
    print(agent.run_agentic_loop("Sanity Check"))
except Exception as e:
    print(f"Import Failed: {e}")
    print(f"Path: {sys.path}")
