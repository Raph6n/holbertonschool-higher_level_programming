#!/usr/bin/python3
class VerboseList(list):
    """
    Custom list class that prints notifications on item addition or removal.
    """
    
    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        """
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and print a notification.
        """
        length_before = len(self)
        super().extend(iterable)
        length_after = len(self)
        added_items = length_after - length_before
        print(f"Extended the list with {added_items} items.")
    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a notification.
        """
        super().remove(item)
        print(f"Removed {item} from the list.")
    
    def pop(self, index=-1):
        """
        Remove and return an item at the given position in the list and print a notification.
        If no index is specified, remove and return the last item in the list.
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
