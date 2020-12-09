def has_sum(i, nums):
  for n in nums:
    sums = [x for x in nums if x != n and x + n == i]
    if sums:
      return True

def get_sumset(t, nums):
  """ t (int): Index within the list of the target number
      nums (list): List of numbers, including the target"""
  for idx in range(t, 0, -1):
    windowsize = 1
    shift_down = False
    while not shift_down:
      if idx - windowsize < 0:
        return False
      window_sum = sum(nums[idx-windowsize:idx])
      if window_sum == nums[t]:
        return nums[idx-windowsize:idx]
      if window_sum > nums[t]:
        shift_down = True
      if window_sum < nums[t]:
        windowsize += 1
        
  return None

def main():

  preamble = 25

  window = []

  with open('input.txt') as f:
    raw_lines = f.readlines()

  lines = [int(x.strip('\n')) for x in raw_lines]

  # Get our initial preamble window
  for p in range(0, preamble):
    window.append(lines[p])

  for l in range(preamble, len(lines)): 
    if not has_sum(lines[l], window):
      print('%d does not have a sum pair in %s' % (lines[l], window))
      sumset = get_sumset(l, lines)
      if sumset:
        print('Summed by: %s' % (sumset))
        print('Weakness: %d' % (sorted(sumset)[0] + sorted(sumset)[-1]))
      return
    window.append(lines[l])
    window.pop(0)

  print('Input valid')

main()
