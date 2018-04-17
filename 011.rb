File.open('11.txt', 'r') do |file|
  grid = file.read.split("\n").map{|line| line.split(' ').map{|x| x.to_i}}

  width = grid.first.size
  height = grid.size

  largest = 0

  # UP AND DOWN
  (0...height-3).each do |i|
    (0...width).each do |j|
      result = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
      largest = result if largest < result
    end
  end

  # SIDEWAYS
  (0...height).each do |i|
    (0...width-3).each do |j|
      result = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
      largest = result if largest < result
    end
  end

  # DIAGONALLY ASCENDING
  (3...height).each do |i|
    (0...width-3).each do |j|
      result = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
      largest = result if largest < result
    end
  end

  # DIAGONALLY DESCENDING
  (0...height-3).each do |i|
    (0...width-3).each do |j|
      result = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
      largest = result if largest < result
    end
  end

  puts largest
end
