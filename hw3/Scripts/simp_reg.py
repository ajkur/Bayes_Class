from numpy import arange,array,ones,linalg
import hw3_data

data_x, data_y = hw3_data.evap()
# print data_y
print data_x
w = linalg.lstsq(data_x,data_y)[0] # obtaining the parameters
print w
