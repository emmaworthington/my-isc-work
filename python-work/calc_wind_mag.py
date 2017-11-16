import numpy as np

def calc_wind_mag(u, v, noise_level):
    total = np.sqrt(u**2 + v**2)
    print 'Magnitude before noise level adjustment is\n', total

    condition = np.less(total, noise_level)
    result = np.where(condition, noise_level, total) 
  
    return result


test_u = np.array([[4, 5, 6], [2, 3, 4]])
test_v = np.array([[2, 2, 2], [1, 1, 1]])
print 'Result is', calc_wind_mag(test_u, test_v, 0.1)

test_u = np.array([[4, 5, 0.01], [2, 3, 4]])
test_v = np.array([[2, 2, 0.03], [1, 1, 1]])
print 'Result is', calc_wind_mag(test_u, test_v, 0.1)



