import math
import random
import matplotlib.pyplot as plt


def value(mytuple, function): #this function helps us decide which function we are performing simmulated annealing on
    x, y = mytuple
    if function == "sphere":
        z = x**2 + y**2
        z = float(z)
        return z
    elif function == "rosenbrock":
        z = 100 * (((x**2) - y)**2) + (1-x)**2
        return z
    elif function == "griewank":
        z = (((x**2)+(y**2))/4000) - (math.cos(x) * math.cos(y/math.sqrt(2))) + 1
        z = float(z)
        return z
    
def currentcode(x_range, y_range): #this helps us get the coordinates of the currentnode
    xmin, xmax = x_range
    ymin, ymax = y_range 
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)
    return (x,y)




def nextnode(curtuple, step, xvals, yvals):
    x, y = curtuple
    lst = [(x-step, y), (x, y-step), (x+step, y), (x, y+step),
               (x-step, y-step), (x+step, y+step), (x-step, y+step), (x+step, y-step)]
    new =  random.choice(lst)
    while new[0] > xvals[1] or new[0] < xvals[0] or new[1] < yvals[0] or new[1] > yvals[1]:
        new = random.choice(lst)
    return new

def simmulated_annealing(x_range, y_range, step, minormax, function):
    xvalues = []
    yvalues = []
    fvalues = []
  
    current = currentcode(x_range, y_range)
    xvalues.append(current[0])
    yvalues.append(current[1])
    fvalues.append(value(current, function))
    
    
    Temperature = value(current, function)*0.2
    while Temperature > 0.00000006: #this loop works unless the temperature becomes very small
        for i in range (100): #this loop ensures that there are 100 iterations over each temperature value
            #Temperature = Temperature*0.8
            #if Temperature <= 0.0000005:
                #return current 
            next = nextnode(current, step, x_range, y_range)
            E = value(next, function) - value(current, function)
            if minormax == 1:
                if E > 0:
                    current = next
                    fvalues.append(value(current, function))
                    xvalues.append(float(current[0]))
                    yvalues.append(float(current[1]))
                    
                else:
                    P = math.exp(E/Temperature)
                    randomno = random.uniform(0,1)
                    if randomno < P:
                        current = next
                        fvalues.append(value(current, function))
                        xvalues.append(float(current[0]))
                        yvalues.append(float(current[1]))
        
                    else:
                        continue
            elif minormax == 0:
                if E < 0:
                    current = next
                    fvalues.append(value(current, function))
                    xvalues.append(float(current[0]))
                    yvalues.append(float(current[1]))
                else:
                    P = math.exp(-E/Temperature)
                    randomno = random.uniform(0,1)
                    if randomno < P:
                        current = next
                        fvalues.append(value(current, function))
                        xvalues.append(float(current[0]))
                        yvalues.append(float(current[1]))
                    else:
                        continue

        Temperature = Temperature*0.8
    return value(current, function), xvalues, yvalues, fvalues
#val, x, y, f = simmulated_annealing((-5,5), (-5,5), 0.1, 1, "sphere")
#val, x, y, f = simmulated_annealing((-2,2), (-1,3), 1, 1, "rosenbrock")
#val, x, y, f = simmulated_annealing((-30,30), (-30,30), 1, 1, "griewank"))



def plotting (xvalues, yvalues, fvalues):

    func, axis = plt.subplots(2)

    axis[0].plot(fvalues, color='red', label="functionValue")
    axis[0].legend()
    axis[1].plot(xvalues, color='blue', label="x")
    axis[1].plot(yvalues, color='green', label="y")
    axis[1].legend()

    plt.show()

   
val, x, y, f = simmulated_annealing((-5,5), (-5,5), 0.01, 0, "sphere")
print(val, x, y, f)
plotting(x,y,f)

