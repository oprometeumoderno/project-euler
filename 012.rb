require 'prime'

def number_of_factors n
  result = 0
  sqrt = Math.sqrt(n)
  (1..sqrt.floor).each do |i|
    result +=2 if n % i == 0
  end
  if sqrt.floor == sqrt
    return result-1
  else
    return result
  end
end

i = 2

loop do
  sum = (i * (i+1))/2
  if number_of_factors(sum) > 500
    puts sum
    exit
  else
    i += 1
  end
end
