import sys

def test():
  string = 'この文字列は隠すべし。'
  key = int(sys.argv[1]) if len(sys.argv) > 1 else 19
  print(f'Key: {key}')
  
  encrypted_string = encrypt(string, key)
  decrypted_string = decrypt(encrypted_string, key)

  print(f'暗号化された文字列：{encrypted_string}')
  print(f'復号化された文字列：{decrypted_string}')

def encrypt(string, key):
  encrypted_string = ''

  for char in string:
    encrypted_char_code = ord(char) + key
    len_code = len(str(encrypted_char_code))
    encrypted_string += f'{len_code}x{encrypted_char_code}'

  return encrypted_string

def decrypt(string, key):
  decrypted_string = ''
  current_pos = 0

  # Get length of encrypted char code located at current pos - Read until 'x'
  while current_pos < len(string):
    len_code_string = ''

    while string[current_pos] != 'x':
      len_code_string += string[current_pos]
      current_pos += 1

    len_code = int(len_code_string)
    current_pos += 1

    encrypted_char_code = ''
    for _ in range(len_code):
      encrypted_char_code += string[current_pos]
      current_pos += 1
    encrypted_char_code = int(encrypted_char_code)
    
    decrypted_char_code = encrypted_char_code - key
    decrypted_string += chr(decrypted_char_code)

  return decrypted_string

if __name__=='__main__':
  test()
