#!/usr/bin/python3
'''Defines a CountedIterator class.'''


class CountedIterator:
    '''Iterator that counts how many items were fetched.'''

    def __init__(self, iterable):
        '''Initialize iterator and counter.'''
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        '''Return next item and update counter.'''
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        '''Return number of fetched items.'''
        return self.count

    def __iter__(self):
        '''Return self as iterator.'''
        return self

