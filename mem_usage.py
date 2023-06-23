import os
import psutil



def monitor_proc():
    while True:

        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):

        
    
            process = {
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu_percent': proc.info['cpu_percent'],
                'memory_percent': proc.info['memory_percent']
            }
    
            processes.append(process)

        print('PID\tNAME\tCPU\tMEMORY %')
        for process in processes:
            print(f"{process['pid']}\t{process['name']}\t{process['cpu_percent']}\t{process['memory_percent']}")

        print("\n")
        time.sleep(5)


monitor_proc()

