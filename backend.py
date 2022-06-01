import string

alph = string.ascii_lowercase

def code_message(string):
    bin_string = []
    for char in string:
        bin_string += [int(x) for x in "{0:08b}".format(ord(char))]
        print(char, "{0:08b}".format(ord(char)))
    bin_string.append(2)
    print(len(bin_string))
    return bin_string


def code_image(jpg_array, path_to_webp, coded_msg, img_name):
    point = 0
    for i in range(len(jpg_array)):
        if point < len(coded_msg) and i > 42:
            jpg_array[i] = jpg_array[i] + coded_msg[point] if jpg_array[i] + coded_msg[point] < 255 else jpg_array[i] - coded_msg[point]
            point += 1
    output = open("\\".join(path_to_webp.split("/")[:-1]) + "\\" + str(img_name) + ".jpg", "wb")
    output.write(jpg_array)
    print(jpg_array)


def decode_message(coded_list):
    res_str = ""
    for i in range(0, len(coded_list) - 1, 8):
        res_str += chr(int("".join([str(bit) for bit in coded_list[i:i + 8]]), 2))
    return res_str


def decode_image(coded_array, original_array):
    i = 43
    diff = []
    while i < len(coded_array) and (len(diff) == 0 or diff[-1] != 2):
        diff.append(abs(coded_array[i] - original_array[i]))
        i += 1
    return diff


def jpg_to_bytes(path):
    f = open(path, "br")
    bytes_ = bytearray(f.read())
    return bytes_


def encrypt(txt, key='coursework'):
    ans = ''
    for i in range(len(txt)):
        x = (alph.find(txt[i]) + alph.find(key[i % len(key)])) % 26
        ans += alph[x]
    return ans


def decrypt(txt, key='coursework'):
    ans = ''
    for i in range(len(txt)):
        x = (26 + alph.find(txt[i]) - alph.find(key[i % len(key)])) % 26
        ans += alph[x]
    return ans

def code(path, coded_msg, img_name, mode):
    if mode == '1':
        code_image(jpg_to_bytes(path), path, encrypt(coded_msg), img_name)
    else:
        code_image(jpg_to_bytes(path), path, coded_msg, img_name)


def decode(path_coded, path_original, mode):
    coded_array = jpg_to_bytes(path_coded)
    original_array = jpg_to_bytes(path_original)
    msg_array = decode_image(coded_array, original_array)
    if mode == '1':
        return decrypt(decode_message(msg_array))
    else:
        return decode_message(msg_array)
