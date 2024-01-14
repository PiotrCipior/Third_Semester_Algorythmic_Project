# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:58:28 2024

@author: Piotr
"""

from collections import deque

def fifo(pages, frame_size):
    page_queue = deque(maxlen=frame_size) # Inicjalizacja kolejki przy użyciu klasy deque z ograniczeniem do frame_size elementów
    page_faults = 0
    
    for page in pages:
        if page not in page_queue:
            page_queue.append(page) # Jeżeli strona nie istnieje w kolejce, dodaj ją do kolejki
            page_faults += 1
    return page_faults
