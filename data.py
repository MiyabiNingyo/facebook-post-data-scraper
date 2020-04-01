#!/usr/bin/env python3

import requests
import json
import sys
from urllib.parse import urlencode


def getPageAccessToke():
    with open('page_access_token') as f:
        return f.readline()


def getFeed(url, page_id, fields, page_access_token):
    posts = []
    fields = ['id', 'is_hidden', 'is_popular']
    query = {
        'fields': fields,
        'access_token': page_access_token
    }
    processing = True
    url = "%s/%s/feed?%s" % (url, page_id, urlencode(query))
    while processing:
        r = requests.get(url)
        try:
            posts = posts + r.json()['data']
        except:
            print(r.text)
            sys.exit(1)
        if 'paging' in r.json() and 'next' in r.json()['paging']:
            url = r.json()['paging']['next']
        else:
            processing = False
    return(posts)


def getAnalytics(url, post, metrics, page_access_token):
    query = {
        'metric': metrics,
        'access_token': page_access_token
    }
    r = requests.get("%s/%s/insights?%s" % (url, post['id'], urlencode(query)))
    output_metrics = {}
    try:
        data = r.json()['data']
    except:
        print(r.text)
        sys.exit(1)
    for metric in data:
        output_metrics[metric['name']] = metric['values'][0]['value']
    return output_metrics


def getAllAnalytics(url, posts, metrics, page_access_token):
    output = []
    for post in posts:
        post['data'] = getAnalytics(url, post, metrics, page_access_token)
        output.append(post)
    return output


def printAsCsv(data):
    csv_seperator = ";"
    header = []
    for key, value in data[0].items():
        if key == 'data':
            for key, value in value.items():
                header.append(key)
        else:
            header.append(key)
    print(*header, sep=csv_seperator)
    for post in data:
        line = []
        for key, value in post.items():
            if key == 'data':
                for key, value in value.items():
                    line.append(value)
            else:
                line.append(value)
        print(*line, sep=csv_seperator)

url = "https://graph.facebook.com/v6.0"
page_access_token = getPageAccessToke()

page_id = "an_id"
# https://developers.facebook.com/docs/graph-api/reference/v6.0/page/feed#readfields
fields = ['id', 'is_hidden', 'is_popular']
# https://developers.facebook.com/docs/graph-api/reference/v6.0/insights#page-post-engagement
metrics = ['post_engaged_users', 'post_negative_feedback']

posts = getFeed(url, page_id, fields, page_access_token)

data = getAllAnalytics(url, posts, metrics, page_access_token)

printAsCsv(data)
