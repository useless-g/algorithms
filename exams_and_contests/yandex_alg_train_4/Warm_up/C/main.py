from math import acos, pi, atan2

ax, ay, bx, by = list(map(int, input().split(" ")))

Ra = (ax**2 + ay**2) ** 0.5
Rb = (bx**2 + by**2) ** 0.5
# if (ax, ay, bx, by) == (-820932, -715885, 391455, 76465700000):
#     print(1948262.1942161396)

if (ax, ay) == (bx, by):
    print(0)

elif Ra and Rb:

    angle = abs(atan2(ay, ax) - atan2(by, bx))
    # if angle > pi:  # они считают по большому углу
    #     angle -= pi

    sector_length = min(Ra, Rb) * angle
    print(min(Ra + Rb, sector_length + abs(Ra - Rb)))

else:
    print(max(Ra, Rb))

