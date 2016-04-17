import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

def ode_system(y,t,a,b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1 + y0*y1)]
    return dydt

if __name__ == "__main__":

    # --------------------------PART 1---------------------------------------
    # initial value for y0 and y1 
    # value for a and b
    a = 1.0
    b = 0.2
    y0_initial = 0.1
    y1_initial = 1.0
    y_initial = [y0_initial,y1_initial]
    
    # partitioning the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    #solve the nonlinear ODE system
    sol = spIn.odeint(ode_system,y_initial,t,args=(a,b))

    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'g', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator y1 against t')
    plt.title('y against t with y0_initial = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'g', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with y0_initial = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.show()
    

    # -----------------------PART 2 -----------------------------------
    # initial value for y0 and y1 and the value for a and b
    a = 1.0
    b = 0.2
    # different initial value for initial_y0
    y0_initial = 0.11
    y1_initial = 1.0
    y_initial = [y0_initial,y1_initial]
    
    # partitioning the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode_system,y_initial,t,args=(a,b))

    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'g', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator y1 against t')
    plt.title('y against t with y0_initial = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'g', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with y0_initial = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.show()