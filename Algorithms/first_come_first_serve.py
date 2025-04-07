# algorithms/first_come_first_serve.py

from .scheduling_algorithm import SchedulingAlgorithm

class FirstComeFirstServe(SchedulingAlgorithm):
    def schedule(self):
        """Schedule tasks using the First-Come-First-Serve algorithm."""
        # Implémentation de l'algorithme First-Come-First-Serve
        # Les tâches sont planifiées dans l'ordre de leur arrivée
        scheduled_tasks = []

        for task in self.tasks:
            scheduled_tasks.append(task)
            # Ajouter la logique pour vérifier la faisabilité de la planification

        return scheduled_tasks
