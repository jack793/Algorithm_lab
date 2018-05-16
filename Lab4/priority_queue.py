import heapq


class PriorityQueue:
    def __init__(self, heap):
        self.heap = heap
        heapq.heapify(self.heap)

    # for iterating inter obj
    def __iter__(self):
        return iter(self.heap)

    def get_heap(self):
        return self.heap

    def extract_min(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
