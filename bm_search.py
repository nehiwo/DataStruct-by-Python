#-*- coding: utf-8 -*-

def bm_search(text, key):
    m = len(key)
    skip = [m for _ in range(256)]

    #ずらし表の作成
    for i in range(m):
        skip[ord(key[i])] = m - i - 1

    #文字列探索
    i = m - 1
    while i < len(text):
        j = m - 1
        while text[i] == key[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i = i + max(skip[ord(text[i])], m - j)
    return i

if __name__ == "__main__":
    text = "TRTTCJHVUYTRSERCVUFYTRRYCUDRTSYTIFYTDUTVHJCTRSRTDCHFYJTDYTXRTST"
    key = "ERCVUFYTRRY"

    index = bm_search(text, key)

    if index >= 0 and index <= len(text) - len(key):
        print("index:" + str(index))
    else:
        print("No exist.")
