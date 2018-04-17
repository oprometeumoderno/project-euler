File.open('13.txt', 'r') do |file|
  sum = file.read.split("\n").map{|x| x.to_i}.inject(:+)
  puts sum.to_s[0..9]
end
