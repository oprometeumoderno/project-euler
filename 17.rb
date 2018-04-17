uni = [
  "",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "eleven",
  "twelve",
  "thirteen",
  "fourteen",
  "fifteen",
  "sixteen",
  "seventeen",
  "eighteen",
  "nineteen"
]

dez = [
  "",
  "",
  "twenty",
  "thirty",
  "forty",
  "fifty",
  "sixty",
  "seventy",
  "eighty",
  "ninety"
]

result = 0
(1...1000).each do |i|
  result += uni[i / 100].size + "hundred".size if i >= 100

  if i % 100 > 0 then
    result += "and".size if i >= 100
    if i % 100 < 20 then
      result += uni[i % 100].size
    else
      result += dez[(i % 100) / 10].size + uni[(i % 100) % 10].size
    end
  end

end
result += "one".size + "thousand".size
puts result
