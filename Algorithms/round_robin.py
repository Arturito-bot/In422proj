# algorithms/round_robin.py

from .scheduling_algorithm import SchedulingAlgorithm

class RoundRobin(SchedulingAlgorithm):
    def __init__(self, time_quantum):
        super().__init__()
        self.time_quantum = time_quantum

    def schedule(self):
        scheduled_tasks = []
        tasks = [task.copy() for task in self.tasks]  # Copie pour ne pas modifier les tâches originales
        time = 0
        ready_queue = []

        # On continue tant qu'il reste des tâches (dans la file d'attente ou non encore arrivées)
        while tasks or ready_queue:
            # Ajouter les tâches arrivées au temps actuel dans la file d'attente
            newly_arrived = [t for t in tasks if t['beginning'] <= time]
            ready_queue.extend(sorted(newly_arrived, key=lambda t: t['beginning']))
            tasks = [t for t in tasks if t not in newly_arrived]

            if ready_queue:
                task = ready_queue.pop(0)

                # Exécution pendant le quantum ou le temps restant
                exec_time = min(self.time_quantum, task['remaining_time'])
                task['remaining_time'] -= exec_time
                time += exec_time
                scheduled_tasks.append(task)

                # 💡 Vérifier les nouvelles tâches arrivées pendant l’exécution
                newly_arrived = [t for t in tasks if t['beginning'] <= time]
                ready_queue.extend(sorted(newly_arrived, key=lambda t: t['beginning']))
                tasks = [t for t in tasks if t not in newly_arrived]

                # Si elle n’est pas terminée, on la remet à la fin
                if task['remaining_time'] > 0:
                    ready_queue.append(task)

            else:
                # Si aucune tâche prête, on avance dans le temps
                time += 1

        return scheduled_tasks

