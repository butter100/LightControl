# -*- coding: utf-8 -*-
import datetime
import time
import csv
import ctypes
import screen_brightness_control as sbc

consecutive_minute = 0

def set_monitor_contrast(contrast):
    hmonitor = ctypes.c_ulonglong()
    result = ctypes.windll.dxva2.SetMonitorContrast(hmonitor, contrast)
    if result == 0:
        raise ctypes.WinError()

while True:

    # Get the current time
    now = datetime.datetime.now()
    
    # Calculate the consecutive minute
    consecutive_minute = now.hour * 60 + now.minute
    # Print the consecutive minute
    time.sleep(5)
    with open('times.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
    set_monitor_contrast(sum(list(map(int, rows[consecutive_minute]))))
    sbc.set_brightness(sum(list(map(int, rows[consecutive_minute]))))
