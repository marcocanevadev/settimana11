"""
define sorted list with no duplicates
"""
class SortedSet(list):
    def __init__(self,iterable):
      #  iterable = set(iterable)
        super().__init__(set(iterable))
       # self = set(self)
    def insert(self, value):
       # print(self)
        if value not in self:
            self.append(value)
            self = sorted(set(self))
            return self
          #  _index = [i for x,i in self if x < value]
           # super().insert(_index,value)
            
    def append(self, value):
        return SortedSet.insert(self,value)

if __name__ == '__main__':
    l = [2,1,8,5,3,1,1]
    print(SortedSet(l))
    print(SortedSet.insert(l,4))
    print(SortedSet.append(l,7))

    list