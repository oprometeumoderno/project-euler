puts (2**1000).to_s.split('').map{|x| x.to_i}.inject(:+)
