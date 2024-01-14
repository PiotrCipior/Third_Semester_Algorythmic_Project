# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:55:43 2024

@author: Piotr
"""
from collections import OrderedDict

def lru(pages, frame_size):
    page_order = OrderedDict() # Inicjalizacja OrderedDict do przechowywania kolejności używanych stron
    page_faults = 0
    
    for page in pages:
        if page in page_order:
            page_order.move_to_end(page) #przeniesienie na koniec i oznaczenie jako niedawno użyte
        else:
            if len(page_order) >= frame_size:
                page_order.popitem(last=False) #usunięcie najmniej niedawno używanej strony
            page_order[page] = None # Dodanie nowej strony do słownika na końcu, oznaczając jako niedawno używaną
            page_faults +=1
    return page_faults
