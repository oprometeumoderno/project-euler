require 'prime'

limit = 2000000
primes = Prime::EratosthenesGenerator.new.take_while {|i| i <= limit}
puts primes.inject(:+)
