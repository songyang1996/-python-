# -*- coding: utf-8 -*-
# 时间复杂度 最好O(n) 最坏O(n^2)

def insert_sort(array):
    "插入排序"
    import copy
    array = copy.copy(array)
    for i in range(1, len(array)):
        # 从下标一位置取数据 和前面的有序数据倒叙比较
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

if __name__ == '__main__':
    import numpy as np
    data_array = list(np.random.randint(-100, 100, size=10))
    print(data_array)
    print(insert_sort(data_array))
