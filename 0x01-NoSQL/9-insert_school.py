#!/usr/bin/env python3

"""
The module defines the function insert_school
"""

def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    Returns the new _id
    """

     if mongo_collection is None or kwargs == {} or kwargs is None:
        return
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
