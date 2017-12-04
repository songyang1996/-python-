# -*- coding: utf-8 -*-
# 优化了最好情况的算法
# 浅拷贝原对象 以防止原数组变化
# 时间复杂度 最好O(n), 最坏O(n^2)

def bubble_sort(array):
    "冒泡排序"
    import copy
    array = copy.copy(array)
    count = 0
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                count += 1
        if count == 0:
            # 最好情况
            break
    print(count)
    return array

if __name__ == '__main__':
    import numpy as np
    array = list(np.random.randint(-100, 100, size=10))
    print(array)
    print(bubble_sort(array))
