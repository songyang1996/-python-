# -*- coding: utf-8 -*-
# 时间复杂度 最好O(n^2) 最坏O(n^2)
def select_sort(array):
    "选择排序"
    import copy
    array = copy.copy(array)
    for j in range(len(array)):
        cur = j
        for i in range(j+1, len(array)):
            if array[cur] > array[i]:
                cur = i
        array[cur], array[j] = array[j], array[cur]
    return array



if __name__ == '__main__':
    import numpy as np
    array = list(np.random.randint(-100, 100, size=10))
    print(array)
    print(select_sort(array))
