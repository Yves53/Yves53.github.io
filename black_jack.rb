class Black_jack

  attr_accessor :cards, :card_deck, :bet_money, :deposit, :array, :value, :cards_value, :answer, :d_cards_value, :d_cards, :remove_ten_p, :remove_ten_d

  def initialize
    @cards = []
    @card_deck = %q( 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, A♣, J♣, Q♣, K♣, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, A♦, J♦, Q♦, K♦, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, A♥, J♥, Q♥, K♥, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, A♠, J♠, Q♠, K♠).split(/,/)
    @bet_money = bet_money
    @deposit = deposit
    @value = value
    @array =[]
    @cards_value = 0
    @d_cards = []
    @d_cards_value = 0
    @answer = answer
    @remove_ten_p = 0
    @remove_ten_d = 0
  end

  def set_deposit
    @deposit = gets.to_i
  end

  def set_bet_money
    @bet_money = gets.to_i
  end

  def hit_card # Method to deal cards
    card = '' # Initialize "card" as a string variable
    loop do
      @value = rand(52) # randomly choose a number between 0 and 51
      card = @card_deck[@value] # This gets the corresponding card in "card_deck"
      break unless @array.include?(card) # keeps looping if the randomly chosen card is already in the "array"
    end
    @array << card # Add the card in the array so that it cannot be dealt again until the deck is reset
    card # return the card to the caller
  end # end method to deal cards

  ##### Method to calculate the value of a card #####
  def card_value(a)
    a = a + 1 # Add one(1) to the variable so that we have 1 through 52 cards instead of 0 through 51
    number = 0 # Initialize "number " as an integer
    if a == 1 || a == 14 || a == 27 || a == 40 # These numbers represent the current position of cards in the the array "card_deck"
      number = 2 # and this is the value of that card
    elsif a == 2 || a == 15 || a == 28 || a == 41
      number = 3
    elsif a == 3 || a == 16 || a == 29 || a == 42
      number = 4
    elsif a == 4 || a == 17 || a == 30 || a == 43
      number = 5
    elsif a == 5 || a == 18 || a == 31 || a == 44
      number = 6
    elsif a == 6 || a == 19 || a == 32 || a == 45
      number = 7
    elsif a == 7 || a == 20 || a == 33 || a == 46
      number = 8
    elsif a == 8 || a == 21 || a == 34 || a == 47
      number = 9
    elsif a == 9 || a == 22 || a == 35 || a == 48
      number = 10
    elsif a == 10 || a == 23 || a == 36 || a == 49
      number = 11
    elsif a == 11 || a == 24 || a == 37 || a == 50
      number = 10
    elsif a == 12 || a == 25 || a == 38 || a == 51
      number = 10
    elsif a == 13 || a == 26 || a == 39 || a == 52
      number = 10
    end
    number
  end
  ##### End method to calculate the value of a card #####

  ##### player's card block #####
  def cards_total_value(v = 0)
    @cards_value += v.to_i # This add the cards values
    if @cards_value > 21 # This statement execute when the total value of cards exceed 21
      @cards_value -= @remove_ten_p # If one of the cards is an Ace that was counted as 11, 10 is subtracted
      @remove_ten_p = 0 # This value is then reset so that it doesn't keep subtracting 10
    end
    @cards_value # Variable to display the total value of the player's cards.
  end

  def player_cards(c) # This method add the cards that are dealt to the array "cards" when called
    @cards.push(c)
  end

  def print_player_cards # This method print the string of cards that was dealt
    card = ''
    @cards.each do |i|
      card += i
    end
    card
  end
  ##### end player's cards block #####

  ##### start dealer's cards block #####
  def d_cards_total_value(d = 0)
    @d_cards_value += d.to_i
    if @d_cards_value > 21
      @d_cards_value -= @remove_ten_d
      @remove_ten_d = 0
    end
    @d_cards_value
  end

  def dealer_cards(c)
    @d_cards.push(c)
  end

  def print_dealer_cards
    card = "#{}"
    @d_cards.each do |i|
      card += i
    end
    card
  end
  ##### end dealer's cards block #####
end

########################################## end Black_jack class #################################################

bj = Black_jack.new

puts 'How much do you want to deposit?'
print '$'
bj.set_deposit

if bj.deposit <= 0 # This statement check to make sure the player entered a valid amount
  loop do
    puts 'INVALID!Please enter an amount more than $0'
    bj.set_deposit
    break if bj.deposit > 0
  end
end

########################### This block repeats as log as the player wants to play again ###########################
loop do
# reset the deck if there are 10 cards or less left in it
  if bj.array.length >= 42
    puts "There are only #{52 - bj.array.length} cards left in the deck.\nThe game will continue with a new deck of cards"
    bj.array = [] # This reset the array containing played cards
  end

  # reset values for the next deal
  bj.cards = []
  bj.d_cards = []
  bj.cards_value = 0
  bj.d_cards_value = 0
  bj.remove_ten_p = 0
  bj.remove_ten_d = 0
  puts "You have $#{bj.deposit}! \nHow much do you want to bet?"
  bj.set_bet_money

  # Make sure the bet does not exceed the current balance
    while bj.bet_money > bj.deposit || bj.bet_money <= 0
      puts "INVALID!Please enter an amount equal or lower than $#{bj.deposit}"
      bj.set_bet_money
    end

  2.times do # Player's first two card
    card = bj.hit_card # call the method to deal a random card
    bj.player_cards(card) # This method keeps this player's cards in the variable "cards"
    value = bj.card_value(bj.value)
    # value of Ace
    if value == 11
      value = 1 unless (bj.cards_value + 11) <= 21
    end
    # end value of Ace

    if value == 11
      bj.remove_ten_p = 10
    end
    bj.cards_total_value(value)
  end # end Player's first two card

  puts "Your cards are: #{bj.print_player_cards}" # print the player's cards
  puts "Their value is: #{bj.cards_total_value}" # And the value
  puts 'BLACKJACK!' if bj.cards_total_value == 21 # Display if the first two cards add up to 21

  # dealer's first card
  if bj.cards_total_value <21 # This statement execute only if the player's first 2 cards did not add up to 21
    d_card = bj.hit_card
    bj.dealer_cards(d_card)
    d_value = bj.card_value(bj.value)
    bj.d_cards_total_value(d_value)
    puts "The dealer's card is: #{bj.print_dealer_cards}"
    puts "its value is: #{bj.d_cards_total_value}"
  # end dealer's first card

  loop do # Hit loop
      puts 'HIT(H) or STAND(S)'
      bj.answer = gets.chomp.upcase
      unless bj.answer == 'H' || bj.answer == 'S' # make sure the answer is H or S
        loop do
          puts 'Please enter a valid answer; H for Hit or S for Stand'
          bj.answer = gets.chomp.upcase
          break if bj.answer == 'H' || bj.answer == 'S'
        end
      end # end unless statement
      if bj.answer == 'H'
        h_card = bj.hit_card
        bj.player_cards(h_card)
        h_value = bj.card_value(bj.value)
        # value of Ace
        if h_value == 11
          h_value = 1 unless (bj.cards_value + 11) <= 21
        end
        if h_value == 11 # When ace is counted as 11, "remove_ten_d" is assigned the value of 10 so that it can be subtracted if the total value is over 21
          bj.remove_ten_p = 10
        end
        # end value of Ace
        bj.cards_total_value(h_value)
        puts "Your cards are: #{bj.print_player_cards}"
        puts "Their value is: #{bj.cards_total_value}"
        puts 'BUST!' if bj.cards_total_value > 21
      end
    break if (bj.answer == 'S' || bj.cards_total_value >= 21)
  end #end do , break loop when answer is STAND(S)
  end # end if statement

  ##### start dealer's card block #####
  if bj.cards_total_value < 21 # Execute if the player's cards did not add up to 21
    loop do
        dd_card = bj.hit_card
        bj.dealer_cards(dd_card)
        dd_value = bj.card_value(bj.value)
        if dd_value == 11
          dd_value = 1 unless (bj.d_cards_value + 11) <= 21
        end
        if dd_value == 11 # When ace is counted as 11, "remove_ten_d" is assigned the value of 10 so that it can be subtracted if the total value is over 21
          bj.remove_ten_d = 10
        end
        bj.d_cards_total_value(dd_value)
      break if (bj.d_cards_total_value > bj.cards_total_value || bj.d_cards_total_value >= 21 || bj.d_cards_total_value == bj.cards_total_value)
    end
    puts "The dealer's cards are: #{bj.print_dealer_cards}"
    puts "Their value is: #{bj.d_cards_total_value}"
  end
  ##### end dealer's card block #####

  ##### check if the player won, lost or it's a push; then update the balance accordingly #####
  if bj.cards_total_value == 21 || (bj.d_cards_total_value > 21 && bj.cards_total_value < 21) # It's a WIN
    puts 'You won!'
    bj.deposit += bj.bet_money
    puts "Your new balance is: $#{bj.deposit}"

  elsif bj.cards_total_value == bj.d_cards_total_value # It's a PUSH
    puts 'PUSH!'
    puts "Your balance is still: $#{bj.deposit}"

  else # It's a losing deal
    puts 'You Lost!'
    bj.deposit -= bj.bet_money
    puts "Your new balance is: $#{bj.deposit}"
  end
  ###### end check for deals #####

  puts "There are #{52 - bj.array.length} cards left in the deck" # Keep track of cards in the deck
  puts 'Do you want to Play again? Yes(Y) or No(N)' # ask the player if they want to continue playing, after a deal
  pa_answer = gets.chomp.upcase

  unless pa_answer == 'N' || pa_answer == 'Y' # make sure the answer is Y or N
    loop do
      puts 'Please enter a valid answer; Y for Yes or N for No'
      pa_answer = gets.chomp.upcase
      break if pa_answer == 'N' || pa_answer == 'Y'
    end
  end # end unless statement

  ##### Executes when the balance is zero, and the player wants to keep playing after adding money #####
  if bj.deposit == 0 && pa_answer == 'Y'
    puts 'You are out of money; do you want to add more?'
    puts 'Please press Y for Yes or N for No'
    deposit_answer = gets.chomp.upcase # get the player's answer

    unless deposit_answer == 'N' || deposit_answer == 'Y' # unless statement to make sure the answer is Y or N
      loop do
        puts 'Please enter a valid answer; Y for Yes or N for No'
        deposit_answer = gets.chomp.upcase
        break if deposit_answer == 'N' || deposit_answer == 'Y'
      end
    end # end unless statement

    if deposit_answer == 'Y' # This statement execute when the player choose to add money
      puts 'How much do you want to deposit?'
      print '$'
      bj.set_deposit
      if bj.deposit <= 0
        loop do
          puts 'Please enter a valid amount, more than $0'
          bj.set_deposit
          break if bj.deposit > 0
        end
      end
    end # end if statement for deposit
  end
  ##### end if statement after money was added or not #####

  break if pa_answer == 'N' || bj.deposit == 0 # Exit the loop (game) when the player answers No (N)
end
################################################# End play again! #####################################################
puts 'Thanks for playing!'
puts 'GAME OVER!'