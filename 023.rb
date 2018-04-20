LIMIT = 28123

def is_abundant? n
  divisors = [1]
  root = Math.sqrt(n)
  (2..root.floor).each do |i|
    if n % i == 0 then
      divisors << i
      divisors << n / i
    end
  end

  divisors.slice!(-1) if root.floor == root
  return true if divisors.sum > n
  return false
end

abundant_numbers = []

(12..28123).each do |i|
  abundant_numbers << i if is_abundant?(i)
end

is_sum = Array.new(LIMIT + 1)

loop do
  curr = abundant_numbers.shift
  is_sum[2 * curr] = true if 2 * curr < LIMIT
  i = 0
  loop do
    sum = curr + abundant_numbers[i]
    break if sum > LIMIT || i == abundant_numbers.size
    is_sum[sum] = true
    i += 1
  end

  break if abundant_numbers.empty? || curr + abundant_numbers[0] > LIMIT
end

result = 0

(0...is_sum.size).each do |i|
  result += i if is_sum[i].nil?
end

puts result
