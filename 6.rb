n = 100

a = (1..n).to_a.inject(:+) ** 2
b = (1..n).to_a.map{|x| x ** 2}.inject(:+)

puts a - b
