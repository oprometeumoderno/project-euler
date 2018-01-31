max_m = 20
max_n = 20

(1..max_n).each do |n|
  (n+1..max_m).each do |m|
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2

    k = 0
    while k*a + k*b + k*c < 1000 do
      if a + b + c == 1000
        puts "#{a*b*c}"
        exit
      end
      k += 1
    end
  end
end
