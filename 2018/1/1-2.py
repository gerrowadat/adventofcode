import sys

def main():
    with open('2018/1/input.txt') as f:
        lines = f.readlines()

    current = 0
    freqs = []

    while True:
        for l in lines:
            freqs.append(current)

            this = int(l.strip('\n'))
            current += this

            #print('Current (%d stored): %d' % (len(freqs), current,))

            if current in freqs:
                print ('First seen twice: %s' % (current,))
                sys.exit(0)
            freqs.append(current)
          



main()
