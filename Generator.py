import numpy as np

def generate_processes(num_processes, average_execution_time, execution_time_deviation, arrival_time_range):
    # Generowanie czasów nadejścia z określonego zakresu
    arrival_times = np.random.randint(arrival_time_range[0], arrival_time_range[1] + 1, size=num_processes)
    
    # Generowanie czasów wykonywania z rozkładu normalnego
    execution_times = np.random.normal(average_execution_time, execution_time_deviation, size=num_processes)
    execution_times = np.abs(execution_times).astype(int)  # Konwersja na dodatnie liczby całkowite
    
    processes = []
    for i in range(num_processes):
        process = {
            'id':i+1,
            'arrival_time': arrival_times[i],
            'execution_time': max(1, execution_times[i])
        }
        processes.append(process)
    
    return processes
def generate_pages(num_pages, max_page_size):
    pages = []
    
    #generowanie randomowej wielkoci strony dla każdej strony
    for i in range(num_pages):
        page_size = np.random.randint(1, max_page_size)
        pages.append(page_size)
    
    
    return pages