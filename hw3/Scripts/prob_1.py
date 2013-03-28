import numpy as np
import math as m

def p_y(n,y,M):
    t_1 = m.exp(-0.5*n*y**2)
    t_2 = m.erf((0.5*n)**(0.5)*(y-0.5*M)) 
    t_3 = m.erf((0.5*n)**(0.5)*(y+0.5*M))
    m_f1 = (n/(8*m.pi))**2
    m_f2 = (n/(2*m.pi))**2/M
    return m_f1*(t_1 - m_f2*(t_2 - t_3))

m_var = 'y'

if m_var == 'n':
    # Changing n
    y = 0
    M = 10
    M0 = p_y(100,y,M)
    M1 = p_y(10,y,M)
    M2 = p_y(1,y,M)
if m_var == 'y':
    # Changing y
    n = 10
    M = 10
    M0 = p_y(n,5.1,M)
    M1 = p_y(n,1,M)
    M2 = p_y(n,5,M)
if m_var == 'M':
    # Changing M
    y = 0
    n = 100
    M0 = p_y(n,y,.1)
    M1 = p_y(n,y,10)
    M2 = p_y(n,y,100)


BF01 = M0/M1
BF12 = M1/M2
BF02 = M0/M2

print BF01
print BF12
print BF02
