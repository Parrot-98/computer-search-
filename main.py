from pathlib import Path

folders = [
    Path.home(),                     
    Path("C:/Program Files"),
    Path("C:/Program Files (x86)")
]

x = input("Enter what you want to find: ")

for folder in folders:
    for i in folder.rglob("*"):
        try:
            if x.lower() in i.name.lower():
                print(i)
        except PermissionError:
            pass


