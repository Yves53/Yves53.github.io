# Find the largest palindrome made from the product of two 3-digit numbers.
a = 0
b = 0
c = 0
pld_number = 0
(101..999).reverse_each do |i|
  (100..(998 - c)).reverse_each do |j|
    break if j <= b
    number = i * j
    array = number.to_s.scan(/\w/)
    if (array == array.reverse) && (number > pld_number)
      pld_number = number
      a = i
      b = j
    end
  end
  c += 1
end
puts "The largest palindrome from the product of #{a} and #{b} is #{pld_number}"