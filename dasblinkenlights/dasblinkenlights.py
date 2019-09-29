#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dasblinkenlights"""

import enum

class ProgressKind(enum.Enum):
    INFO = (0, 64, 64)
    DANGER = (64, 0 , 0)
    WARNING = (64, 64, 0)
    DEBUG = (64, 64, 64)
    SAFE = (0, 64, 0)
    MONITOR = (0, 0, 64)


def get_mote():
    import mote
    mote = mote.Mote()
    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)
    mote.clear()
    mote.show()
    return mote


def show_progress(percent, kind=ProgressKind.INFO):
    """displays progress on the motes."""
    # mote = get_mote()
    import mote
    mote = mote.Mote()
    mote.clear()
    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)
    print(percent)
    r,g,b = kind.value
    if percent == 100:
        for i in range(1, 5):
            for j in range(16):
                mote.set_pixel(i, j, r,g,b)
    elif 75 <= percent < 100:
        for i in range(1, 4):
            for j in range(16):
                mote.set_pixel(i, j, r,g,b)
        pixels = int(16*(percent-75)/25)
        for pixel in range(pixels):
            mote.set_pixel(4, pixel, r,g,b)
    elif 50 <= percent < 75:
        for i in range(1, 3):
            for j in range(16):
                mote.set_pixel(i, j, r,g,b)
        pixels = int(16*(percent-50)/25)
        for pixel in range(pixels):
            mote.set_pixel(3, pixel, r,g,b)
    elif 25 <= percent < 50:
        for i in range(1, 2):
            for j in range(16):
                mote.set_pixel(i, j, r,g,b)
        pixels = int(16*(percent-25)/25)
        # print(pixels)
        for pixel in range(pixels):
            mote.set_pixel(2, pixel, r,g,b)
    else:
        pixels = int(16*(percent)/25)
        # print(pixels)
        for pixel in range(pixels):
            mote.set_pixel(1, pixel, r,g,b)

    mote.show()
