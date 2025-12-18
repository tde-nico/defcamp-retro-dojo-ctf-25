CIPHERTEXT = bytes([
    0x80,0x8B,0x89,0x8E,0xF0,0xEB,0x8F,0x99,0x88,0xB4,
    0x92,0xE5,0x91,0x98,0x8B,0xE4,0x98,0x88,0x8C,0x91,
    0xE9,0x84,0x9B,0xED,0xEE,0x9B,0xBF,0xD1,0xAE,0xA7,
    0xBB,0xA7,0xB4,0xD6,0xAF,0xA1,0xDD,0xB4,0xA8,0xD9,
    0xB7,0xDA,0x8D,0xD5
])

def compute_key(year:int, month:int, day:int) -> int:
    year_low = year & 0xFF
    return year_low ^ (month & 0xFF) ^ (day & 0xFF)

def decrypt(cipher: bytes, key: int) -> bytes:
    out = bytearray(len(cipher))
    for i, b in enumerate(cipher):
        out[i] = b ^ ((key + i) & 0xFF)
    return bytes(out)

def main(year:int=1993, month:int=11, day:int=4):
    key = compute_key(year, month, day)
    plain = decrypt(CIPHERTEXT, key)
    try:
        text = plain.decode('utf-8')
    except UnicodeDecodeError:
        text = plain.decode('latin-1')
    print(f"Date used: {year:04d}-{month:02d}-{day:02d}")
    print(f"Computed key: 0x{key:02X}")
    print("Decrypted output:")
    print(text)

if __name__ == "__main__":
    main()

# CTF{B4CK_1N_TH3_G00D_0LD_BR1GH7_D4Y5}
