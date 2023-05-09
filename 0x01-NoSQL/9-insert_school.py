#!/usr/bin/env python3

"""
The module defines the function insert_school
"""

def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    Returns the new _id
    """

    if len(kwargs) == 0:
        return None
    result = mongo_collection.insert(kwargs)
    return result.new_id
