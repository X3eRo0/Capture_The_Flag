import pyperclip
import sys
usage = '''
usage: python vigenere.py <-e or --encrypt> <-k or --key> <lmaoyourkey> DATA
 _________________________________________________________________
|                                                                 |
|  -e      --encrypt            encrypt data with vigenere cipher |
|  -d      --decrypt            decrypt data with vigenere cipher |
|  -k      --key                key for encryption and decryption |
|_________________________________________________________________|
'''
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = ""
def main():
 # This text can be copy/pasted from http://invpy.com/vigenereCipher.py
 message = sys.argv[4]
 
 if sys.argv[2] == "-k" or sys.argv[2] == "--key":
	key = sys.argv[3]
 else:
	for i in range(len(message)):
		key += random.choice(LETTERS)
 if sys.argv[1] == "-e" or sys.argv[1] == "--encrypt":# set to 'encrypt' or 'decrypt'
	mode = 'encrypt'
 elif sys.argv[1] == "-d" or sys.argv[1] == "--decrypt":
	mode = 'decrypt'

 if mode == 'encrypt':
	 translated = encryptMessage(key, message)
 elif mode == 'decrypt':
	 translated = decryptMessage(key, message)


 print(translated)
 pyperclip.copy(translated)
 
 #print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
 return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
 return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
 translated = [] # stores the encrypted/decrypted message string

 keyIndex = 0
 key = key.upper()

 for symbol in message: # loop through each character in message
	 num = LETTERS.find(symbol.upper())
	 if num != -1: # -1 means symbol.upper() was not found in LETTERS
		 if mode == 'encrypt':
			 num += LETTERS.find(key[keyIndex]) # add if encrypting
		 elif mode == 'decrypt':
			 num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

		 num %= len(LETTERS) # handle the potential wrap-around

		 # add the encrypted/decrypted symbol to the end of translated.
		 if symbol.isupper():
			 translated.append(LETTERS[num])
		 elif symbol.islower():
			 translated.append(LETTERS[num].lower())

		 keyIndex += 1 # move to the next letter in the key
		 if keyIndex == len(key):
			 keyIndex = 0
	 else:
		 # The symbol was not in LETTERS, so add it to translated as is.
		 translated.append(symbol)

 return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
	print usage
	main()