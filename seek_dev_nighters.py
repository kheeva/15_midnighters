#!/usr/bin/env python
from datetime import datetime
import requests
import pytz


def download_attempts_page_json(page_number):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    payload = {'page': page_number}
    return requests.get(url, params=payload).json()


def load_attempts(pages):
    for page in range(1, pages):
        yield download_attempts_page_json(page)['records']


def get_midnighters(attempts):
    owl_time = range(6)
    night_attempts = filter(lambda x: datetime.fromtimestamp(
                                        x['timestamp'],
                                        pytz.timezone(x['timezone'])
                                    ).hour in owl_time,
                            attempts)
    return {username['username'] for username in night_attempts}


if __name__ == '__main__':
    midnighters = set()
    start_page = 1
    number_of_pages = download_attempts_page_json(start_page)['number_of_pages']
    attempts_pages = load_attempts(number_of_pages)
    for page in attempts_pages:
        midnighters = midnighters.union(get_midnighters(page))

    print('There are the users who turned out at a task at night:')
    for username in midnighters:
        print(username)