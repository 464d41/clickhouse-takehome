"""Package"""

import heapq
from functools import partial, reduce
from multiprocessing import Pool, cpu_count


class Item:
    """Item"""

    def __init__(self, line):
        self.url, self.val = line.split(" ")

    def __lt__(self, other):
        return int(self.val) < int(other.val)

    def __repr__(self):
        return f"{self.url} {self.val}"


class Topn:
    """Implements a class finding top N most valued URLs from a file"""

    def __init__(self, path):
        self.path = path

    def _chunkify(self, chunk_size=65536):
        with open(self.path, "r", encoding="utf-8") as fd:
            chunk = []
            for idx, line in enumerate(fd):
                if idx % chunk_size == 0 and idx > 0:
                    yield chunk
                    chunk = []
                chunk.append(line.rstrip())
                idx += 1
            yield chunk

    def _mapper(self, count, chunk):
        itemized = [Item(line) for line in chunk]
        heapq.heapify(itemized)
        top = heapq.nlargest(count, itemized)
        heapq.heapify(top)
        return top

    def _get_reducer(self, count):
        def reducer(a, b):
            merged = heapq.merge(a, b)
            top = heapq.nlargest(count, merged)
            heapq.heapify(top)
            return top

        return reducer

    def top(self, count):
        """Finds top N most valued URLs"""

        with Pool(processes=cpu_count()) as pool:
            mapped = pool.map(partial(self._mapper, count), self._chunkify())

        reduced = reduce(self._get_reducer(count), mapped)
        return sorted([item.url for item in reduced], reverse=True)
