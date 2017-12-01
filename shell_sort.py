# -*- coding: utf-8 -*-

def shell_sort(array):
    "希尔排序"
    n = len(array)
    # 初始步长
    gap = n/2
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and array[j - jap] > array[j]:
                array[j - jap], array[j] = array[j], array[j - gap]
                j -= gap
            gap = gap/2
if __name__ == '__main__':
    import numpy as np
    data_array = list(np.random.randint(-100, 100, size=10))
    print(data_array)
    print(shell_sort(data_array))
