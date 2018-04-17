def factorial n
  (1..n).to_a.inject(:*)
end

puts(factorial(40)/(factorial(20)*factorial(20)))
