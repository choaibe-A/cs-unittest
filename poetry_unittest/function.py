from collections import Counter
from typing import Iterable

def frequency_sort(items):
    # Use Counter to count the frequency of each element
    item_counts = Counter(items)
    
    # Define a custom sorting key that sorts first by frequency (in reverse order)
    # and then by the original order of appearance
    def custom_sort_key(item):
        return (-item_counts[item], items.index(item))
    
    # Sort the items using the custom key
    sorted_items = sorted(items, key=custom_sort_key)
    
    return sorted_items

