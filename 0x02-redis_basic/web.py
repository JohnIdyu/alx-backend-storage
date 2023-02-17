#!/usr/bin/env python3
"""
create a web cache
"""
import redis
import requests
rc = redis.Redis()

def get_page(url: str) -> str:
    """ get a page and cache value"""
    try:
        cached_value = rc.incr(f"cached:{url}")
    except redis.exceptions.RedisError as e:
        print(f"Error incrementing cache value: {e}")
        cached_value = 0
    else:
        if cached_value == 1:
            rc.expire(f"cached:{url}", 10)

            try:
                resp = requests.get(url)
                rc.setex(f"page:{url}", 10, resp.text)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching page: {e}")
                resp = ""

                return resp.text


            if __name__ == "__main__":
                urls = [
                        'http://slowwly.robertomurray.co.uk',
                        'http://example.com',
                        'http://google.com',


                        for url in urls:
                        print(get_page(url))
