#coding=utf-8
import configparser
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
import pickle
import utils.logger as logger
import base64


def get_IV_key():
    try:
        IV='$j8Kww4PCncKZwpx'
        key = get_key("g3nCsMKgw&")
    except:
        logger.logger().exception("set_config:get_IV_key")
    finally:
        return IV, key

def get_key(password):                
    hasher = None
    try:
        hasher = SHA256.new(password.encode('utf-8'))
    except:
        logger.logger().exception("set_config:get_key")
    finally:
        return hasher.digest()


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encrypt_text(plaintext, key, IV):
    ciphertext=None
    try:
        print("encrypt_text(plaintext, key, IV)")
        
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        text_size = len(plaintext)
        if text_size%16!=0:
            plaintext += ' '*(16-text_size%16)
        ciphertext = encryptor.encrypt(plaintext) 
    except:
        logger.logger().exception("set_config:encrypt_text")
    finally:
        return ciphertext


def decrypt_text(ciphertext, key, IV):
    try:
        print("decrypt_text(ciphertext, key, IV)")
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        plaintext = decryptor.decrypt(ciphertext)
        plaintext = plaintext.split()[0].decode('utf-8')
    except:
        logger.logger().exception("set_config:decrypt_text")
    finally:
        return plaintext
    

    
def get_item(src_file, item_key, key, IV):
    ciphertext=None
    try:
        with open(src_file, 'rb') as handle:
            dest_dict = pickle.load(handle)
        ciphertext = dest_dict.get(item_key)
        
    except:
        logger.logger().exception("set_config:get_item")
    finally:
        if ciphertext:
            item_value = decrypt_text(ciphertext, key, IV)
            return item_value
        else:
            return ''
    
    
def set_item(src_file, item_key, item_value, key, IV):
    try:
        if os.path.isfile(src_file):
            with open(src_file, 'rb') as handle:
                config_dict = pickle.load(handle)
        else:
            config_dict = {}
        item_value = encrypt_text(item_value, key, IV)
        config_dict[item_key] = item_value
        with open(src_file, 'wb') as handle:
            pickle.dump(config_dict, handle)
    except:
        logger.logger().exception("set_config:set_item")

    
    
if __name__=='__main__':

    IV, key = get_IV_key()
    src_file = 'Qt5Config'

    set_item(src_file, "TIMES", '0', key, IV)
    item_value = get_item(src_file, "TIMES", key, IV)
    print(item_value)


    
    
        
    
    
    
    
    
    
    
    
    


