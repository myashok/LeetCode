class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq = defaultdict(int)
        self.r_freq = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.r_freq[self.freq[val]].append(val)

    def pop(self) -> int:
        x = self.r_freq[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.r_freq[self.max_freq]:
            self.max_freq -= 1
        return x

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
