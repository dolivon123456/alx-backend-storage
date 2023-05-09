#!/usr/bin/env python3

"""
The module defines the function update_topics
"""

def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """

    if mongo_collection is None:
        return None
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
