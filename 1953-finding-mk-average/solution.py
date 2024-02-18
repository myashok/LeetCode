from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.middleSum = 0
        self.queue = deque()
        self.sortedValues = SortedList()
        self.m = m
        self.k = k  
        self.segment_size = m - (2 * k)

    def addElement(self, num: int) -> None:
        if len(self.queue) < self.m: 
            self.queue.append(num)
            self.sortedValues.add(num)
            if len(self.queue) == self.m:
                self.middleSum = sum(self.sortedValues[self.k:-self.k])
            return
        
        remove_val = self.queue.popleft()
        removal_idx = self.sortedValues.bisect_left(remove_val)

        if removal_idx < self.k:
            self.middleSum -= self.sortedValues[self.k]
            self.middleSum += self.sortedValues[self.m - self.k]
        elif self.k <= removal_idx < self.m - self.k:
            self.middleSum -= remove_val
            self.middleSum += self.sortedValues[self.m - self.k]
        
        self.sortedValues.remove(remove_val)
        
        self.queue.append(num)
        
        insertion_idx = self.sortedValues.bisect_left(num)
        if insertion_idx < self.k:
            self.middleSum += self.sortedValues[self.k - 1]
            self.middleSum -= self.sortedValues[self.m - self.k - 1]
        elif self.k <= insertion_idx < self.m - self.k:
            self.middleSum += num
            self.middleSum -= self.sortedValues[self.m - self.k - 1]
            
        self.sortedValues.add(num)       

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        return self.middleSum // self.segment_size

