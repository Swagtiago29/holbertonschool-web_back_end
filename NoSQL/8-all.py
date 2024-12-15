#!/usr/bin/env python3
"""
    Module with the function list_all
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.
    """
    all_docs = list(mongo_collection.find())
    return all_docs
