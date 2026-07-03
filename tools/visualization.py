import os

import matplotlib.pyplot as plt


class VisualizationAgent:

    def create_bar_chart(self, analysis_result):

        labels = list(analysis_result.keys())
        values = list(analysis_result.values())

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values)

        plt.title("Detected Objects")
        plt.ylabel("Count")
        plt.xticks(rotation=20)

        plt.tight_layout()

        os.makedirs("reports", exist_ok=True)

        output_path = "reports/object_distribution.png"

        plt.savefig(output_path, dpi=300)
        plt.close()

        print(f"Chart saved to {output_path}")

        return output_path

    def run(self, context):

        chart = self.create_bar_chart(
            context["analysis"]
        )

        context["chart"] = chart

        return context