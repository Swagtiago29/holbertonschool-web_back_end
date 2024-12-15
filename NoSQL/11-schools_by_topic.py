#!/usr/bin/env python3
"""
Module that contains schools_by_topic()
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    """
    a = mongo_collection.find({"topics": topic})
    return list(a)
