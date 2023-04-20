# Jordan Martin
# Create a code to inform the reader about soccer
print('Hello this is Jordan Martin and this code will show you all about '
      'Soccer.')
print("Soccer was the sport I played when I was growing up all the way until"
      " I graduated high school.")
print("Soccer is a sport know all across the world and the known as the most "
      "played sport in the world.")
# Small fun fact addition that is optional
funFact1 = input("Do you want to see a fun fact?")
if funFact1 == 'Yes' or funFact1 == 'yeah' or funFact1 == 'sure' or \
        funFact1 == 'ok':
    print("In most places around the world the sport is called football")
else:
    print("Well okay than.")
# Begin to talk about how the sport is played soccer with some questions
# to keep attention
print(
    "Now let's start going over some information about how soccer is played.")
print("The sport includes 11 players who play on a team.")
gk = input("How many goalkeepers do you think soccer includes for each"
           " team on the field?")
if gk == "1":
    print("Correct")
else:
    print("No sorry the answer is 1")
print("The goalkeeper is just one position and the other positions vary "
      "position wise.")
print("An example of this is the formation 4-2-2.")
print("In this formation there are exactly 4 defenders, 4 midfielders, "
      "and 2 forwards.")
print("People who do not know soccer may not be able to read "
      "formations.")
print("The way to read formations involves the placement of the"
      " numbers.")
print("The first number is the number of defenders not including the "
      "goalkeeper which is always 1.")
print("The second number is the midfielders and the last number "
      "is the forwards.")
print("To me I think it is pretty cool the way formations are since "
      "it gives each team their own style.")
print("Well let's have a little math quiz with formations.")
Q1 = input("How much forwards are in a 4-2-4?")
# The numbers below are numeric operators which do math with +
# as addition,- as subtraction,* as multiplication
# / as division, ** for exponents, % for returning remainder,
# and // is for floor division
if Q1 == (11 - 7) or Q1 == 4:
    print("Correct")
else:
    print("The answer is 4")
Q2 = input("How about the number of defenders?")
if Q2 == (2 + 2) or Q2 == 4:
    print("Correct")
else:
    print("The answer is 4 again")
Q3 = int(input("Now for a tricky one. How many players are on the field "
               "besides the defenders?#Don't forget goalkeeper"))
if Q3 == (1 * 7) or Q3 == (14 / 2) or Q3 == 7:
    print("Correct")
else:
    print("The answer is 7 ")
print("How did you do on the quiz.", "If you did good than I'm glad you "
                                     "understand the formations.)")
print("This may seem like a lot, but this is just the start of understanding"
      " the sport.")
print("This would probably be a good time to start with the rules of soccer.",
      end='\n')
print("The rules are pretty basic, but it can get confusing if you have"
      " never played a sport.")
print("The first rule everyone should know is not to use your "
      "hands.")
print("The next rule is to keep the ball within the white lines or else the "
      "ball would be out.")
print("Next would be the offside rule which means if you are in a position "
      "behind the other teams last player you")
print("cannot receive the ball. If you get passed the ball in an offside"
      " position the other team gets the ball.")
# Using line_end so if code reaches word limit there is easy print
line_end = '\n'
print("Another important rule would be the handball rule. ")
print("This rule is one many people who don't play the sport know, and it's"
      " a quite simple rule. ")
print("The rule says that no player other than the goalkeeper can use their "
      "hands anytime besides on a throw in.")
print(line_end)
print("Even the goalkeeper is restricted with his hands as they can't pick"
      " up the ball if a teammate passes it back ")
print("and they are not allowed to touch the ball with their hand outside "
      "their box.")
print("Speaking of goalkeepers, they have special rules protecting them from"
      " getting injured. ")
print("There are multiple rules, however they can be summarized by saying if"
      " a goalkeeper is going for the ball you ")
print("not obstruct or physically stop them from there attempt to get the "
      "ball. ")
print("If the player does not follow these rules they get a foul called "
      "against them which can result in a card. ")
print("The cards represent a penalty system, and in this penalty system "
      "if u receive 2 yellow cards or 1 red card you ")
print("will get sent off.")
Value_quiz = input("So in this penalty system what is the number value of "
                   "a yellow card compared to a red card")
if not Value_quiz != 2:
    print("That is correct")
elif Value_quiz == 3 or 1:
    print("Close the answer is 2 ")
else:
    print("Incorrect, the answer is 2")
print("The cards make it important to be careful with fouls as once a player"
      " gets sent off the team plays a man down")
print("For the rest of the game, which in competitive games becomes an "
      "important liability.")
print("With the extra protection for goalkeepers if you foul them the chances "
      "of getting a card is definitely higher.")
print("Sometimes referees will take advantages of these goalkeeper rules"
      " to make difficult calls favor the goalkeeper.")
print(line_end)
print("One time when I was playing a match and the referee used "
      "the rules against me")
print("It was a game at an IMG tournament and I was playing forward "
      "for my team.")
print("When I was playing my team was pressing and challenging the "
      "other team to win the ball.")
print("My team ended up getting a dangerous loose ball a little past the "
      "half field line.")
print("The ball was also in the air so in order to win this ball I would"
      " have to head it.")
print("I proceeded to head the ball and the goalkeeper for the other team"
      " came and challenged me since the ball was ")
print("going to their side of the field and I had gotten past the defenders.")
print("I ended up getting kneed right in the face leading me to bust my "
      "lip and get stitches, however even though")
print("the rule did not apply to the goalkeeper since he was way out of"
      " his box. The other team got the foul even ")
print("though I was the one who got fouled rule wise.")
print("This shows how goalkeepers can get favoured in non favourable"
      " situations.")
print("Let's see what you remember about formations ")
Formation_quest = int(input("What is a good number for forwards in a "
                            "formation? # hint 0 is not good"))
if 4 >= Formation_quest >= 1:
    print("Great that's a good number")
else:
    print("Sorry the best amount of forwards is 1 to 4 so you have enough "
          "players for other positions")


def describe_formations():
    """
# Below is a function that will be able to remind people about formations if
it needs to be mentioned again
    """
    print("In formations it is important to understand your team before"
          " employing a specific formation.")
    print("If your team has players who are like to attack together you may "
          "want 3-4 forwards, nut if you have players")
    print("who want or are good at creating chances themselves you may want"
          " 1 forward to allow more power in other ")
    print("positions.")


describe_formations()
