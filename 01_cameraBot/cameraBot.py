#!/usr/bin/env python
#coding:utf-8

import time
import subprocess
import twython

from PIL import Image

IMG_WIDTH = "2592"
IMG_HEIGHT = "1944"
IMG_NAME = "spot.jpg"

CONSUMER_KEY      = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET   = 'YOUR_CONSUMER_SECRET'
ACCESS_KEY      = 'YOUR_ACCESS_KEY'
ACCESS_SECRET   = 'YOUR_ACCESS_SECRET'
api = twython.Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

snapCommand = "raspistill -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT + " -o " + IMG_NAME

now = time.ctime()
parsed = time.strptime(now)
tweetTime = time.strftime("%Y %b %d (%a) %H:%M:%S ", parsed)

ret = subprocess.call(snapCommand, shell=True)
photo = open(IMG_NAME, 'rb')

media_status = api.upload_media(media=photo)

api.update_status(media_ids=[media_status['media_id']], status='テスト投稿だす．'+str(tweetTime)+'')
