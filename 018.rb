File.open('input/018.txt', 'r') do |file|
  lines = file.read.split("\n")
  triangle = lines.map{|line| line = line.split(' ').map{|x| x.to_i}}.reverse

  (1...triangle.size).each do |line|
    triangle[line].size.times do |row|
      possibilities = [triangle[line-1][row], triangle[line-1][row+1]]
      triangle[line][row] += possibilities.max
    end
  end
  puts triangle[-1]
end
