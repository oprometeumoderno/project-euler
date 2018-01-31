largest = 0
(100..999).each do |a|
  (a...999).each do |b|
    if (a * b).to_s == (a * b).to_s.reverse && a * b > largest then
      largest = a * b
    end
  end
end

puts largest
