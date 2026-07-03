import json

from workflow.registry import Registry


class WorkflowExecutor:

    def __init__(self):
        self.registry = Registry()

    def execute(self, plan_text):

        # Parse workflow plan
        try:
            plan = json.loads(plan_text)
        except json.JSONDecodeError:
            raise ValueError("Invalid workflow plan.")

        context = {}

        for step in plan:

            agent_name = step.get("agent")

            if agent_name is None:
                continue

            print(f"\nExecuting: {agent_name}")

            tool = self.registry.get(agent_name)

            if tool is None:
                print(f"Agent '{agent_name}' not found.")
                continue

            context = tool.run(context)

        return context