#Cách 1
import string

def ceasar_cipher(text: str, k: int) -> str:
    """Trả về chuỗi đã mã hóa bằng Caesar cipher với shift k (k có thể >26 hoặc âm)."""
    k = k % 26
    result_chars = []
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase

    for ch in text:
        if ch in upper:
            idx = upper.index(ch)
            result_chars.append(upper[(idx + k) % 26])
        elif ch in lower:
            idx = lower.index(ch)
            result_chars.append(lower[(idx + k) % 26])
        else:
            result_chars.append(ch)
    return ''.join(result_chars)

if __name__ == "__main__":
    plaintext = "HOANGTHIKIMDUNG"
    k = 6

    ciphertext = ceasar_cipher(plaintext, k)
    print(f"Plaintext: {plaintext}")
    print(f"k = {k}")
    print(f"Ciphertext: {ciphertext}")

