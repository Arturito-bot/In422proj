from .scheduling_algorithm import SchedulingAlgorithm

class EarliestDeadlineFirst(SchedulingAlgorithm):
    def schedule(self):
        """Schedule tasks using the Earliest Deadline First algorithm, accounting for new tasks."""
        # Initialiser les tâches déjà arrivées (initialement triées par deadline)
        self.tasks.sort(key=lambda task: task['deadline'])  # Trier les tâches par deadline
        scheduled_tasks = []
        time = 0  # Le temps de la simulation
        remaining_tasks = self.tasks[:]
        
        while remaining_tasks:
            # Sélectionner la tâche ayant la deadline la plus proche parmi les tâches arrivées
            current_task = remaining_tasks.pop(0)
            scheduled_tasks.append(current_task)
            time += current_task['duration']  # Avancer le temps de l'exécution de la tâche
            
            # Mettre à jour les nouvelles tâches arrivées pendant l'exécution
            new_tasks = self.get_new_tasks(time)  # Méthode fictive à définir pour récupérer de nouvelles tâches
            remaining_tasks.extend(new_tasks)
            
            # Trier les tâches restantes à chaque cycle par deadline
            remaining_tasks.sort(key=lambda task: task['deadline'])
            
        return scheduled_tasks

    def get_new_tasks(self, current_time):
        """Retourner les nouvelles tâches arrivées à l'instant actuel (par exemple, basées sur la période)."""
        # Exemple d'une logique simple pour renvoyer de nouvelles tâches arrivant à ce moment
        new_tasks = []
        # Logique fictive : ajout d'une tâche qui arrive à un certain moment
        if current_time == 6:  # Une tâche arrive à l'instant 6
            new_tasks.append({'name': 'Task4', 'duration': 3, 'deadline': 10})
        return new_tasks
