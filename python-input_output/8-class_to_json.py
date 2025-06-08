#!/usr/bin/python3
"""Return dict description of obj for JSON serialization."""
import json


def class_to_json(obj):
    """Return obj attributes as dict."""
    return obj.__dict__
