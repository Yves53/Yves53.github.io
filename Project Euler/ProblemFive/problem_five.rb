start = Time.now
def prime(number) # This method returns an array of prime number
  a = 2
  prime_array = []
  while a < number
    if (number % a).zero?
      number /= a
      prime_array << a
    else
      a += 1
    end
  end
  prime_array << number
end

array2 = []
(0..20).each do |i|
  array = prime(i) # This calls the method for prime numbers
  array.each do |j|
    if array.count(j) > array2.count(j) # This statement verifies that there are enough variables to create the number "J" in array2
      (array.count(j) - array2.count(j)).times { array2 << j } # This add the numbers needed to create "j" if needed to array2
    end
  end
end
puts array2.sort.join(',') # This array now contains every numbers needed to create every number in the given range of numbers
puts array2.reject(&:zero?).inject(:*) # Multiplies every numbers in the array
puts "It tooks #{Time.now - start} second(s) to run"