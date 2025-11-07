def analyze_text(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(char)

text = input("hello world")
analyze_text(text)
