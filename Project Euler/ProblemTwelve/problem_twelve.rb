# What is the value of the first triangle number to have over five hundred divisors?
require 'Prime'
start = Time.now
def factor(number)
  a = number
  array = []

  if Prime.prime?(number)
    nod = 2
  else

    while a >= 1
      if (number%a).zero?
        array << a
        a -= 1
      else
        a-=1
      end
    end
    nod = array.length
    puts array.join(',') if array.length > 20
    puts number
  end
  nod
end

a = 1
triangle = 1
while factor(triangle) < 20
  a += 1
  triangle += a
end

puts "The value of the first triangle number to have over five hundred divisors is #{triangle}"
puts Time.now - start

def factors_of(number)
  primes, powers = number.prime_division.transpose
  exponents = powers.map{|i| (0..i).to_a}
  divisors = exponents.shift.product(*exponents).map do |powers|
    primes.zip(powers).map{|prime, power| prime ** power}.inject(:*)
  end
  divisors.sort.map{|div| [div, number / div]}
end

p factors_of(76576500)