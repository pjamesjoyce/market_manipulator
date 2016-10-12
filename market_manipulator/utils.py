"""Utility functions for use in market manipulation"""

def get_dataset_by_id(activity_id, data):
    """get the dataset specified by an activity id from a database"""
    
    dataset = [i for i in data if i['id'] == activity_id][0]
    return dataset

def get_dataset_by_code(activity_code, data):
    """get the dataset specified by an activity id from a database"""
    
    dataset = [i for i in data if i['code'] == activity_code][0]
    return dataset

