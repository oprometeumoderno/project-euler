largest = 0

File.open('8.txt', 'r') do |file|
  big_ass_number = file.read.split("\n").join
  (0..big_ass_number.size-12).each do |i|
    current = big_ass_number[i..i+12].split('').map{|x| x.to_i}.inject(:*)
    largest = current if current > largest
  end
end

puts largest
