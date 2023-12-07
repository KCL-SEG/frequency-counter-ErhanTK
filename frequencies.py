"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        # Convert item to string
        key = str(item)
        # Increment the count for this key in the dictionary
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1
    return frequencies

