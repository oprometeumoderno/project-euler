TARGET = 1000000 - 1

def nth_permutation(digits, target)
  return digits[0] if digits.size == 1
  possibilities = (1...digits.size).to_a.inject(:*)

  i = target / possibilities

  target = target % ((possibilities) * i)
  return digits.slice!(i) + nth_permutation(digits, target)
end

puts nth_permutation(('0'..'9').to_a, TARGET)
