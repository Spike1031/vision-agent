from tools.yolo_detector import YOLODetector
from agents.planner import PlannerLLM
from workflow.executor import WorkflowExecutor


class VisionAgent:

    def __init__(self):

        self.detector = YOLODetector()

        self.planner = PlannerLLM()

        self.executor = WorkflowExecutor()

    def run(self, image_path):

        print("=" * 60)
        print("Vision Agent Started")
        print("=" * 60)

        # Step 1
        print("\n[1] Object Detection")
        self.detector.detect(image_path)

        # Step 2
        print("\n[2] LLM Planning")

        plan = self.planner.plan(
            "Analyze the detected traffic scene and generate an engineering report."
        )

        print("\n===== Workflow =====")
        print(plan)
        print("====================")

        # Step 3
        print("\n[3] Execute Workflow")

        context = self.executor.execute(plan)

        print("\nWorkflow Finished.")

        return context