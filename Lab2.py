# GROUP 9: Duy Luu, Kristine Nguyen, Nitya Prasad
# 2025SP-COMSC-077
# Lab 2
# This program aims to converts a floating-point number to its simplified floating-point representation or the IEEE 754 format discussed in the slides.

import struct

def convertFloatingPoint(FP_num):
    sign = 0 if FP_num >=0 else 1
    FP_num = abs(FP_num)
