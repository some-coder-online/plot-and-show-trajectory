from matplotlib import pyplot as plt
import math

def find_t(vi,th):

    theta = th * (math.pi/180)

    viy= ((math.sin(theta)*vi))
    t = viy/9.8

    return t

def show_vector(vi,theta,len_of_time):
    x_vals=[]
    y_vals=[]
    theta = theta*(math.pi/180)
    viy = vi*math.sin(theta)
    vix = vi*math.cos(theta)
    a = 9.8

    time = find_t(vi,30) / 50
    # d = vt + at^2
    temp_time = find_t(vi,30) / 50
    for i in range(1,len_of_time+1):

        d = viy*(time) - a*(time**2)
        y_vals.append(d)
        x_vals.append(time)
        time += temp_time
    plt.plot(x_vals,y_vals)
    plt.show

show_vector(100,30,50)









