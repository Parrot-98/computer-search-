from pathlib import Path
import time
import threading
import os

def search_func(folder, x):
    x_lower = x.lower()
    try:
        for item in os.scandir(folder):  
            if x_lower in item.name.lower():
                print(Path(item.path))  
            elif item.is_dir(follow_symlinks=False):
                search_func(item.path, x)
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



