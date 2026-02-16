import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
average_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", average_fahrenheit)


print("\n----------------------\n")

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
print("Range:", np.max(scores) - np.min(scores))


print("\n----------------------\n")


numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

start_numpy = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start_numpy

start_python = time.time()
python_sum = sum(python_list)
python_time = time.time() - start_python

speed = round(python_time / numpy_time, 1)

print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print("NumPy time:", format(numpy_time, ".4f"), "seconds")
print("Python time:", format(python_time, ".4f"), "seconds")
print("NumPy is", speed, "x faster")
