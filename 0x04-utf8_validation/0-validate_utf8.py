#!/usr/bin/python3
"""method that determines if a
given data set represents
a valid UTF-8 encoding."
def validUTF8(data):
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Mask to check the least significant 8 bits of num
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes in the character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0