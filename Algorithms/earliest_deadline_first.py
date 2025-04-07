# algorithms/earliest_deadline_first.py

from .scheduling_algorithm import SchedulingAlgorithm

class EarliestDeadlineFirst(SchedulingAlgorithm):
    def schedule(self):
        """Schedule tasks using the Earliest Deadline First algorithm."""
        # Implémentation de l'algorithme Earliest Deadline First
        # Trier les tâches par date limite (plus la date limite est proche, plus la priorité est élevée)
        sorted_tasks = sorted(self.tasks, key=lambda task: task['deadline'])
        scheduled_tasks = []

        # Logique de planification basée sur la priorité
        for task in sorted_tasks:
            scheduled_tasks.append(task)
            # Ajouter la logique pour vérifier la faisabilité de la planification

        return scheduled_tasks
