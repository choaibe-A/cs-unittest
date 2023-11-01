"""
This module contains functions for sorting items by frequency.
"""
from collections import Counter

def frequency_sort(items):
    """
    Sorts a list of items by their frequency and original order of appearance.

    :param items: A list of items to be sorted.
    :return: A list of items sorted by frequency.
    """
    # Use Counter to count the frequency of each element
    item_counts = Counter(items)
    # Define a custom sorting key that sorts first by frequency (in reverse order)
    # and then by the original order of appearance
    def custom_sort_key(item):
        return (-item_counts[item], items.index(item))
    # Sort the items using the custom key
    sorted_items = sorted(items,key=custom_sort_key)
    return sorted_items

frequency_sort(1)
