import base64
from ..chaos_generator import chaos_generator, utils


def decode_key(enc_bytes):
    try:
        enc_bytes = enc_bytes.strip()
        dec_line = base64.standard_b64decode(enc_bytes)
        dec_line_str = dec_line.decode()
        key = [float(value) for value in dec_line_str.split(",")]
        key.append(9.81)
        return key
    except OSError as ex:
        print(f"Exception while decoding key bytes: {str(ex)}")
        return []


def get_encoded_key(hex_string):
    with open("web/security/vault/keyset.txt", "r") as file:
        lines = file.readlines()

    line_index = int(hex_string, 16) % len(lines)
    encoded_keys = lines[line_index].strip().split(",")

    return encoded_keys


encryption_key = "57e579753df01c95ff3c56de0137996f48aacc08d813461ae48d8baec4af0e0c65aebede1fb85aac70747100f3578119"
encoded_key = get_encoded_key(encryption_key)
generate_list_key = decode_key(encoded_key[0])


def encrypt_Text_New(plaintext: str, secret_key=generate_list_key):
    cg = chaos_generator.ChaosGenerator()
    text = utils.convert_to_bytes(plaintext)
    cipher_text = cg.encrypt(text, secret_key)

    # print("Plaintext: ",plaintext)
    # print("Encryption key: ", secret_key)
    # print("Cipher text: ",cipher_text)

    return cipher_text


def decrypt_Text_New(cipher_text: list, secret_key=generate_list_key):
    encoded_key = get_encoded_key(secret_key)
    generate_keys_list = decode_key(encoded_key[0])

    cg = chaos_generator.ChaosGenerator()
    data = cg.decrypt(cipher_text, generate_keys_list)
    plaintext = utils.convert_to_string(data)

    return plaintext


def test():
    cg = chaos_generator.ChaosGenerator()
    key = cg.generate_key()
    print(len(key))
    text = utils.convert_to_bytes("A really secret message. Not for prying eyes.")
    tokens = cg.encrypt(text, key)
    print(tokens)
    data = cg.decrypt(tokens, key)
    print(utils.convert_to_string(data))


# test()


# random_hex = "7764db7b517f010c845e0dbf19ea00c0965dbeefeec4cefb3b1fff73fa5a239ec2105204a240fe76a3364d62fce6f5f1"
# encoded_key = get_encoded_key(random_hex)
# generate_list_key = decode_key(encoded_key[0])
# cipher_text = encrypt_Text_New("Hiijhkjn", generate_list_key)
# plain_text = decrypt_Text_New(cipher_text, generate_list_key)
# print("Decrypted :", plain_text)
