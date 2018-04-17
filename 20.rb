puts (1..100).to_a.inject(:*).to_s.split('').map{|x| x.to_i}.inject(:+)
