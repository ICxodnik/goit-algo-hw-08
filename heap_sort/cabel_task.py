import heapq

class MaxHeap:
    def __init__(self, iterable=None):
        self._heap = []
        if iterable:
            self._heap = [-x for x in iterable]
            heapq.heapify(self._heap)
    
    def __repr__(self):
        return f"{self.to_sorted_list()}"

    def push(self, value):
        heapq.heappush(self._heap, -value)

    def pop(self):
        return -heapq.heappop(self._heap)

    def is_empty(self):
        return not self._heap

    def to_sorted_list(self):
        return sorted([-x for x in self._heap], reverse=True)

    def sort_desc(iterable):
        return MaxHeap(iterable).to_sorted_list()

def took_cables(cables_lengths, required_length):
    total = 0
    heap = MaxHeap(cables_lengths)
    used_cables = []

    while not heap.is_empty() and total < required_length:
        cable = heap.pop()
        total += cable
        used_cables.append(cable)

    remaining = heap.to_sorted_list()
    return total, remaining

if __name__ == "__main__":
    cables_lengths = [12, 4, 13, 5, 6, 7, 11]
    sorted_cables = MaxHeap(cables_lengths)
    print("Відсортований масив (за спаданням):", sorted_cables)

    length_to_take = 40
    cost, cables_left = took_cables(cables_lengths, length_to_take)
    print("Сумарна довжина кабелів, що використані:", cost)
    print("Кабелі, що лишились:", cables_left)
