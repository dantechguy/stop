def msplit(string, chars):
    result = string
    for char in chars:
        result.replace(char, "`")
    result.replace("`", "")
    return result