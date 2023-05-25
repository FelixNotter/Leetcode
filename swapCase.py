def swap_case(s):
    ans = []
    for letter in s:
        if not letter.isalpha():
            ans.append(letter)
            continue
        if letter.isupper():
            ans.append(letter.lower())
        else:
            ans.append(letter.upper())
    return "".join(ans)

if __name__ == '__main__':
