from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.hash_map = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_map:
            return False
        #  update self.hash_map
        self.hash_map[val] = len(self.arr)
        #  update self.arr
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash_map:
            return False
        idx = self.hash_map[val]
        last = self.arr[-1]
        #  update self.arr
        self.arr[idx] = last
        self.arr.pop()
        #  update self.hash_map
        self.hash_map[last] = idx
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)
        


#  Your RandomizedSet object will be instantiated and called as such:
#  obj = RandomizedSet()
#  param_1 = obj.insert(val)
#  param_2 = obj.remove(val)
#  param_3 = obj.getRandom()