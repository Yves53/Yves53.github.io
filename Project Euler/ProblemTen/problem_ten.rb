# Find the sum of all the primes below two million.
require 'mathn'
sum = 0
n = 2_000_000
Prime.each(n) do |i|
  sum += i
end
puts "The sum of all the primes below #{n} is #{sum}"
