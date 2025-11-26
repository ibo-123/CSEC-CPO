class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
        else:
            if len(self.stream) > 0:
                self.stream.append(num*self.stream[-1])
            else:
                self.stream.append(num)
        return self.stream
    def getProduct(self, k: int) -> int:
        if k >=len(self.stream):
            return 0

        nums = self.stream[-1]//self.stream[-k-1]
        return nums
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
