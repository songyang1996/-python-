# -*- coding: utf-8 -*-

def quick_sort(array, l=0, r=len(array)-1):
    "快速排序"
    if l >= r:
        return
    flag = l
    for temp in range(l+1, r+1):
        if array[flag] > array[temp]:  # 如果数字小于基准， 则把此数字放在基准左侧
            array.insert(flag, array.pop(temp))
            flag += 1
    quick_sort(array, l, flag-1)
    quick_sort(array, flag+1, r)



if __name__ == '__main__':
    # array = [1,-2,4,7,6,3,2,3]
    import numpy as np
    array = list(np.random.randint(-1000, 1000, size=10))
    print(array)
    quick_sort(array)
    print(array)
