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

def took_cables(cables_lengths, required_length):
    heap = MinHeap(cables_lengths)
    total_cost = 0
    used_cables = []

    while not heap.is_empty() and total_cost < required_length:
        cable = heap.pop()
        total_cost += cable
        used_cables.append(cable)
    remaining = heap.to_sorted_list()
    return total_cost, remaining

if __name__ == "__main__":
    cables_lengths = [12, 4, 13, 5, 6, 7, 11]
    length_to_take = 40

    sorted_cables = MinHeap(cables_lengths)
    print("Відсортований масив:", sorted_cables)
    
    cost, cables_left = took_cables(cables_lengths, length_to_take)
    print("Мінімальна сумарна вартість з'єднання кабелів:", cost)
    print("Кабелі, що лишились:", cables_left)

