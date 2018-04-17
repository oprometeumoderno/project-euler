def collatz_length n
  length = 1
  until n == 1 do
    if n.even?
      n /= 2
    else
      n = 3*n + 1
    end
    length += 1

  end
  return length
end

longest = 0
longest_chain = 0
1000000.times do |i|
  length = collatz_length(i + 1)
  if length > longest_chain then
    longest = i + 1
    longest_chain = length
  end
end

puts longest
