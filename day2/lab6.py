#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#run to university. You jog the first mile at 7mph; then run the next two at15mph; before
#jogging the last at 7mph again. Will this be quicker or slower than the bus?
distance=4
velocity=25
T1 =((distance/velocity)*60)
T2=20
total1 =T1 +T2
J1= ((1/7)*60)
J2= ((2/15)*60)
J3 =((1/7)*60)
total2 = J1 + J2 + J3
print(f"total time taken by bus is {total1}")
if (total1> total2):
    print("going by bus is slower than running")
else:
    print("going on foot is quicker than going by bus")
