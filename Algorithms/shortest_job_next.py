# algorithms/shortest_job_next.py

from .scheduling_algorithm import SchedulingAlgorithm

class ShortestJobNext(SchedulingAlgorithm):
    def schedule(self):
        """Schedule tasks using the Shortest Job Next algorithm."""
        # Implémentation de l'algorithme Shortest Job Next
        # Trier les tâches par durée (plus la durée est courte, plus la priorité est élevée)
        sorted_tasks = sorted(self.tasks, key=lambda task: task['duration'])
        scheduled_tasks = []

        # Logique de planification basée sur la priorité
        for task in sorted_tasks:
            scheduled_tasks.append(task)
            # Ajouter la logique pour vérifier la faisabilité de la planification

        return scheduled_tasks
