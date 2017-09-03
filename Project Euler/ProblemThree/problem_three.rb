# What is the largest prime factor of the number 600851475143?
n = 600_851_475_143
def prime(number)
  a = 2
  while a < number
    if (number % a).zero?
      number /= a
    else
      a += 1
    end
  end
  number
end
puts "The largest prime factor of the number #{n} is #{prime(n)}"

