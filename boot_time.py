#!/usr/bin/env python
# encoding: utf-8

import datetime
import psutil

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

print boot_time
