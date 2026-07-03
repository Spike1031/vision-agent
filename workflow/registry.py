from agents.analysis import AnalysisAgent
from agents.report import ReportAgent
from tools.visualization import VisualizationAgent


class Registry:

    def __init__(self):

        self.tools = {
            "analysis": AnalysisAgent(),
            "visualization": VisualizationAgent(),
            "report": ReportAgent()
        }

    def get(self, name):

        return self.tools.get(name)