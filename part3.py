from msilib.schema import Class
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import math


fig = plt.figure()
ax = fig.add_subplot(111)   

r = 25

def plot_circle(i,j):
    crcl = plt.Circle((i,j),r,fill=False)
    ax.set_aspect(1)
    ax.add_artist(crcl)



xrec1,yrec1 = 30,25         #starting coordinates for figure 1   (bottom left corner coordinates)
lrec1,brec1 = 50,30         #length(along x axis) and width(along y axis) for figure 1 


xrec2,yrec2 = 150,30        #starting coordinates for figure 2
lrec2,brec2 = 40,160        #length(along x axis) and width(along y axis) for figure 1

rectangle1 = matplotlib.patches.Rectangle((xrec1,yrec1),lrec1,brec1,color='green')

rectangle2 = matplotlib.patches.Rectangle((xrec2,yrec2),lrec2,brec2,color='blue')

ax.add_patch(rectangle1)
ax.add_patch(rectangle2)

xl,yl = 200,200

#ax.scatter()

#function to return the nearest boundary point of a removed point
def shifting(x,y,xrec,yrec,lrec,brec):        # x,y -> coordinates of the removed points
    b_points = [[xrec,y],[xrec+lrec,y],[x,yrec],[x,yrec+brec]]
    distances = []

    for i in b_points:
        #plt.plot(i[0],i[1],'ko')  
        #plot_circle(i[0],i[1]) 
        distances.append(math.dist(i,[x,y]))

    ind = distances.index(min(distances))
    plt.plot(b_points[ind][0],b_points[ind][1],'ko')
    plot_circle(b_points[ind][0],b_points[ind][1])


points_to_delete = []
rec2point = []
rec1point = []


row_count = 0

for i in range(xl,-1,-40):
    for j in range(yl,-1,-40):
        if row_count%2==0:
            if (i>xrec2 and i<xrec2+lrec2 and j>yrec2 and j<yrec2+brec2):
                points_to_delete.append((i,j))
                rec2point.append((i,j))
                #plt.plot(i,j,'ro')

            elif (i>xrec1 and i<xrec1+lrec1 and j>yrec1 and j<yrec1+brec1):
                points_to_delete.append((i,j))
                rec1point.append((i,j))
                #plt.plot(i,j,'ro')
            else:
                plt.plot(i,j,'ko')
                plot_circle(i,j)
        else:
            if (i-20>xrec2 and i-20<xrec2+lrec2 and j>yrec2 and j<yrec2+brec2):
                points_to_delete.append((i-20,j))
                rec2point.append((i-20,j))
                #plt.plot(i-20,j,'ro')
            
            elif (i-20>xrec1 and i-20<xrec1+lrec1 and j>yrec1 and j<yrec1+brec1):
                points_to_delete.append((i-20,j))
                rec1point.append((i-20,j))
                #plt.plot(i-20,j,'ro')

            else:
                plt.plot(i-20,j,'ko')
                plot_circle(i-20,j)
        row_count+=1
                   




plt.xlim([0,xl])
plt.ylim([0,yl])

#print(points_to_delete)

for i in rec1point:
    shifting(i[0],i[1],xrec1,yrec1,lrec1,brec1)

for j in rec2point:
    shifting(j[0],j[1],xrec2,yrec2,lrec2,brec2)

plt.title('figure 3')
fig.show()