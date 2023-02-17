#!/usr/bin/env python3
"""
create a web cach
"""
import redis
import requests
rc = redis.Redis()
count = 0


def get_page(http://slowwly.robertomurray.co.uk: str) -> str:
    """ get a page and cach value"""
    rc.set(f"cached:{http://slowwly.robertomurray.co.uk}", count)
    resp = requests.get(http://slowwly.robertomurray.co.uk)
    rc.incr(f"count:{http://slowwly.robertomurray.co.uk}")
    rc.setex(f"cached:{http://slowwly.robertomurray.co.uk}", 10, rc.get(f"cached:{http://slowwly.robertomurray.co.uk}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
