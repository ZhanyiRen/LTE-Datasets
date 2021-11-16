# -*-coding:utf-8-*-
# !/usr/bin/env python
# @Time    : 2021/11/16 15:35
# @File    : get_data_urls.py
from tensorbay import GAS
from tensorbay.dataset import Dataset

# Authorize a GAS client.
gas = GAS('XXXX')  # please email ren12852@stu.xjtu.eddu.cn for Accesskey

# Get a dataset.
dataset = Dataset("LTE_Dataset", gas)

# List dataset segments.
segments = dataset.keys()

# Enumerate each segment to get the data_url.
urls = dict()  # dictionary of the data_urls
for index, segment in enumerate(segments):

    url = dataset[segment][0].get_url()
    urls[segment] = url
