# What is the 10001st prime number?
require 'Prime'
n = 10_001
puts "The #{n} prime number is #{Prime.take(n).last}"


