# encoder.py

def encode_code128(data: str) -> str:
    """
    Encode text into Code 128 format for Libre Barcode font.
    """
    start_char = "Ì"  # Start Code B
    stop_char = "Î"   # Stop
    start_code_b = 104
    checksum = start_code_b

    for i, ch in enumerate(data, start=1):
        value = ord(ch) - 32
        checksum += value * i

    checksum %= 103
    checksum_char = chr(checksum + 32) if 32 <= checksum + 32 <= 126 else "?"
    return f"{start_char}{data}{checksum_char}{stop_char}"
