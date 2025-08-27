import time
import threading

def cpu_load():
    while True:
        # Just calculate something useless to keep CPU busy
        _ = [x**2 for x in range(10000)]

# Create multiple threads to increase CPU usage
threads = []
for i in range(4):  # Change 4 → number of CPU cores you want to stress
    t = threading.Thread(target=cpu_load)
    t.start()
    threads.append(t)

# Run for 2 minutes
time.sleep(120)
