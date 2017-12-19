import math
input = 325489
moves = math.ceil((math.sqrt(input) + 1)/2) - 1 # radial moves to the center
axis1 = int(math.pow(2*moves -1,2) + moves)
axes = [axis1,axis1 + 2 * moves, axis1 + 4 * moves, axis1 + 6 * moves]
tan = input # tangential moves to the axis
for a in axes:
    tan = min(tan,abs(a - input))
print(tan+moves) # 552