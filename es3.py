"""
define sorted list with no duplicates
"""
class SortedSet(list):
    def __init__(self,iterable):
      #  iterable = set(iterable)
        #super().__init__(set(iterable))
        self._items= sorted(set(iterable))
       # self = set(self)
    def insert(self, value):
      # print(self)
      if super().count(value)==0:
    
          self._items.append(value)
          self._items.sort()
      """
      if value not in self:
          print('inserting..')
          super().append(value)
          print('self: ',self)
          print('sorted', sorted(set(self)))
          #self = sorted(set(self))
          return sorted(set(self))
        #  _index = [i for x,i in self if x < value]
          # super().insert(_index,value)
      """
      return self._items
    def append(self, value):
        return SortedSet.insert(self,value)
    
    def extend(self, other):
        return set(other)
    
    def reverse(self):
        raise RuntimeError
    
    def indexAfter(self,value):
        print(type(self._items))
        print([v for x, v in self._items if x > value][0])


if __name__ == '__main__':
    """
    l = [2,1,8,5,3,1,1]
    print(SortedSet(l))
    print('\t',l)
    print(SortedSet.insert(l,4))
    print('\t',l)
    print(SortedSet.append(l,7))
    print('\t',l)
  """
    list = SortedSet([5,2,3,3,1])
    print(list)
   
    list.insert(0)
    list.append(6)
    print(list._items) 
    
    i = list.indexAfter(4)
    print(i)