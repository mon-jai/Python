from typing import List


def main():
    s = str(input()).split()
    sen = [str(input()) for _ in range(int(s[0]))]
    cmd = [str(input()) for _ in range(int(s[1]))]
    Ac: List[str] = []
    for c in cmd:
        cm = c.split()
        if cm[0] == 'ADD_W_FRONT':
            i = int(cm[1])
            n = int(cm[2])
            w = cm[3]
            d = sen[i - 1].split()
            sen[i - 1] = ' '.join(d[:n - 1] + [w] + d[n - 1:])
        elif cm[0] == 'ADD_W_AFTER':
            i = int(cm[1])
            n = int(cm[2])
            w = cm[3]
            d = sen[i - 1].split()
            sen[i - 1] = ' '.join(d[:n] + [w] + d[n:])
        elif cm[0] == 'ADD_S_FRONT':
            i = int(cm[1])
            s = ' '.join(cm[2:])
            ns = [s] + sen[i - 1].split()
            sen[i - 1] = ' '.join(ns)
        elif cm[0] == 'ADD_S_AFTER':
            i = int(cm[1])
            ns = sen[i - 1].split() + [' '.join(cm[2:])]
            sen[i - 1] = ' '.join(ns)
        elif cm[0] == 'INSERT_FRONT':
            sen
            key = cm[1]
            w = cm[2]
            for s in range(len(sen)):
                sen[s] = sen[s].replace(key, w + ' ' + key)
        elif cm[0] == 'INSERT_AFTER':
            key = cm[1]
            w = cm[2]
            for s in range(len(sen)):
                sen[s] = sen[s].replace(key, key + ' ' + w)
        elif cm[0] == 'DEL_W':
            i = int(cm[1])
            n = int(cm[2])
            s = sen[i - 1].split()
            sen[i - 1] = ' '.join(s[:n - 1] + s[n:])
        elif cm[0] == 'DEL_L':
            i = int(cm[1])
            sen = sen[:i - 1] + sen[i:]
        elif cm[0] == "REPLACE":
            old = cm[1]
            new = cm[2]
            for i in range(len(sen)):
                ns = sen[i].split()
                for s in range(len(ns)):
                    if ns[s] == old:
                        ns[s] = new
                sen[i] = ' '.join(ns)
        elif cm[0] == 'COUNT':
            c = 0
            for s in sen:
                c += len(s.split())
            Ac.append(str(c))

    print('\n'.join(Ac + sen))

main()