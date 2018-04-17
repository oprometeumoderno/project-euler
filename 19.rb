require 'date'

current_date = Date.new(1901, 1, 1)
end_date = Date.new(2001, 1, 1)

result = 0
loop do
  result += 1 if current_date.day == 1 && current_date.wday == 0
  current_date = current_date.next_day
  break if current_date == end_date
end

puts result
