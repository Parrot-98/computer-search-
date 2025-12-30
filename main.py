from pathlib import Path
import time
import threading

def search_func(folders, x):
    for item in folder.rglob("*"):
        try:
            if x.lower() in item.name.lower():
                print(item)
        except PermissionError:
            pass



folders = [
    Path.home(),                     
    Path("C:/Program Files"),
    Path("C:/Program Files (x86)")
] # searchs thses folders only 

x = input("Enter what you want to find: ")

threads = []

start = time.perf_counter()

for folder in folders:
    t = threading.Thread(target=search_func, args=(folder, x))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.perf_counter()

print(f"Time taken: {end - start:.6f} seconds")



