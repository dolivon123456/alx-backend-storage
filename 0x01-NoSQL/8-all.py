#!/usr/bin/env python3

"""
The module defines the function list_all
"""

def list_all(mongo_collection):
    """
    lists all documents in a collection
    Return an empty list if no document in the collection
    """

    if not mongo_collection:
        return []
    return mongo_collection.find()
