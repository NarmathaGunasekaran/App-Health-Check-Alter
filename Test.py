import time
import threading

running = True  # global flag to stop threads later

def cpu_load():
    while running:
        _ = [x**2 for x in range(10000)]

threads = []
for i in range(4):  # adjust number of CPU threads
    t = threading.Thread(target=cpu_load)
    t.start()
    threads.append(t)

# Run for 2 minutes
time.sleep(120)
running = False   # stop threads

# Wait for all threads to finish
for t in threads:
    t.join()

print("CPU stress test finished ✅")

