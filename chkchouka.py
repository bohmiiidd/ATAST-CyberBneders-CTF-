loughet_num_3 = '3aa'
loughet_num_2 = 'ééé'
wbi3et_num_5 = 'KHAAA'
wle2iii = 'i' # maybee^^
real_key = 'boh' 
fake_key = 12345
key = fake_key

def chkchouka(text, key):
    transformed_chars = []
    dynamic_key = (key + len(text)) % 256

    for i, char in enumerate(text):
        ascii_val = ord(char)
        ascii_val = (ascii_val + (i + dynamic_key)) % 256
        ascii_val ^= (dynamic_key >> (i % 8))
        shift_amount = (i + 3) % 8
        ascii_val = ((ascii_val << shift_amount) & 0xFF) | (ascii_val >> (8 - shift_amount))
        
        transformed_chars.append(ascii_val)
    
    transformed_chars.reverse() 
    return transformed_chars

