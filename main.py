from OTXv2 import OTXv2
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
import requests
# from pymisp import PyMISP
import time

otx_key = 'e66c26fe67aad476e00452f341ce9a77c6de100927da5bdf2a0a1414e58f4f28'


def readTimestamp():
    fname = "timestamp"
    f = open(fname, "r")
    mtimestamp = f.read()
    f.close()
    return mtimestamp

def getTagList():
    fname = "tags"
    f = open(fname, "r")
    lines = f.readlines()
    tags = [i.strip() for i in lines]
    f.close()
    return tags

if __name__ == "__main__":

    otx = OTXv2(otx_key)

    mtime = readTimestamp()
    pulses = otx.getsince(mtime)
    print("Retrived %d pulses" % len(pulses))

    tags = getTagList()

    for p in pulses:
        for t in p['tags']:
            if t in tags:
                print(p['modified'])
                print(p['name'])
                print(p['author_name'])
                print(p['description'])
                print(len(p['indicators']))
                for i in p['indicators']:
                    print(i['indicator'])
                    print(i['type'])
                print('=' * 12)
                break