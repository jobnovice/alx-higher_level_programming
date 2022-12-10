def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i == n:
            str[i] = ""
    return str;