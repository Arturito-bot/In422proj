# algorithms/scheduling_algorithm.py

class SchedulingAlgorithm:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def schedule(self):
        """Schedule the tasks based on the specific algorithm."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_tasks(self):
        """Return the list of tasks."""
        return self.tasks
