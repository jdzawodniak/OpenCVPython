import matplotlib.pyplot as plt
x=[1,2,3,4] 
y=[3,5,7,9]
plt.plot(x,y,'b-*',linewidth=3)
plt.plot(y,x,'r--*',linewidth=2)
plt.plot(y,x,'b*',markersize=10) #color options are vast. check of options online
plt.grid(True)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('my graph') # puts title on the graph
plt.axis([0,5,0,10]) #maps the axis with custom range
plt.show()