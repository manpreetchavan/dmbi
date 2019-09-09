import matplotlib.pyplot as plt
import statistics as stats

y = [34,108,64,88,99,51]
x = [5,17,11,8,14,5]
meal = [1,2,3,4,5,6]
line = [mean_x] * 6

def mean(list):
    avg=stats.mean(list)
    return avg

def sse(list):
    temp=0
    for i in range(len(list)):
        temp += (list[i]-mean_x)**2
    return temp

def plotit():
    plt.plot(meal,x,'ro')
    plt.plot(meal,line,'r',color='blue')
    plt.show()

def b1(x,y):
    numr,denr = 0,0
    for i in range(0,len(x)):
        print(x[i])
        numr = numr + ((x[i]-mean_x)*(y[i]-mean_y))
        denr = denr + ((y[i]-mean_y)**2)
    print(numr,denr)
    return numr/denr


mean_x=mean(x)
print(mean_x)

mean_y=mean(y)

print(sse(x))
print(b1(x,y))
# plotit()
