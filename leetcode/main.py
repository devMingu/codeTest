def repeatedSubstringPattern(s):
    s_idx = 0
    last = 1
    l_idx = 0
    while last <= len(s) - last:
        if s[s_idx] != s[l_idx]:
            last += 1
            s_idx = 0
            l_idx = last
            continue
        s_idx += 1
        s_idx %= last
        l_idx += 1
        if l_idx >= len(s):
            if s_idx == 0:
                return True
    return False


print(repeatedSubstringPattern("a"))