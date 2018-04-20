TARGET = 1000000 - 1

def nth_permutation(digits, target)
  return digits[0] if digits.size == 1
  possibilities = (1...digits.size).to_a.inject(:*)

  i = 0
  loop do
    break if target >= (possibilities) * i && target < (possibilities) * (i+1)
    i += 1
  end

  target = target % ((possibilities) * i)
  return digits.slice!(i) + nth_permutation(digits, target)
end

puts nth_permutation(('0'..'9').to_a, TARGET)
