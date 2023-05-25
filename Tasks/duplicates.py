def count_repeated_chars(s):
    s = s.lower()  # convert to lowercase
    char_count = {}
    for char in s:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return len([char for char in char_count if char_count[char] > 1])


print(count_repeated_chars("Indivisibilities"))
