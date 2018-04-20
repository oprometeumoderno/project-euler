scores = ("A".."Z").to_a

File.open("input/022.txt", "r") do |file|
  names = file.read.split("\",\"")
  names[0]  = names[0][1..-1]
  names[-1] = names[-1][0..-2]
  names = names.sort

  result = 0
  (0...names.size).each do |name|
    score = 0
    names[name].split('').each do |char|
      score += scores.index(char) + 1
    end
    result += (score * (name + 1))
  end

  puts result
end
