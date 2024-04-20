import sys
import math

input = sys.stdin.readline
line_a = tuple(map(float, input().split()))
line_b = tuple(map(float, input().split()))
INF = 10 ** 10

if line_b[0] == line_b[2]:
    line_a, line_b = line_b, line_a


def equation(xa, ya, xb, yb):
    if xa == xb:
        return INF, INF

    slope = (yb - ya) / (xb - xa)
    cut = ya - slope * xa

    return slope, cut


axh, axl = max(line_a[0], line_a[2]), min(line_a[0], line_a[2])
ayh, ayl = max(line_a[1], line_a[3]), min(line_a[1], line_a[3])
bxh, bxl = max(line_b[0], line_b[2]), min(line_b[0], line_b[2])
byh, byl = max(line_b[1], line_b[3]), min(line_b[1], line_b[3])

slope_a, cut_a = equation(*line_a)
slope_b, cut_b = equation(*line_b)
e = 10 ** -6


def is_interact():
    if math.isclose(slope_a, slope_b):
        if slope_b == INF:
            if axl == bxl and not (ayh < byl or byh < ayl):
                return 1
        else:
            if math.isclose(cut_a, cut_b) and not (axh < bxl or bxh < axl):
                return 1
    else:
        if slope_a == INF:
            y = slope_b * axl + cut_b
            if bxl <= axl <= bxh and ayl - e <= y <= ayh + e:
                return 1
        else:
            value = (cut_b - cut_a) / (slope_a - slope_b)
            if axl - e <= value <= axh + e and bxl - e <= value <= bxh + e:
                return 1
    return 0


print(is_interact())
