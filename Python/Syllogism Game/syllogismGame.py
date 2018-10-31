#!/usr/bin/python3

# The Syllogism Game
# This game generates random Categorical Syllogisms
# to test the player, who must make the correct deduction
# from the two statements
import os.path
from random import *
from time import sleep
# import collection of nouns
# what would be the collective noun for a collection of nouns anyway?

# importing all nouns if pluralnounsplain.rtf is present
if os.path.isfile("pluralnounsplain.rtf"):
	noun_file = open("pluralnounsplain.rtf", "r")
	nouns = noun_file.read().strip().split(', ')
else:
	# Importing some nouns beginning with r
	nouns = ["revelations", "revelers", "revenges", "revenues", "reveres", "reverends", "reversals", "reviews", "reviewers", "revises", "revisers",  "revisions", "revivals", "revivalists", "revocations", "revokes", "revolts", "revolutions", "revolutionaries", "revolutionists", "revolvers", "revues", "revulsions", "rewards", "rewording", "rewrites", "rewriting", "rhapsodies", "rheas", "rhenium", "rheologies",  "rhetorics", "rhetoricians", "rheums", "rheumatisms", "rhinestones", "rhinitis", "rhinos", "rhinoceros", "rhizomes", "rhos", "rhodium", "rhododendrons", "rhomboids", "rhombi", "rhubarbs", "rhymes", "rhymers", "rhymesters", "rhythms", "rials", "ribs", "ribalds", "ribaldries", "ribbings", "ribbons", "riboflavins", "rices", "ricers", "riches", "richnesses", "ricks", "rickets", "rickracks", "rickshaws", "ricochets", "ricottas", "riddances", "riddles", "rides", "riders", "ridges", "ridgepoles", "ridicules", "ridiculousnesses", "ridings", "riffs", "riffles", "riffraff", "rifles", "riflemen", "rifling", "rifts", "rigs", "rigatonis", "riggers", "riggings", "rights", "righteousnesses", "rightfulnesses", "rightisms", "rightists", "rightnesses", "rigidities", "rigidnesses", "rigmaroles", "rigors"]

print("######################################")
print("###                                ###")
print("### Welcome to the Syllogism game! ###")
print("###                                ###")
print("###      specially made for        ###")
print("###      year 8 Cornerstone        ###")
print("###       at Oxley College         ###")
print("###                                ###")
print("######################################")
tally = 0
best = 0
play = True
while play:
	# choosing the three nouns
	noun1 = choice(nouns)
	noun2 = choice(nouns)
	nounJoin = choice(nouns)
	# syl_sel helps choose which style of categorical syllogism to choose
	# Universal Affirmative: both all
	# Universal Negative: both not all
	# Particular Negative: none and some
	# Particular Affirmative: all and some
	syl_sel = random()
	if syl_sel > 0.8: # universal affirmative
		majorPremise = "All " + nounJoin + " are " + noun1
		minorPremise = "All " + noun2 + " are " + nounJoin
		answer1 = "all " + noun2 + " are " + noun1
		answer2 = "all " + noun1 + " are " + noun2
	elif syl_sel > 0.6: # universal negative
		majorPremise = "No " + nounJoin + " are " + noun1
		minorPremise = "All " + noun2 + " are " + nounJoin
		answer1 = "no " + noun2 + " are " + noun1
		answer2 = "no " + noun1 + " are " + noun2
	elif syl_sel > 0.4: # particular negative
		majorPremise = "No " + nounJoin + " are " + noun1
		minorPremise = "Some " + noun2 + " are " + nounJoin
		answer1 = "some " + noun2 + " are not " + noun1
		answer2 = answer1
	else: # particular affirmative
		majorPremise = "All " + nounJoin + " are " + noun1
		minorPremise = "Some " + noun2 + " are " + nounJoin
		answer1 = "some " + noun2 + " are " + noun1
		answer2 = answer1
	print("\n")
	if random() > 0.5:
		print("1.  Rosencrantz: " + minorPremise)
		print("2.  Guildenstern: " + majorPremise)
	else:
		print("1.  Rosencrantz: " + majorPremise)
		print("2.  Guildenstern: " + minorPremise)
	print("...................................................")
	deduction = input("3.  Therefore, ")
	print("...................................................")
	if deduction == answer1 or deduction == answer2:
		print("    Correct!")
		tally = tally + 1
		if tally%5==0:
			print('\n')
			print("That's", end='')
			for k in range(10):
				print(".",end='')
				sleep(0.08)
			print(str(tally) + " correct deductions in a row!")
			if tally == 10:
				print("Are you some kind of philosopher genius?")
			elif tally == 15:
				print("Is your name Aristotle?")
			elif tally == 20:
				print("Is your name Socrates?")
			elif tally == 30:
				print("You must be Aristotle or Socrates - you are too good at this!")
	else:
		print("Not quite, " + answer1 + "!")
		best = max(best, tally)
		tally = 0
	print("\n")
	again = input("Play again? y for Yes and n for No.")
	if again == "n":
		play = False
	elif again != "y":
		print("I don't understand")
		again = input("Play again? y for Yes and n for No. ")
		if again == "n":
			play = False
		else:
			print("I'll take that as a yes.")

print("\n")
print("Thanks for playing!")
print("\n")
print("Your best score was ", best, " correct in a row.")
print("\n")
