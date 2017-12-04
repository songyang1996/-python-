# -*- coding: utf-8 -*-
# 时间复杂度和步长相关 大概为O(nlogn)
# 恶性bug  写完变成了死循环
def shell_sort(array):
    "希尔排序"
    import copy
    array = copy.copy(array)
    n = len(array)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 插入排序
            while(i-gap) >= 1:
                if array[i] < array[i-gap]:
                    array[i], array[i-gap] = array[i-gap], array[i]
                i -= gap
        gap //= 2
    return array

if __name__ == '__main__':
    import numpy as np
    data_array = list(np.random.randint(-100, 100, size=8))
    print(data_array)
    print(shell_sort(data_array))
