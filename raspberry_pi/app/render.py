#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'images')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def render_file(file_name):
    try:
        logging.info("Starting rendering...")
        epd = epd7in5_V2.EPD()
    
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        logging.info("Reading file..")
        Himage = Image.open(file_name)
#        Himage = Image.open(os.path.join(picdir, 'latest.jpeg'))
        epd.display(epd.getbuffer(Himage))
        time.sleep(2)

        logging.info("Goto Sleep...")
        epd.sleep()
    
    except IOError as e:
        logging.info(e)
    
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == "__main__":
    render_file(sys.argv[1])
