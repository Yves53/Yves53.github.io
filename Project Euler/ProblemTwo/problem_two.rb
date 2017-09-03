# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms
fb_number = 0
sum = 0
a = 1
b = 2
while fb_number < 4_000_000
  sum += b if (fb_number % 2).zero?
  fb_number = a + b
  a = b
  b = fb_number
end
puts sum