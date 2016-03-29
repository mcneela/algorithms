import algorithms.data_structures.heap

def heapsort(items):
    to_sort = Heap(items)
    for i in range(to_sort.heap_size - 1, 0, -1):
        copy = to_sort.heap[0]
        to_sort.heap[0] = to_sort.heap[i]
        to_sort.heap[i] = copy
        to_sort.heap_size -= 1
        to_sort.heapify(0)
    return to_sort.heap
