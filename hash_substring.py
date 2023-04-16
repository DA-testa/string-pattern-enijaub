# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    iev = input()
    if "F" in iev:
        path = './tests/'+'06'
        with open(path,'r') as f:
            # after input type choice
            # read two lines 
            # first line is pattern 
            # second line is text in which to look for pattern 

            # return both lines in one return
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return pattern, text
    if "I" in iev:
        # this is the sample return, notice the rstrip function
        pattern = input().rstrip()
        text = input().strip()

        return pattern, text


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = 1000000007
    x = 263
    result = []
    pattern_hash = hash_func(pattern, p, x)

    t = len(text)
    p_len = len(pattern)
    h = [0] * (t - p_len + 1)
    s = text[t - p_len:]
    h[t - p_len] = hash_func(s, p, x)
    y = pow(x, p_len, p)
    for i in range(t - p_len - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + p_len])) % p
    for i in range(len(h)):
        if h[i] == pattern_hash:
            if text[i:i+p_len] == pattern:
                result.append(i)
    # and return an iterable variable
    return result


def hash_func(s, p, x):
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

