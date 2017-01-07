#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
config = ConfigParser.ConfigParser()
with open('config.ini', 'r') as cfg_file:
    config.readfp(cfg_file)
    username = config.get('data', 'username')
    password = config.get('data', 'password')
    deck = config.get('data', 'deck', 'Default')

import requests


def getCookies():
    url = 'https://ankiweb.net/account/login'
    login_info = {'submitted': '1', 'username': username, 'password': password}
    r = requests.post(url, data=login_info)
    return r.cookies


def addCard(front):
    cookies = getCookies()
    url = 'https://ankiweb.net/edit/save'
    data = '[["%s",""],""]' % front
    save_info = {'data': data, 'mid': '1479215711126', 'deck': deck}
    r = requests.post(url, cookies=cookies, data=save_info)
    if r.text != '1':
        raise Exception('error: %s' % r.text)
if __name__ == '__main__':
    addCard('bigzhu test for you')
