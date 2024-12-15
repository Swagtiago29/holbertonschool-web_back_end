#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    a = mongo_collection.find({"topic": topic})
    return a