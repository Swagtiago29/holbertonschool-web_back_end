#!/usr/bin/env python3
"""
Module containing the function update_topics()
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    """
    a = mongo_collection.update_many(
    {"name": name},
    {"$set": {"topics": topics}}
    )
    return a.modified_count