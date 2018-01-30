last = 1
current = 2
result = 0
while current < 4000000 do
	result += current if current % 2 == 0
	next_one = current + last
	last = current
	current = next_one
end
puts result
