# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:58:14 2024

@author: Piotr
"""

def round_robin_scheduler(processes, time_quantum):
    current_time = 0
    remaining_times = [process['execution_time'] for process in processes]
    waiting_times = [0] * len(processes)
    
    while any(remaining_times):
        for i in range(len(processes)):
            if remaining_times[i] > 0: # Sprawdzenie, czy dany proces ma jeszcze pozostały czas wykonania
                # Jeśli pozostały czas wykonania jest mniejszy lub równy kwantom czasu,
                # to proces zostaje zakończony w obecnej jednostce czasu
                if remaining_times[i] <= time_quantum:
                    current_time += remaining_times[i]
                    waiting_times[i] = current_time - processes[i]['arrival_time'] - processes[i]['execution_time']
                    remaining_times[i] = 0
                else:
                    # W przeciwnym razie, wykonuje się tylko fragment czasu równy kwantom czasu,
                    # a pozostały czas procesu jest aktualizowany
                    current_time += time_quantum
                    remaining_times[i] -= time_quantum
    
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    return average_waiting_time
