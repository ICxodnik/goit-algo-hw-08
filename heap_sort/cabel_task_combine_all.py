import heapq

class MinHeap:
    def __init__(self, iterable=None):
        self._heap = []
        if iterable:
            self._heap = list(iterable)
            heapq.heapify(self._heap)

    def __repr__(self):
        return f"{self.to_sorted_list()}"

    def push(self, value):
        heapq.heappush(self._heap, value)

    def pop(self):
        return heapq.heappop(self._heap)

    def is_empty(self):
        return not self._heap

    def __len__(self):
        return len(self._heap)

    def to_sorted_list(self):
        return sorted(self._heap)

def min_connection_cost(cables_lengths):
    heap = MinHeap(cables_lengths)
    total_cost = 0

    while len(heap) > 1:
        first = heap.pop()
        second = heap.pop()
        combined = first + second
        total_cost += combined
        heap.push(combined)

    return total_cost

if __name__ == "__main__":
    cables_lengths = [12, 4, 13, 5, 6, 7, 11]
    print("Cумарна вартість з'єднання всіх кабелів:", min_connection_cost(cables_lengths))
