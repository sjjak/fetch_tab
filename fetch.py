#!/usr/bin/python2.7
import dbus

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from BeautifulSoup import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd

session_bus = dbus.SessionBus()

spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")
metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

# The property Metadata behaves like a python dict
for key, value in metadata.items():
    print key, value

options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
string = "https://www.ultimate-guitar.com/search.php?title=" + metadata['xesam:title']
driver.get(string)
