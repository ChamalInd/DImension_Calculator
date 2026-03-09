with open('assets/data/winfo.txt') as f:
    string = f.read().splitlines()

width = int(string[0])
height = int(string[1])

x = 100
y = 100