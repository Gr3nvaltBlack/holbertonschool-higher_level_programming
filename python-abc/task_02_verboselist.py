#!/usr/bin/python3
'''Defines a class VerboseList that extends list.'''


class VerboseList(list):
    '''List subclass that prints messages on modification.'''

    def append(self, item):
        '''Add item and print a message.'''
        super().append(item)
        print(f'Added [{item}] to the list.')

    def extend(self, iterable):
        '''Add multiple items and print a message.'''
        count = len(iterable)
        super().extend(iterable)
        print(f'Extended the list with [{count}] items.')

    def remove(self, item):
        '''Print message before removing item.'''
        print(f'Removed [{item}] from the list.')
        super().remove(item)

    def pop(self, index=-1):
        '''Print message before popping item.'''
        item = self[index]
        print(f'Popped [{item}] from the list.')
        return super().pop(index)

