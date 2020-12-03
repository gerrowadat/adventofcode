def main():
    with open('2018/1/input.txt') as f:
        lines = f.readlines()

    result = 0

    for l in lines:
      result += int(l.strip('\n'))

    print ('Result: %s' % (result,))

main()
