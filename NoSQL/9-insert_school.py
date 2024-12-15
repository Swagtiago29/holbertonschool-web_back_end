#!/usr/bin/env python3

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the given MongoDB collection based on provided keyword arguments.
    """
    ins = mongo_collection.insert_one(kwargs)
    return ins.inserted_id
