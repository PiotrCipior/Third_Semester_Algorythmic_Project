# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:46:32 2024

@author: Piotr
"""

'''
Główny plik który zawiera podstawowe menu oraz obliczanie rednią dla wszystkich powtórzeń algorytmów procesów
'''
from Generator import generate_processes
from Generator import generate_pages
from fifo import fifo
from LRU import lru
from FCFS import fcfs_scheduler
from round_robin import round_robin_scheduler
import sys

fcfs_result = 0
round_robin_result = 0
lru_result = 0
fifo_result = 0

time_quantum = 3
choice = input("wybierz: \n 1. Algorytmy planowania procesów \n 2. Algorytmy zastępywania stron \n (Wpisz 1 albo 2): ")


if choice == "1":
    program_reapets = int(input("Ile razy program ma powtórzyć testy: "))

    num_processes = int(input("Podaj liczbę procesów: "))
    arrival_range_start = int(input("Podaj minimalną liczbę czasu nadejcia: "))
    arrival_range_end = int(input("Podaj maksymalną liczbę czasu nadejcia: "))
    arrival_range = (arrival_range_start, arrival_range_end)

    average_time = int(input("Podaj sredni czas procesów: "))
    time_deviation = int(input("Podaj odchylenie standardowe: "))
    for i in range(program_reapets):

        processes = generate_processes(num_processes, average_time, time_deviation, arrival_range)

        # FCFS
        avg_waiting_time_fcfs = fcfs_scheduler(processes)
        print( f"Średni czas oczekiwania dla algorytmu FCFS: {avg_waiting_time_fcfs}")

        # round-robin
        avg_waiting_time_round_robin = round_robin_scheduler( processes, time_quantum)
        print(f"Średni czas oczekiwania dla algorytmu Round Robin: {avg_waiting_time_round_robin}")
        
        fcfs_result+= avg_waiting_time_fcfs
        round_robin_result+=avg_waiting_time_round_robin
    fcfs_result = fcfs_result/program_reapets
    round_robin_result = round_robin_result/program_reapets
    print(f"Średni czas algorytmu FCFS: {fcfs_result}")
    print(f"Średni czas algorytmu round_robin: {round_robin_result}")
    
        
elif choice == "2":
    num_pages = int(input("Podaj liczbę żądań stron: "))
    page_size = int(input("Podaj wielkoć stron: "))

    pages = generate_pages(num_pages, page_size)
    while(True):
        pages_frame = int(input("Podaj liczbę ramek w pamięci: "))
        # fifo
        fifo_faults = fifo(pages, pages_frame)
        print(f"FIFO Page Faults: {fifo_faults}")
    
        # lru
        lru_faults = lru(pages, pages_frame)
        print(f"LRU Page Faults: {lru_faults}")
    
    
        choice_if_reapete = input("Czy chcesz powtórzyć z inną iloscią ramek pamięci(y/n): ")
        if choice_if_reapete == "n":
            break
else:
    print("Błąd!")
    sys.exit(0)
