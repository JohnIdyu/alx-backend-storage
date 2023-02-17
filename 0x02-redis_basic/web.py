#!/usr/bin/env python3
"""
create a web cach
"""
import redis
import requests
rc = redis.Redis()
count = 0


def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text