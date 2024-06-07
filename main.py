from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram.enums import ChatAction
import requests
import random
from random import choice
import os
import re
import asyncio
import time
from datetime import datetime
from pyrogram import enums
API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME","") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL","ARTIST_i_NETWORK")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","JAYSHRI_RAM_JAYSHRI_RAM")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP","linkxyyx")
BOT_NAME = os.environ.get("BOT_NAME","CHATBOT")
START_IMG = os.environ.get("START_IMG","")
