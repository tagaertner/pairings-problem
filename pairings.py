def find_pairs(num_string):
  # Write your solution here!

  new_nums =num_string.split()
  pair_nums = set()
    
  for num1 in new_nums:
    for num2 in new_nums:
      convert_num1 = int(num1)
      convert_num2= int(num2)
      if convert_num1 < convert_num2:
        pair_nums.add((convert_num1,convert_num2))
  return pair_nums
  
  
  

# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")