import sys

def main():
    lines = sys.stdin.readlines()
    out = []
    for line in lines:
        line = line.strip()
        if 'ORDER' in line:
            t = line.split('.')
            out.append(t[0] + '.')
            out.append('.'.join(t[1:]))
        else:
            out.append(line)
    out = [o for o in out if len(o) > 1]
    print('\n'.join(out))

if __name__ == '__main__':
    main()
        
