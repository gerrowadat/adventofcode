def common_chars(word1, word2):
  common = ''
  for i in range(0, len(word1)):
    if word1[i] == word2[i]:
      common += word1[i]
  return common

def main():
    with open('input.txt') as f:
        raw_lines = f.readlines()
    lines = [x.strip('\n') for x in raw_lines]

    # { common_char_count: [(i, j), (i, j) ... ]
    diffs = dict([(x, []) for x in range(0, 50)])

    for i in range(0, len(lines)):
      for j in range(0, len(lines)): 
        if i == j:
          continue
        common = common_chars(lines[i], lines[j])
        if ((min(i, j), max(i, j))) not in diffs[len(common)]:
          diffs[len(common)].append((min(i, j), max(i, j),))

    max_count = max([x for x in diffs.keys() if len(diffs[x]) > 0])
    intersection = common_chars(lines[diffs[max_count][0][0]], lines[diffs[max_count][0][1]])

    print('Max %d: %s' % (max_count, intersection))

main()
