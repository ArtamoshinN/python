x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())
k1 = 0
if x1 // y1 > 0 and x2 // y2 > 0 and x3 // y3 > 0:
    k1 = (x1 // y1) * (x2 // y2) * (x3 // y3)
if x1 // y1 > 0 and x2 // y3 > 0 and x3 // y2 > 0:
    if k1 <= (x1 // y1) * (x2 // y3) * (x3 // y2):
        k1 = (x1 // y1) * (x2 // y3) * (x3 // y2)
if x1 // y2 > 0 and x2 // y1 > 0 and x3 // y3 > 0:
    if k1 <= (x1 // y2) * (x2 // y1) * (x3 // y3):
        k1 = (x1 // y2) * (x2 // y1) * (x3 // y3)
if x1 // y2 > 0 and x2 // y3 > 0 and x3 // y1 > 0:
    if k1 <= (x1 // y2) * (x2 // y3) * (x3 // y1):
        k1 = (x1 // y2) * (x2 // y3) * (x3 // y1)
if x1 // y1 > 0 and x2 // y2 > 0 and x3 // y3 > 0:
    if k1 <= (x1 // y3) * (x2 // y1) * (x3 // y2):
        k1 = (x1 // y3) * (x2 // y1) * (x3 // y2)
if x1 // y1 > 0 and x2 // y2 > 0 and x3 // y3 > 0:
    if k1 <= (x1 // y3) * (x2 // y2) * (x3 // y1):
        k1 = (x1 // y3) * (x2 // y2) * (x3 // y1)
print(k1)
