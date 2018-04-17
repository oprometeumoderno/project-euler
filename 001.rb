puts (1...1000).to_a.select{|x| x % 3 == 0 || x % 5 == 0}.inject(:+)
