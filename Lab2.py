# GROUP 9: Duy Luu, Kristine Nguyen, Nitya Prasad
# 2025SP-COMSC-077
# Lab 2
# This program aims to converts a floating-point number to its simplified floating-point representation or the IEEE 754 format discussed in the slides.


def convertFloatingPoint(x):
    #for the sign bit
    sign = 0 if x >=0 else 1
    x = abs(x)


#normallization
exponent = 0
while x >= 2.0:
        x /= 2.0
        exponent += 1
while x < 1.0:
        x *= 2.0
        exponent -= 1

#With bias 15
exponent_with_bias = exponent + 15 

 # The 8 bits (The significand/mantissa)
significand = x - 1  #removes the 1
mantissa_bits = []
for _ in range(8):
        significand *= 2
        bit = int(significand)
        mantissa.append(bit)
        significand -= bit


 #convert to binary 
exponent_bin = format(exponent_with_bias,)  # Convert exponent to 5-bit binary
mantissa = ''.join(map(str, mantissa_bits))  # Convert the mantissa list to a string of bits

    # Return the simplified floating-point representation
return x"{sign} | {exponent_bin} | {mantissa_bin}"








