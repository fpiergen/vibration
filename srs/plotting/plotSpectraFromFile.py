# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import csv
import matplotlib.pyplot as plt
x=[];
y1=[];
y2=[];
with open('in', 'rb') as f:
    reader = csv.reader(f, delimiter=' ')
    i=0;
    for row in reader:
         if i>300:
             break;
         i=i+1
         x.append(row[0])
         y1.append(row[1])
         y2.append(row[2])

plt.plot(x,y1,lw=2)
plt.plot(x,y2)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('G\'s')
plt.xlabel('Hz')
plt.title('SRS for 40G 0.015 s 1/2 sine shock')
plt.grid(b=None, which='both', axis='both')
plt.show()
