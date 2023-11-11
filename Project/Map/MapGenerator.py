size = 800, 600

with open("map.txt", 'r') as fileIn:
    lines = [line.strip() for line in fileIn.readlines()]
scaleX = size[0] // len(lines[0])
scaleY = size[1] // len(lines)

print('g')