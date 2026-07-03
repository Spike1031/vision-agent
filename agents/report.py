REPORT_PATH = "reports/report.md"


class ReportAgent:

    def __init__(self):
        self.name = "Report Agent"

    def generate_report(self, analysis_result, chart_path=None):

        print(f"\n[{self.name}]")

        report = "# Engineering Detection Report\n\n"

        report += "## Object Statistics\n\n"

        total_objects = 0

        for cls, count in analysis_result.items():
            report += f"- {cls}: {count}\n"
            total_objects += count

        if chart_path:
            report += "\n## Object Distribution\n\n"
            report += f"![chart]({chart_path})\n"

        report += "\n## Analysis\n\n"

        report += f"- Total detected objects: {total_objects}\n"

        if total_objects >= 15:
            report += "- Traffic density: High\n"
        elif total_objects >= 8:
            report += "- Traffic density: Medium\n"
        else:
            report += "- Traffic density: Low\n"

        if analysis_result:
            max_class = max(
                analysis_result,
                key=analysis_result.get
            )

            report += (
                f"- Most common object: "
                f"{max_class} "
                f"({analysis_result[max_class]})\n"
            )

        report += "\n## Conclusion\n\n"

        report += (
            "The engineering analysis has been completed successfully.\n"
        )

        return report

    def save_report(self, report):

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"Report saved to {REPORT_PATH}")

    def run(self, context):

        report = self.generate_report(
            context["analysis"],
            context.get("chart")
        )

        self.save_report(report)

        context["report"] = report

        return context