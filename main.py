from Line import Line

line1 =  Line(1,5)
line2 =  Line(2,6)


print(line2.overLap(line1))
print(line1.overLap(line2))

line1 =  Line(2,6)
line2 =  Line(3,6)

print(line1.overLap(line2))
print(line2.overLap(line1))

line1 =  Line(2,3)
line2 =  Line(5,6)

print(line2.overLap(line1))
print(line1.overLap(line2))



line1 =  Line(3,6)
line2 =  Line(3,6)

print(line1.overLap(line2))
print(line2.overLap(line1))
