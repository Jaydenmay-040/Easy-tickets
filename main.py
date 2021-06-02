# Challenge1
import numpy as np
list_of_numbers = np.arange(20)
print("Array:", list_of_numbers)
mean = np.mean(list_of_numbers)
print("Mean:", mean)
std_list = np.std(list_of_numbers)
print("Standard Deviation:", std_list)
variance = np.var(list_of_numbers)
print("Variance:", variance, "\n", "\n")

# Challenge2
import matplotlib.pyplot as plt
import numpy as np
nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
a = np.histogram(nums, bins)
print("nums: " + str(nums))
print("bins: " + str(bins))
print(a)
plt.hist(nums, bins)
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Histogram of nums against bins")
plt.show()
