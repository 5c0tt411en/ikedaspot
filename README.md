# IKEDASPOT project
IKEDA SPOT Raspberry Pi BOT Project.

## Requirements

- Raspberry Pi Model B (or later)
- Picamera
- Wi-fi dongle

## 概要
Wi-fi環境で動く，TwitterBOT．  
いずれは外でスタンドアローンでしばらく景色を撮り続けるものにする．  
cameraBot.pyをアップデートなどして更新していく．

## Wi-fi
### wpa_supplicant
directory path : /etc/wpa_supplicant/

#### wpa_supplicant.conf
SSID，passを入力する．

### sshしたくてip固定したいとき
directory path : /etc/network/interfaces

#### interfaces
xxx.xxx.xxx.xxx　の部分に入力し固定する．

## TwitterBOT
### 01_cameraBot
directory path : ~/programs

#### cameraBot.py
YOUR_CONSUMER_KEY，YOUR_CONSUMER_SECRET，YOUR_ACCESS_KEY，YOUR_ACCESS_SECRETに自身のTwitterアプリの情報を入れる．

## 時間管理
### cron
設定Command :

    crontab -e

#### botの動作を開始する

    # */5 * * * * python /home/pi/programs/01_cameraBot/cameraBot.py

の # を消す．5というのは5分おきにcameraBot.pyを動作させるということ．


## Copy right
Copyright 2013-, Scott Allen([scottallen.ws](http://scottallen.ws)).  
Twitter:[@Scott_Allen__](https://twitter.com/#!/Scott_Allen__ "twitter@Scott_Allen__").

