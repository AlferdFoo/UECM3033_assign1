import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sin(x)*(4*sy.cos(x))*sy.exp(2*(sy.cos(x))+1), (x, 0, (sy.pi)/2))
    return ans

def my_solution():
    A = np.array([[3,2,0,0,0,0,0,0,0,0], [5,0,0,0,1,0,0,0,0,0], [0,1,10,0,0,0,0,0,0,0], [0,0,9,0,0,8,0,0,0,0], [0,0,0,3,6,0,0,0,0,0],
                  [0,0,0,4,0,0,0,8,0,0], [0,0,0,0,0,2,0,0,0,1], [0,0,0,0,0,0,4,0,5,0], [0,0,0,0,0,0,10,0,0,2], [0,0,0,0,0,0,0,7,9,0]])
    b = np.array([7,10,32,75,42,80,22,73,90,137])
    x = np.linalg.solve(A,b) #Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1300981
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
