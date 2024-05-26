class CountedIterator:
    """
    Custom iterator that counts the number of items iterated over.
    """
    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator, incrementing the counter.
        Raise StopIteration when the iterator is exhausted.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Return the number of items that have been iterated over.
        """
        return self.count
