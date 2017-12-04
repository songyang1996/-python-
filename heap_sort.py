# -*- coding: utf-8 -*-
# 施工中

def heap_sort():
    "堆排序"
    pass

# class Tree(object):
#     def __init__(self, array):
#         self.deep = len(array)
def sift_down(array, node, end):
    root = node
    while True:
        # 调整为最大堆
        child = 2 * root - 1  # 左节点
        if child > end:
            break
        print("v:", root, array[root], child, array[child])
        print(array)
        # 找出两个子节点中较大的 并设置右边的大
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        # 如果最大堆小于较大的child 则交换顺序
        if array[root] < arr[child]:
            array[root], array[child] = array[child], array[root]

if __name__ == '__main__':
    heap_sort()
