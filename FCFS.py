# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:58:13 2024

@author: Piotr
"""


def fcfs_scheduler(processes):
    current_time = 0
    waiting_times = []
    
    for process in processes:
        if current_time < process['arrival_time']: # Sprawdza, czy aktualny czas jest mniejszy niż czas przybycia danego procesu
            current_time = process['arrival_time'] # Jeśli tak, aktualizuje aktualny czas na czas przybycia procesu
        
        waiting_time = current_time - process['arrival_time'] # Oblicza czas oczekiwania dla danego procesu
        waiting_times.append(waiting_time) # Dodaje czas oczekiwania do listy waiting_times
        
        current_time += process['execution_time'] # Aktualizuje aktualny czas o czas wykonania danego procesu
    
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    return average_waiting_time
