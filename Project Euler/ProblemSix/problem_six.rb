# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
multi_sum = 0
add_sum = 0
(1..100).each do |i|
  multi_sum += i**2
  add_sum += i
end
puts "The difference between the two is #{(add_sum**2) - multi_sum}"

# answer = 25164150