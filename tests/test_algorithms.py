# tests/test_algorithms.py

import unittest
import sys
import os

# Ajouter le dossier parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\IPSA\AeroX\A4\In422\Project\In422proj')))

from Algorithms.round_robin import RoundRobin
from Algorithms.earliest_deadline_first import EarliestDeadlineFirst
from Algorithms.first_come_first_serve import FirstComeFirstServe
from Algorithms.shortest_job_next import ShortestJobNext
from Algorithms.rate_monotonic import RateMonotonic

class TestSchedulingAlgorithms(unittest.TestCase):

    def setUp(self):
        # Créer un set commun de tâches avec des paramètres génériques, y compris `beginning`
        self.tasks = [
            {'name': 'Task1', 'duration': 5, 'deadline': 10, 'period': 5, 'remaining_time': 5, 'beginning': 0},
            {'name': 'Task2', 'duration': 3, 'deadline': 8, 'period': 3, 'remaining_time': 3, 'beginning': 1},
            {'name': 'Task3', 'duration': 2, 'deadline': 6, 'period': 2, 'remaining_time': 2, 'beginning': 6},
        ]

    def test_round_robin(self):
        rr = RoundRobin(time_quantum=2)
        for task in self.tasks:
            rr.add_task(task)  # Ajouter toutes les tâches à RoundRobin

        scheduled_tasks = rr.schedule()

        # Vérifier que les tâches sont planifiées correctement
        expected_order = ['Task1', 'Task2', 'Task1', 'Task2', 'Task3', 'Task1']  # Ordre corrigé
        scheduled_order = [task['name'] for task in scheduled_tasks]
        self.assertEqual(scheduled_order, expected_order)

    def test_earliest_deadline_first(self):
        edf = EarliestDeadlineFirst()
        # Pour EDF, on utilise uniquement les paramètres deadline
        for task in self.tasks:
            edf.add_task({'name': task['name'], 'deadline': task['deadline']})

        scheduled_tasks = edf.schedule()

        # Vérifier que les tâches sont planifiées par ordre de date limite
        expected_order = ['Task3', 'Task2', 'Task1']  # Tâches triées par deadline
        scheduled_order = [task['name'] for task in scheduled_tasks]
        self.assertEqual(scheduled_order, expected_order)

    def test_first_come_first_serve(self):
        fcfs = FirstComeFirstServe()
        for task in self.tasks:
            fcfs.add_task(task)  # Ajouter toutes les tâches à FCFS

        scheduled_tasks = fcfs.schedule()

        # Vérifier que les tâches sont planifiées dans l'ordre de leur arrivée
        expected_order = ['Task1', 'Task2', 'Task3']
        scheduled_order = [task['name'] for task in scheduled_tasks]
        self.assertEqual(scheduled_order, expected_order)

    def test_shortest_job_next(self):
        sjn = ShortestJobNext()
        # Pour SJN, on utilise uniquement les paramètres duration
        for task in self.tasks:
            sjn.add_task({'name': task['name'], 'duration': task['duration']})

        scheduled_tasks = sjn.schedule()

        # Vérifier que les tâches sont planifiées par durée (la plus courte en premier)
        expected_order = ['Task3', 'Task2', 'Task1']
        scheduled_order = [task['name'] for task in scheduled_tasks]
        self.assertEqual(scheduled_order, expected_order)

    def test_rate_monotonic(self):
        rm = RateMonotonic()
        # Pour RM, on utilise uniquement les paramètres period
        for task in self.tasks:
            rm.add_task({'name': task['name'], 'period': task['period']})

        scheduled_tasks = rm.schedule()

        # Vérifier que les tâches sont planifiées par période (la plus courte en premier)
        expected_order = ['Task3', 'Task2', 'Task1']
        scheduled_order = [task['name'] for task in scheduled_tasks]
        self.assertEqual(scheduled_order, expected_order)

if __name__ == '__main__':
    unittest.main()
