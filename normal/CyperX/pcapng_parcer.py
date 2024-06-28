import re
import base64

with open("cyperx.pcapng", "rb") as file:
    data = file.read()

patterns = {
    b"\x00\x00\x03\x12\x00\x00\x00\x00\x00\x01": (1, False),  # Base64 디코딩 안 함
    b"\x00\x00\x11\x05\x00\x00\x00\x00\x00\x04": (4, True),  # Base64 디코딩 함
}

pattern_regex = b"|".join(patterns.keys())

results = []

for match in re.finditer(pattern_regex, data):
    pattern = match.group()
    length, decode = patterns[pattern]
    start = match.end()
    end = start + length
    extracted_bytes = data[start:end]

    if decode:
        try:
            decoded_data = base64.b64decode(extracted_bytes)
            results.append(decoded_data)
        except Exception as e:
            results.append(f"Error decoding: {e}")
    else:
        results.append(extracted_bytes)

buf = b"".join(results)
print(buf)
