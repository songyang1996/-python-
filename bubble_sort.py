#coding:utf-8
import random
def bubble_sort(data_array):
    "冒泡排序"
    loop_count = 0
    for j in range(len(data_array)):
        for i in range(j+1, len(data_array)):
            if data_array[j] > data_array[i]:
                data_array[j], data_array[i] = data_array[i], data_array[j]
            loop_count += 1

    return (data_array, loop_count)

if __name__ == '__main__':
    import numpy as np
    data_array = list(np.random.randint(-100, 100, size=10))
    print(data_array)
    print(bubble_sort(data_array))
