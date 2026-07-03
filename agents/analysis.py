from collections import Counter

from tools.file_reader import FileReader


DETECTION_JSON = "data/detection.json"


class AnalysisAgent:

    def __init__(self):
        self.reader = FileReader()

    def analyze(self):
        print("\n[Analysis Agent]")

        data = self.reader.read_json(DETECTION_JSON)

        counter = Counter()

        for obj in data["objects"]:
            counter[obj["class"]] += 1

        analysis_result = dict(counter)

        print("Analysis Result:")

        for cls, count in analysis_result.items():
            print(f"{cls}: {count}")

        return analysis_result

    def run(self, context):
        context["analysis"] = self.analyze()
        return context