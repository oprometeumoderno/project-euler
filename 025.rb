f_n_minus_2 = 1
f_n_minus_1 = 1
f_n = 2

i = 4

loop do
  f_n_minus_1 = f_n_minus_2
  f_n_minus_2 = f_n
  f_n = f_n_minus_1 + f_n_minus_2
  break if f_n.to_s.split('').size >= 1000
  i += 1
end

puts i
