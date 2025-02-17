# GROUP 9: Duy Luu, Kristine Nguyen, Nitya Prasad
# 2025SP-COMSC-077
# Lab 2
# This program aims to converts a floating-point number to its simplified floating-point representation or the IEEE 754 format discussed in the slides.

def convertFloatingPoin(FP_num):
    # Identify the sign 0-> pos 1->neg
    sign = 0 if FP_num >= 0 else 1
    FP_num = abs(FP_num) 
    
    # Step 2: Normalize the number
    exponent = 0
    while FP_num >= 2.0:
        FP_num /= 2.0
        exponent += 1
    while FP_num < 1.0:
        FP_num *= 2.0
        exponent -= 1

    # bias 15 is appply
    exponent_with_bias = exponent + 15  
   
    


    # the first 8 bits of the mantissa / significand 
    significand = FP_num - 1  
    mantissa_bits = []
    for _ in range(8):
        significand *= 2
        bit = int(significand)
        mantissa_bits.append(bit)
        significand -= bit

     #convert exponent and mantissa to binary
    exponent_binary = format(exponent_with_bias,'05b')  # Convert exponent to 5-bit binary

    mantissa_binary = ''.join(map(str, mantissa_bits))  # convert mantissa to binary

    # return the simplified floating-point representation
    return f'{sign} | {exponent_binary} | {mantissa_binary}'


# examples 
num1 = 3.14
num2 = -7.16

print(f"Floating-point number: {num1}")
print(f"Simplified representation: {convertFloatingPoin(num1)}")

print(f"\nFloating-point number: {num2}")
print(f"Simplified representation: {convertFloatingPoin(num2)}")



