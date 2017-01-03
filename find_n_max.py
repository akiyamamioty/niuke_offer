# -*- coding:utf-8 -*-

def parent(i):
    return (i-1)/2
 
def left(i):
    return 2*i+1
  
def right(i):
    return 2*i+2
  
def min_heap(heap, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and heap[l] < heap[i]:
        min_node =  l
    else:
        min_node = i
    if r < heap_size and heap[r] < heap[min_node]:
        min_node = r
    if min_node != i:
        temp = heap[i]
        heap[i] = heap[min_node]
        heap[min_node] = temp
        min_heap(heap, min_node, heap_size)

def built_min_heap(init_heap, heap_size):
    for i in range(heap_size/2, 0, -1):
        min_heap(init_heap, i, heap_size)
 
def find_max_n(array, heap_size):
    heap = array[0:heap_size]
    built_min_heap(heap,heap_size)
    for i in range(heap_size, len(array)):
        if array[i] > heap[0]:
            heap[0] = array[i]
            min_heap(heap, 0, heap_size)
    for i in range(len(heap)):
        print heap[i], 
 
if __name__ == '__main__':
    input_list = [1,2,3,4,5,6,7,111,8,9,12,123,1]
    heap_size = 3
    find_max_n(input_list,heap_size)

