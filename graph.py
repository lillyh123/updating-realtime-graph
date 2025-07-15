import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd

fig = plt.figure() #creates a new 'figure' - includes all plots
ax1 = fig.add_subplot(1,1,1) #creates axis and allows multiple subplots in a single figure

def animate(i):
    data = open("data2.txt","r").read() #opens file
    items = data.split('\n') #split by new line
    xar = [] #x array?
    yar = []
    for eachLine in items: #checks each line
        if len(eachLine)>1: #doesn't check blank lines
            x,y = eachLine.split(',') #split by comma
            xar.append(pd.to_datetime(x, dayfirst=True)) #adds x to list and changes to datetime
            yar.append(int(y)) #adds all y values to a list
    ax1.clear() #resets plots ?
    ax1.plot(xar,yar) #plots the lists
    plt.xlabel("Time") #labels
    plt.ylabel("Temp")
    plt.title("Test graph")
ani = animation.FuncAnimation(fig, animate, interval=50, cache_frame_data=False)
plt.show()
#test
