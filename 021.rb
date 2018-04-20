def sum_of_divisors n
    return 1 if n == 1
    divisors = [1]
    root = Math.sqrt(n)
    (2...root.floor).each do |i|
      if n % i == 0
        divisors << i
        divisors << n / i
      end
    end
    divisors << root.floor if root == root.floor
    return divisors.sum
end

result = 0
10000.times do |i|
    sof = sum_of_divisors(i)
    if sum_of_divisors(sof) == i && i != sof
      result += i
    end
end

puts result
