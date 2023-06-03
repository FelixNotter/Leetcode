import textwrap

def wrap(string, max_width):
    res = []
    for i in range(len(string)):
        if i != 0 and i % max_width == 0:
            res.append('\n')
        res.append(string[i])
    return "".join(res)

if __name__ == '__main__':
