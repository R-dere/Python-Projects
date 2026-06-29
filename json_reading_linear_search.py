import json
import os
print(os.listdir())
with open("data.json", "r") as f:
    data = json.load(f)
found = False
print(data)
needed = int(input("what value from this list are you looking for? \n>>>"))
for i in range (len(data)):
    if data[i] == needed:
        print(f"data found, it is number {1+i} in the list")
        found = True
        break
if not found:
    print("that value is not in the given data")