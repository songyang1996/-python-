# -*- coding: utf-8 -*-
import random
def insert_sort(array):
    "插入排序"
    loop_count = 0
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            temp = array[i]     # 当前需要排序的元素
            index = i           # 用来记录排序元素需要插入的位置
            while index > 0 and array[index - 1] > temp:
                array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            array[index] = temp # 把需要排序的元素，插入到指定位置
    return array

if __name__ == '__main__':
    import numpy as np
    data_array = list(np.random.randint(-100, 100, size=10))
    print(data_array)
    print(insert_sort(data_array))
