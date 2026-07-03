import json
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()


class PlannerLLM:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def plan(self, task):
        workflow = [
            {"agent": "analysis"},
            {"agent": "visualization"},
            {"agent": "report"}
        ]

        return json.dumps(workflow)