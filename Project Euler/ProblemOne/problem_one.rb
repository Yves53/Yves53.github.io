# Find the sum of all the multiples of 3 or 5 below 1000

sum = 0
(3..999).each do |i|
  sum += i if (i % 3).zero? || (i % 5).zero?
end
puts sum

