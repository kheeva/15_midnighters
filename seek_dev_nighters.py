#!/usr/bin/env python
import requests


def download_attempts_page_json(page_number):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    payload = {'page': page_number}
    return requests.get(url, params=payload).json()


def load_attempts(pages):
    for page in range(1, pages):
        yield download_attempts_page_json(page)['records']


def get_midnighters():
    pass


if __name__ == '__main__':
  start_page = 1
  number_of_pages = download_attempts_page_json(start_page)['number_of_pages']
  attempts_list = load_attempts(number_of_pages)
  print(next(attempts_list))