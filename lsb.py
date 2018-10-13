
"""Utility that uses LSB decoding to decode a message found in the first
45 bytes of the pixel data of a BMP file.
"""
# Offset for Windows BMP files, pre-determined by hex dump.
BMP_HEADER_OFFSET = 54
#get path of file
path = raw_input("file path > ")
# Dump all binary of BMP file.
with open(path, "rb") as img:
	bytes = bytearray(img.read())

# Only take the data from the header onward (pixel data only).
bytes = bytes[BMP_HEADER_OFFSET:]
print("Length of pixel data: " + str(len(bytes)))

# Buffer to store parsed decoded results.
buffer = ""

# Temporary buffer to store current byte.
bits = ""
# Parse through all read bytes of pixel data.
for byte in bytes:
	# Get the least significant bit.
	bits += str(byte & 1)
	# If the byte is completed, add its ASCII value to the buffer...
	if len(bits) == 8:
		char = chr(int(bits, 2))
		# ... only if it is readable.
		if ord(char) > 32 and ord(char) < 126:
			buffer += char
		# And reset the current byte
		bits = ""

print("Result: ")
print(buffer[:60] + "... *REMAINING RESULTS OMITTED*")
