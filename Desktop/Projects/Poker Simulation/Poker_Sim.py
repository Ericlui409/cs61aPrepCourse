"""Part 1: Original deck"""
Suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
Number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

Original_deck = []
for item in Suits:
	for i in range(0,len(Number)):
		card = " "
		Original_deck.append(card.join([item, Number[i]]))

"""Part 2: Hand determinator"""
def individual_card_value(card):
	if card[-1] == "2":
		return 2
	elif card[-1] == "3":
		return 3
	elif card[-1] == "4":
		return 4
	elif card[-1] == "5":
		return 5
	elif card[-1] == "6":
		return 6
	elif card[-1] == "7":
		return 7
	elif card[-1] == "8":
		return 8
	elif card[-1] == "9":
		return 9
	elif card[-1] == "0":
		return 10
	elif card[-1] == "J":
		return 11
	elif card[-1] == "Q":
		return 12
	elif card[-1] == "K":
		return 13
	elif card[-1] == "A":
		return 14

def numerical_values(cards):
	return [individual_card_value(x) for x in cards]

def Consecutive_tester(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	for i in range(0, len(sorted_cards) - 1):
		if not sorted_cards[i] + 1 == sorted_cards[i + 1]:
			return False
	return True

def Straight(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	return Consecutive_tester(hand) or (sorted_cards[0] == 2 and sorted_cards[1] == 3 and sorted_cards[2] == 4 and sorted_cards[3] == 5 and sorted_cards[4] == 14)

def Flush(hand):
	if len(hand) == 2:
		if hand[0][0] == hand[-1][0]:
			return True
	else:
		if hand[0][0] == hand[1][0]:
			return Flush(hand[1:])
	return False

def Straight_Flush(hand):
	return Straight(hand) and Flush(hand)

def Royal_Flush(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	return Straight_Flush(hand) and sorted_cards[4] == 14 and sorted_cards[3] == 13

def Four_of_a_kind_determinator(sorted_hand, count):
	if count == 4:
		return True
	else:
		if len(sorted_hand) == 1:
			return False
		else:
			if sorted_hand[0] == sorted_hand[1]:
				return Four_of_a_kind_determinator(sorted_hand[1:], count + 1)
			else:
				return Four_of_a_kind_determinator(sorted_hand[1:], count = 1)

def Four_of_a_kind(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	return Four_of_a_kind_determinator(sorted_cards, 1)

def Three_of_a_kind_determinator(sorted_hand, count):
	if count == 3:
		return True
	else:
		if len(sorted_hand) == 1:
			return False
		else:
			if sorted_hand[0] == sorted_hand[1]:
				return Three_of_a_kind_determinator(sorted_hand[1:], count + 1)
			else:
				return Three_of_a_kind_determinator(sorted_hand[1:], count = 1)

def Three_of_a_kind(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	return Three_of_a_kind_determinator(sorted_cards, 1) and not Four_of_a_kind_determinator(sorted_cards, 1) and not Full_House(hand)

def Full_House(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	return Three_of_a_kind_determinator(sorted_cards, 1) and sorted_cards[0] == sorted_cards[1] and sorted_cards[3] == sorted_cards[4]

def Two_pair_determinator(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	counter = 0	
	for i in range(0,len(sorted_cards) - 1):
		if sorted_cards[i] == sorted_cards[i + 1]:
			counter += 1
	if counter == 2:
		return True
	else:
		return False

def Two_pair(hand):
	return Two_pair_determinator(hand) and not Three_of_a_kind(hand) and not Four_of_a_kind(hand) and not Full_House(hand)

def Pair(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	counter = 0	
	for i in range(0,len(sorted_cards) - 1):
		if sorted_cards[i] == sorted_cards[i + 1]:
			counter += 1
	if counter == 1:
		return True
	else:
		return False

def Hand_determinator(hand):
	if Royal_Flush(hand):
		return "Royal Flush"
	else:
		if Straight_Flush(hand):
			return "Straight Flush"
		else:
			if Four_of_a_kind(hand):
				return "Four-of-a-kind"
			else:
				if Full_House(hand):
					return "Full House"
				else:
					if Flush(hand):
						return "Flush"
					else:
						if Straight(hand):
							return "Straight"
						else:
							if Three_of_a_kind(hand):
								return "Three-of-a-kind"
							else:
								if Two_pair(hand):
									return "Two pair"
								else:
									if Pair(hand):
										return "Pair"
									else:
										return "High Card"

Hand_equivalent_value = {"Royal Flush": 135, "Straight Flush": 120, "Four-of-a-kind": 105, "Full House": 90, "Flush": 75, "Straight": 60, "Three-of-a-kind": 45, "Two pair": 30, "Pair": 15, "High Card": 0}

def Higher_hand_determinator(input_1, input_2):
	hand_1 = Hand_determinator(input_1)
	hand_2 = Hand_determinator(input_2)
	if Hand_equivalent_value[hand_1] > Hand_equivalent_value[hand_2]:
		return ["input_1", hand_1]
	elif Hand_equivalent_value[hand_2] > Hand_equivalent_value[hand_1]:
		return ["input_2", hand_2]
	else:
		freq_1 = frequency_finder(input_1)[::-1]
		freq_2 = frequency_finder(input_2)[::-1]
		for i in range(0, len(freq_1)):
			if freq_1[i] > freq_2[i]:
				return ["input_1", hand_1]
			elif freq_2[i] > freq_1[i]:
				return ["input_2", hand_2]
	return "Split"

"""Part 3: Other useful blocks"""
def frequency_finder(hand):
	cards = numerical_values(hand)
	sorted_cards = sorted(cards)
	frequency_table = {}
	for item in sorted_cards:
		if item in frequency_table:
			frequency_table[item] += 1
		else:
			frequency_table[item] = 1
	return sorted(sorted(frequency_table), key = frequency_table.get)

def is_not_number(input):
	try:
		value = int(input)
	except ValueError:
		return True
	return False

def subset_finder(set, n):
	if n == 0:
		return [[]]
	if len(set) == 0:
		return []
	subsets = subset_finder(set[1:], n - 1)
	for item in subsets:
		item.append(set[0])
	return subsets + subset_finder(set[1:], n)
"""Took reference from http://stackoverflow.com/questions/16221875/calculating-subsets-of-a-given-list-recursively for the above block"""

"""Part 4: Game code"""
"""Player Class"""
class Player:
	def __init__(self, money, bet, hand):
		self.money = money
		self.bet = bet
		self.hand = hand

player = Player(0, 0, [])
cpu = Player(0, 0, [])

def Card_dealer(deck, destination, n):
	import random
	chosen_cards = random.sample(deck, n)
	for item in chosen_cards:
		deck.remove(item)
	destination += chosen_cards

def input_money_amount_layer():
	import time
	number = raw_input("Please enter how much money you want to play with: ")
	if is_not_number(number):
		print
		print "Sorry, your input is not a number, please try again."
		print
		time.sleep(1)
	else:
		Available_money = int(number)
		print
		time.sleep(1)
		print("Okay, the game will end when you have lost all $" + str(Available_money))
		print
		player.money = Available_money
		cpu.money = Available_money
		global invalid_input
		invalid_input = False

def input_money_amount():
	global invalid_input
	invalid_input = True
	input_money_amount_layer()
	while invalid_input:
		input_money_amount_layer()

def input_blind_amount_layer():
	import time
	global Small_blind
	global Big_blind
	number = raw_input("Please enter how much you want the small blind to be: ")
	if is_not_number(number):
		print
		print "Sorry, your input is not a number, please try again."
		print
		time.sleep(1)
	else:
		Small_blind = int(number)
		print
		time.sleep(1)
		print("Okay, the small blind would be $" + str(Small_blind))
		print
		Big_blind = Small_blind * 2
		global invalid_input
		invalid_input = False

def input_blind_amount():
	global invalid_input
	invalid_input = True
	input_blind_amount_layer()
	while invalid_input:
		input_blind_amount_layer()

def folding(who):
	global pot
	global folder
	folder = who
	if who == "player":
		cpu.money += player.bet
		player.bet = 0
		cpu.money += cpu.bet
		cpu.bet = 0
		cpu.money += pot
		pot = 0
	if who == "cpu":
		player.money += cpu.bet
		cpu.bet = 0
		player.money += player.bet
		player.bet = 0
		player.money += pot
		pot = 0

def raising_layer(who):
	global invalid_input
	import time
	if who == "cpu":
		amount = player.bet * 2
		cpu.money += - (amount - cpu.bet)
		cpu.bet = amount
		invalid_input = False
		print
		print "The computer has raised to $" + str(amount) + "."
		print
		time.sleep(3)
	else:
		print
		amount = raw_input("Please enter the amount you wish to raise to: ")
		print
		if is_not_number(amount):
			print
			print "Sorry, your input is not a number, please try again."
			print
			time.sleep(1)
		else:
			amount = int(amount)
			if who == "player":
				if amount < cpu.bet * 2:
					print
					print "You have to raise to a minimum of $" + str(cpu.bet * 2) + "."
					print
					time.sleep(1)
				else:
					if amount - player.bet > player.money:
						print
						print "Sorry, you do not have that much money."
						print
						time.sleep(1)
					elif amount - cpu.bet > cpu.money:
						print
						print "Sorry, your opponent does not have that much money."
						print
						time.sleep(1)
					else:
							player.money += - (amount - player.bet)
							player.bet = amount
							invalid_input = False

def raising(who):
	global invalid_input
	global raised
	invalid_input = True
	raising_layer(who)
	while invalid_input:
		raising_layer(who)
	raised += 1

def betting_layer(who):
	global invalid_input
	global Big_blind
	import time
	if who == "cpu":
		amount = Big_blind
		if amount > player.money or amount > cpu.money:
				amount = min(player.money, cpu.money)
				cpu.money += - amount
				cpu.bet += amount
				invalid_input = False
				print
				print "The computer has betted $" + str(amount) + "."
				print
				time.sleep(3)
		else:
			cpu.money += - amount
			cpu.bet += amount
			invalid_input = False
			print
			print "The computer has betted $" + str(amount) + "."
			print
			time.sleep(3)
	else:
		print
		amount = raw_input("Please enter the amount you wish to bet: ")
		print
		if is_not_number(amount):
			print
			print "Sorry, your input is not a number, please try again."
			print
			time.sleep(1)
		else:
			amount = int(amount)
			if amount <= 0:
				print
				print "Your bet must be larger than 0."
				print
				time.sleep(1)
			elif amount < Big_blind and player.money >= Big_blind and cpu.money >= Big_blind:
				print
				print "The minimum bet is $" + str(Big_blind) + "."
				print
				time.sleep(1)
			else:
				if who == "player":
					if amount > player.money:
						print
						print "Sorry, you do not have that much money."
						print
						time.sleep(1)
					elif amount > cpu.money:
						print
						print "Sorry, your opponent does not have that much money."
						print
						time.sleep(1)
					else:
						player.money += - amount
						player.bet += amount
						invalid_input = False

def betting(who):
	global invalid_input
	invalid_input = True
	betting_layer(who)
	while invalid_input:
		betting_layer(who)	

def call(who):
	if who == "player":
		player.money += - (cpu.bet - player.bet)
		player.bet += (cpu.bet - player.bet)
	if who == "cpu":
		cpu.money += - (player.bet - cpu.bet)
		cpu.bet += (player.bet - cpu.bet)

def starting_call(who):
	if who == "player":
		player.money += -Small_blind
		player.bet += Small_blind
	if who == "cpu":
		cpu.money += -Small_blind
		cpu.bet += Small_blind

def checking():
	global checked
	checked += 1

def end_round():
	global pot
	global checked
	global raised
	pot += cpu.bet + player.bet
	cpu.bet = 0
	player.bet = 0
	checked = 0
	raised = 0


def ask_for_action_layer():
	import time
	global invalid_input
	global action
	if (player.money == 0 or cpu.money == 0) and player.bet == cpu.bet:
		print
		action = raw_input("Please choose to fold or check: ").lower()
		if action == "fold" or action == "check":
			invalid_input = False
		else:
			print
			print "Sorry, invalid input. Please try again."
			print
			time.sleep(1)
	else:
		if player.bet == cpu.bet == 0:
			print
			action = raw_input("Please choose to fold, check or bet: ").lower()
			if action == "fold" or action == "check" or action == "bet":
				invalid_input = False
			else:
				print
				print "Sorry, invalid input. Please try again."
				print
				time.sleep(1)
				"""the case below considers the starting round"""
		elif player.bet == cpu.bet and not player.bet == 0:
			if player.bet - cpu.bet == cpu.money or cpu.bet - player.bet == player.money:
				print
				action = raw_input("Please choose to fold or call: ").lower()
				if action == "fold" or action == "call":
					invalid_input = False
				else:
					print
					print "Sorry, invalid input. Please try again."
					print
					time.sleep(1)
			else:
				print
				action = raw_input("Please choose to fold, check or raise: ").lower()
				if action == "fold" or action == "check" or action == "raise":
					invalid_input = False
				else:
					print
					print "Sorry, invalid input. Please try again."
					print
					time.sleep(1)
		else:
			if raised == 3:
				print
				action = raw_input("Please choose to fold or call: ").lower()
				if action == "fold" or action == "call":
					invalid_input = False
				else:
					print
					print "Sorry, invalid input. Please try again."
					print
					time.sleep(1)
			else:
				if player.bet - cpu.bet == cpu.money or cpu.bet - player.bet == player.money or player.money < cpu.bet * 2 or cpu.money < player.bet * 2:
					print
					action = raw_input("Please choose to fold or call: ").lower()
					if action == "fold" or action == "call":
						invalid_input = False
					else:
						print
						print "Sorry, invalid input. Please try again."
						print
						time.sleep(1)
				else:
					print
					action = raw_input("Please choose to fold, call or raise: ").lower()
					if action == "fold" or action == "call" or action == "raise":
						invalid_input = False
					else:
						print
						print "Sorry, invalid input. Please try again."
						print
						time.sleep(1)

def ask_for_action():
	global invalid_input
	invalid_input = True
	ask_for_action_layer()
	while invalid_input:
		ask_for_action_layer()

def print_info():
	global pot
	pot_show = pot + player.bet + cpu.bet
	print("Your hand: " + ", ".join(player.hand))
	print("Board cards: " + ", ".join(board))
	print("Your money: $" + str(player.money))
	print("Your bet: $" + str(player.bet))
	print("Computer's money: $" + str(cpu.money))
	print("Computer's bet: $" + str(cpu.bet))
	print("Pot: $" + str(pot_show))

def normal_round(starter, pre_flop_round):
	"""input 1 for pre_flop_round if it is a pre_flop round. Else input 2"""
	global action
	global checked
	global folder
	import time
	print
	print "It is now " + starter + "'s turn."
	print
	time.sleep(2)
	normal_round_layer(starter, pre_flop_round)
	if action == "fold":
		folding(starter)
		folder = starter
		return "folded"
	else:
		if action == "call":
			call(starter)
			end_round()
			return
		else:
			if action == "check":
				checking()
				if checked == pre_flop_round:
					end_round()
					return
				else:
					if starter == "player":
						return normal_round("cpu", 2)
					if starter == "cpu":
						return normal_round("player", 2)
			else:
				if action == "bet":
					betting(starter)
					if starter == "player":	
						return normal_round("cpu", 2)
					if starter == "cpu":
						return normal_round("player", 2)
				else:
					if action == "raise":
						raising(starter)
						if starter == "player":
							return normal_round("cpu", 2)
						if starter == "cpu":
							return normal_round("player", 2)

def normal_round_layer(starter, pre_flop_round):
	import time
	global action
	if starter == "player":
		print_info()
		print
		ask_for_action()
	else:
		if len(board) == 0:
			if action == "call":
				action = "check"
				print
				print "The computer has checked."
				print
				time.sleep(3)
			elif action == "raise":
				action = "call"
				print
				print "The computer has called."
				print
				time.sleep(3)
		else:
			AI()

def pre_flop_round(starter):
	import time
	global action
	print
	print "It is now " + starter + "'s turn."
	print
	time.sleep(2)
	if starter == "cpu":
		action = "call"
		print
		print "The computer has called."
		print
		time.sleep(3)
	else:
		print_info()
		print
		ask_for_action()
	if action == "call":
		starting_call(starter)
		if starter == "player":
			return normal_round("cpu", 1)
		if starter == "cpu":
			return normal_round("player", 1)
	else:
		if action == "fold":
			folding(starter)
			folder = starter
			return "folded"
		elif action == "raise":
			raising(starter)
			if starter == "player":
				return normal_round("cpu", 2)
			if starter == "cpu":
				return normal_round("player", 2)

def set(first, second):
	"""assign appropriate variables"""
	import time
	global board
	global deck
	global pot
	global raised
	global checked
	global action
	global folder
	global Small_blind
	global Big_blind
	deck = Original_deck[:]
	board = []
	pot = 0
	raised = 0
	checked = 0
	action = ""
	invalid_input = True
	folder = ""
	if first == "player":
		player.bet = Small_blind
		cpu.bet = Big_blind
	else:
		cpu.bet = Small_blind
		player.bet = Big_blind
	player.money = player.money - player.bet
	cpu.money = cpu.money - cpu.bet
	player.hand = []
	cpu.hand = []
	Card_dealer(deck, player.hand, 2)
	Card_dealer(deck, cpu.hand, 2)
	print
	"""dealing the starting hands"""
	print "Your hand has been dealt."
	time.sleep(2)
	print
	"""Pre-flop"""
	if pre_flop_round(first) == "folded":
		"""fold action"""
		if folder == "player":
			fold_end_game("player")
		else:
			fold_end_game("cpu")
		return
	else:
		"""flop"""
		Card_dealer(deck, board, 3)
		print
		print "The flop has been dealt."
		time.sleep(2)
		print
		if normal_round(second, 2) == "folded":
			"""fold action"""
			if folder == "player":
				fold_end_game("player")
			else:
				fold_end_game("cpu")
			return
		else:
			"""turn"""
			Card_dealer(deck, board, 1)
			print
			print "The turn card has been dealt."
			time.sleep(2)
			print
			if normal_round(first, 2) == "folded":
				"""fold action"""
				if folder == "player":
					fold_end_game("player")
				else:
					fold_end_game("cpu")
				return
			else:
				"""river"""
				Card_dealer(deck, board, 1)
				print
				print "The river card has been dealt."
				time.sleep(2)
				print
				if normal_round(second, 2) == "folded":
					"""fold action"""
					if folder == "player":
						fold_end_game("player")
					else:
						fold_end_game("cpu")
					return
				else:
					"""showdown"""
					print
					print "Time for the showdown!"
					print
					time.sleep(2)
					result = winner_determinator()
					print("Your hand: " + ", ".join(player.hand))
					print("CPU's hand: " + ", ".join(cpu.hand))
					print("Board cards: " + ", ".join(board))
					time.sleep(3)
					if result == "Split":
						player.money += pot / 2
						cpu.money += pot / 2
						print
						print("Your best hand: " + ", ".join(player_best_hand))
						print("CPU's best hand: " + ", ".join(cpu_best_hand))
						print
						time.sleep(1)
						print "The pot has been splited."
						time.sleep(3)
						print
					else:
						if result[0] == "input_1":
							player.money += pot
							pot = 0
							print
							print("Your best hand: " + ", ".join(player_best_hand))
							print("CPU's best hand: " + ", ".join(cpu_best_hand))
							print
							time.sleep(1)
							print "Congratulations, you have won this round with a " + result[1] + "."
							time.sleep(7)
							print
							return
						else:
							cpu.money += pot
							pot = 0
							print
							print("Your best hand: " + ", ".join(player_best_hand))
							print("CPU's best hand: " + ", ".join(cpu_best_hand))
							print
							time.sleep(1)
							print "Sorry, you have lost this round. The computer won with a " + result[1] + "."
							time.sleep(7)
							print
							return

def game():
	global Big_blind
	global turn_taker
	import time
	print
	print "Welcome to the Texas Hold'em game!"
	time.sleep(1)
	print
	input_money_amount()
	print
	input_blind_amount()
	print
	turn_taker = "player"
	while player.money > 0 and cpu.money > 0 and player.money >= Big_blind and cpu.money >= Big_blind:
		if turn_taker == "player":
			turn_taker = "cpu"
			set("player", "cpu")
		else:
			turn_taker = "player"
			set("cpu", "player")
	if player.money == 0 or player.money < Big_blind:
		print
		print "Game over, you have ran out of money."
		time.sleep(4)
		print
	elif cpu.money == 0 or cpu.money < Big_blind:
		print
		print "Congratulations, the computer has ran out of money, you have won the game!"
		time.sleep(4)
		print
	new_game = raw_input("Please type and enter new game if you wish to play another game: ").lower()
	if new_game[0] == "n":
		game()
	else:
		print
		print "Thanks for playing!"
		print
		time.sleep(2)

def fold_end_game(folder):
	import time
	if folder == "player":
		print
		print "You have folded and lost this round."
		print
	else:
		print
		print "The computer has folded and you have won this round, congratulations!"
		print
	print "Now you have $" + str(player.money) + " left."
	time.sleep(3)
	print

def winner_determinator():
	global player_best_hand
	global cpu_best_hand
	player_sevens = player.hand + board
	cpu_sevens = cpu.hand + board
	player_subsets = subset_finder(player_sevens, 5)
	cpu_subsets = subset_finder(cpu_sevens, 5)
	player_best_hand = player_subsets[0]
	for i in range(1, len(player_subsets)):
		if Higher_hand_determinator(player_best_hand, player_subsets[i])[0] == "input_2":
			player_best_hand = player_subsets[i]
	cpu_best_hand = cpu_subsets[0]
	for i in range(1, len(cpu_subsets)):
		if Higher_hand_determinator(cpu_best_hand, cpu_subsets[i])[0] == "input_2":
			cpu_best_hand = cpu_subsets[i]
	return Higher_hand_determinator(player_best_hand, cpu_best_hand)

"""Part 5: A.I."""
def AI():
	global action
	global board
	import time
	probability = winning_probability(cpu.hand, board)
	if (player.money == 0 or cpu.money == 0) and player.bet == cpu.bet:
		action = "check"
		print
		print "The computer has checked."
		print
		time.sleep(3)
	else:
		if player.bet == cpu.bet == 0:
			if probability[0] + probability[2] >= 75:
				action = "bet"
				print
			else:
				action = "check"
				print
				print "The computer has checked."
				print
				time.sleep(3)
				"""the case below considers the starting round"""
		elif player.bet == cpu.bet and not player.bet == 0:
			if player.bet - cpu.bet == cpu.money or cpu.bet - player.bet == player.money:
				if probability[0] + probability[2] >= 75:
					action = "call"
					print
					print "The computer has called."
					print
					time.sleep(3)
				else:
					action = "fold"
			else:
				if probability[0] + probability[2] >= 75:
					action = "raise"
				else:
					action = "check"
					print
					print "The computer has checked."
					print
					time.sleep(3)
		else:
			if raised == 3:
				if probability[0] + probability[2] >= 50:
					action = "call"
					print
					print "The computer has called."
					print
					time.sleep(3)
				else:
					action = "fold"
			else:
				if player.bet - cpu.bet == cpu.money or cpu.bet - player.bet == player.money or player.money < cpu.bet * 2 or cpu.money < player.bet * 2:
					if probability[0] + probability[2] >= 50:
						action = "call"
						print
						print "The computer has called."
						print
						time.sleep(3)
					else:
						action = "fold"
				else:
					if probability[0] + probability[2] >= 75:
						action = "raise"
					elif probability[0] + probability[2] >= 50 and probability[0] + probability[2] < 75:
						action = "call"
						print
						print "The computer has called."
						print
						time.sleep(3)
					else:
						action = "fold"

def opponent_possible_hands(board, remaining_cards):
	table = {}
	opponent_pocket = subset_finder(remaining_cards, 2)
	all_possible_hands = []
	for item in opponent_pocket:
		all_possible_hands.append(my_best_hand(item, board))
	for item in all_possible_hands:
		result = Hand_determinator(item)
		if result in table:
			table[result] += 1
		else:
			table[result] = 1
	return table

def opponent_all_possible_hands(board, remaining_cards):
	table = {}
	opponent_pocket = subset_finder(remaining_cards, 2)
	all_possible_hands = []
	for item in opponent_pocket:
		all_possible_hands.append(my_best_hand(item, board))
	return all_possible_hands

def my_best_hand(hand, board):
	my_sevens = hand + board
	my_subsets = subset_finder(my_sevens, 5)
	my_best = my_subsets[0]
	if len(my_subsets) == 1:
		return my_best
	else:
		for i in range(1, len(my_subsets)):
			if Higher_hand_determinator(my_best, my_subsets[i])[0] == "input_2":
				my_best = my_subsets[i]
		return my_best

def winning_ratio(my_hand, board):
	opponent_hands_table = opponent_all_possible_hands(board, deck)
	my_best = my_best_hand(my_hand, board)
	winning_ratio_table = {"win" : 0, "lose" : 0, "split" :0}
	for item in opponent_hands_table:
		result = Higher_hand_determinator(my_best, item)
		if result[0] == "input_1":
			winning_ratio_table["win"] += 1
		elif result[0] == "input_2":
			winning_ratio_table["lose"] += 1
		else:
			winning_ratio_table["split"] += 1	
	return winning_ratio_table

def winning_probability(my_hand, board):
	data = winning_ratio(my_hand, board)
	total_outcome = data["win"] + data["lose"] + data["split"]
	winning_prob = float(data["win"]) / total_outcome * 100
	losing_prob = float(data["lose"]) / total_outcome * 100
	spliting_prob = float(data["split"]) / total_outcome * 100
	return [winning_prob, losing_prob, spliting_prob]

"""Part 6: Calls"""
"""Call neccessary to start the game once the program is ran"""
game()

"""Part 7: Testers"""
"""deck = Original_deck[:]
board = []
Card_dealer(deck, cpu.hand, 2)
Card_dealer(deck, player.hand, 2)
Card_dealer(deck, board, 5)
print "Board:"
print board
print
print "cpu.hand:"
print cpu.hand
print
print "player.hand:"
print player.hand
print"""