# my_list = [None, False, 6, 0, 'a']
#
# for item in my_list:
#     print(item)
#
#
# my_list_iterator = iter(my_list)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)

import random
class MyIterator:

    def __init__(self, count=5):
        self.count = count

    def __iter__(self):
        self._count = self.count
        return self

    def __next__(self):
        self._count -= 1
        if self._count < 0:
            raise StopIteration
        return random.randint(1, 100)

my_iterator = MyIterator()
for item in MyIterator(): #iter(my_iterator):
    print(item) #item = next(my_iterator)