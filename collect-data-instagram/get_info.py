import argparse
import os
import sys
import csv
from instabot import Bot, utils

## Bot() adalah library bot dari github berikut "bla bla bla"
bot = Bot()
bot.login(username="akuncobacoba123123", password="akuncobacoba123")

## username yang akan diambil datanya
target_username = "ruthhstefanie"

## menggunakan library Bot() untuk mengambil user_id, dimana user_id adalah berupa beberapa digit, 
## yang immutable (tidak akan berubah) di database instagram
user_id = bot.get_user_id_from_username(target_username)
## mengambil jumlah total following menggunakan library Bot()
following = bot.api.get_total_followers_or_followings(user_id=user_id, usernames=True, which="followings")

## Setelah mendapatkan following, kita akan secara rekursif mengambil lagi data setiap following tersebut
for user in following[:3]:
    
    username = user['username']
    full_name = user['full_name']
    user_id_ = bot.get_user_id_from_username(username)
    data = bot.api.get_user_followings(user_id = user_id_)
    print(data)




"""
    kalau user yang private tidak bisa diextract datanya
    tapi accountnya bisa follow dulu (kayaknya)
    """


