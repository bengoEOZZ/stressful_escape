# First step is to import the game
import pygame
import os

# Imported random for use of the random function in the game
import random

# Defined some colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_RED = (239, 70, 64)
DARK_RED = (132,19,15)

#Initialized the game
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Giving a tile to my game
pygame.display.set_caption("Stressful Escape")

# Loops until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Here I set the all the variables needed
# Setiing the background and regular image variables while making the regular image variables have transparent backgrounds
money_image = pygame.image.load(os.path.join("images", "Money.png"))
background_image = pygame.image.load(os.path.join("images", "Background.jpg"))
fade_in_background_image_1 = pygame.image.load(os.path.join("images", "Fade-in Sick Background.jpeg"))
fade_in_background_image_2 = pygame.image.load(os.path.join("images", "Fade-in 2 Sick Background.jpeg"))
sick_background_image = pygame.image.load(os.path.join("images", "Sick Background.jpeg"))
fade_out_sick_background_image_1 = pygame.image.load(os.path.join("images", "Fade-out Sick Background.jpeg"))
fade_out_sick_background_image_2 = pygame.image.load(os.path.join("images", "Fade-out 2 Sick Background.jpeg"))
very_light_hell_background_image = pygame.image.load(os.path.join("images", "Very Light Hell Background.jpg"))
light_hell_background_image = pygame.image.load(os.path.join("images", "Light Hell Background.jpg"))
hell_background_image = pygame.image.load(os.path.join("images", "Hell Background.jpg"))
heaven_background_image = pygame.image.load(os.path.join("images", "Heaven Background.jpg"))
light_heaven_background_image = pygame.image.load(os.path.join("images", "Light Heaven Background.jpg"))
very_light_heaven_background_image = pygame.image.load(os.path.join("images", "Very Light Heaven Background.jpg"))
very_very_very_light_heaven_background_image = pygame.image.load(os.path.join("images", "Very Very Very Light Heaven Background.jpg"))
parents_image = pygame.image.load(os.path.join("images", "Parents.png"))
parents_image.set_colorkey(BLACK)
angel_parents_image = pygame.image.load(os.path.join("images", "Angel Parents.png"))
angel_parents_image.set_colorkey(BLACK)
devil_parents_image = pygame.image.load(os.path.join("images", "Devil Parents.png"))
devil_parents_image.set_colorkey(BLACK)
test_image = pygame.image.load(os.path.join("images", "Test image.png"))
test_image.set_colorkey(WHITE)
pencil_image = pygame.image.load(os.path.join("images", "Pencil.png"))
pencil_image.set_colorkey(BLACK)
five_image = pygame.image.load(os.path.join("images", "Five.png"))
five_image.set_colorkey(BLACK)
seven_image = pygame.image.load(os.path.join("images", "Seven.png"))
seven_image.set_colorkey(BLACK)
twelve_image = pygame.image.load(os.path.join("images", "Twelve.png"))
twelve_image.set_colorkey(BLACK)
correct_image = pygame.image.load(os.path.join("images", "Correct.png"))
correct_image.set_colorkey(BLACK)
incorrect_image = pygame.image.load(os.path.join("images", "Incorrect.png"))
incorrect_image.set_colorkey(BLACK)
fourteen_image = pygame.image.load(os.path.join("images", "Fourteen.png"))
fourteen_image.set_colorkey(BLACK)
nineteen_image = pygame.image.load(os.path.join("images", "Nineteen.png"))
nineteen_image.set_colorkey(BLACK)
sixteen_image = pygame.image.load(os.path.join("images", "Sixteen.png"))
sixteen_image.set_colorkey(BLACK)
twenty_four_image = pygame.image.load(os.path.join("images", "Twenty-four.png"))
twenty_four_image.set_colorkey(BLACK)
twenty_two_image = pygame.image.load(os.path.join("images", "Twenty-two.png"))
twenty_two_image.set_colorkey(BLACK)
twenty_image = pygame.image.load(os.path.join("images", "Twenty.png"))
twenty_image.set_colorkey(BLACK)
thirty_two_image = pygame.image.load(os.path.join("images", "Thirty-two.png"))
thirty_two_image.set_colorkey(BLACK)
eight_image = pygame.image.load(os.path.join("images", "Eight.png"))
eight_image.set_colorkey(BLACK)
fifty_image = pygame.image.load(os.path.join("images", "Fifty.png"))
fifty_image.set_colorkey(BLACK)
one_thousand_image = pygame.image.load(os.path.join("images", "One-Thousand.png"))
one_thousand_image.set_colorkey(BLACK)
four_image = pygame.image.load(os.path.join("images", "Four.png"))
four_image.set_colorkey(BLACK)
mr_krabs_image = pygame.image.load(os.path.join("images", "Mr.Krabs.png"))
mr_krabs_image.set_colorkey(BLACK)
spongebob_image = pygame.image.load(os.path.join("images", "Spongebob.png"))
spongebob_image.set_colorkey(BLACK)
plankton_image = pygame.image.load(os.path.join("images", "Plankton.png"))
plankton_image.set_colorkey(BLACK)
patrick_image = pygame.image.load(os.path.join("images", "Patrick.png"))
patrick_image.set_colorkey(BLACK)
eraser_image = pygame.image.load(os.path.join("images", "Eraser.png"))
eraser_image.set_colorkey(BLACK)
two_image = pygame.image.load(os.path.join("images", "Two.png"))
two_image.set_colorkey(BLACK)
three_image = pygame.image.load(os.path.join("images", "Three.png"))
three_image.set_colorkey(BLACK)
eleven_image = pygame.image.load(os.path.join("images", "Eleven.png"))
eleven_image.set_colorkey(BLACK)
one_hundred_one_image = pygame.image.load(os.path.join("images", "One Hundred and One.png"))
one_hundred_one_image.set_colorkey(BLACK)
fourty_three_image = pygame.image.load(os.path.join("images", "Fourty Three.png"))
fourty_three_image.set_colorkey(BLACK)
sixty_one_image = pygame.image.load(os.path.join("images", "Sixty One.png"))
sixty_one_image.set_colorkey(BLACK)
eighty_five_image = pygame.image.load(os.path.join("images", "Eighty Five.png"))
eighty_five_image.set_colorkey(BLACK)
one_fifty_seven_image = pygame.image.load(os.path.join("images", "One Hundred and Fifty Seven.png"))
one_fifty_seven_image.set_colorkey(BLACK)
seventeen_image = pygame.image.load(os.path.join("images", "Seventeen.png"))
seventeen_image.set_colorkey(BLACK)
glasses_image = pygame.image.load(os.path.join("images", "Glasses.png"))
glasses_image.set_colorkey(BLACK)
answer_1_image=pygame.image.load(os.path.join("images", "Question Mark.png"))
answer_2_image=pygame.image.load(os.path.join("images", "Question Mark.png"))
answer_3_image=pygame.image.load(os.path.join("images", "Question Mark.png"))
answer_4_image=pygame.image.load(os.path.join("images", "Question Mark.png"))
answer_5_image=pygame.image.load(os.path.join("images", "Question Mark.png"))
incorrect_answer_image=pygame.image.load(os.path.join("images", "Incorrect Answer.png"))
correct_answer_image=pygame.image.load(os.path.join("images", "Correct Answer.png"))

#Ser the variables for different sizes of the fonts of the text
font_1 = pygame.font.SysFont('Calibri', 50, True, False)
font_2 = pygame.font.SysFont('Calibri', 30, True, False)
font_3 = pygame.font.SysFont('Calibri', 20, True, False)
font_4 = pygame.font.SysFont('Calibri', 15, True, False)
font_5 = pygame.font.SysFont('Calibri', 100, True, False)

#Set the variables for the text for use in the game
game_over_text_1 = font_1.render("Boi, Don't exit the box.",True,WHITE)
game_over_text_2 = font_2.render("Procced to Red square to restart.",True,WHITE)
level_0_text_0 = font_2.render("Also you cannot go off the screen",True,WHITE)
level_0_text_1 = font_1.render("WELCOME TO THE GAME",True,WHITE)
level_0_text_2 = font_1.render("Arrow Keys to move",True,WHITE)
level_0_text_5 = font_2.render("Proceed to the red square to continue",True,WHITE)
level_1_text_1 = font_2.render("Hey, I know, MONEY can make you happy!",True,WHITE)
level_1_text_2 = font_2.render("Here, take some and force a smile!",True,WHITE)
level_1_text_3 = font_1.render("DaMN, ThAT Is TruLY One",True,BLACK)
level_1_text_4 = font_1.render("O WEll, AS lOng aS YOur'E",True,BLACK)
level_1_text_5 = font_2.render("I'm geting a little depressed looking",True,WHITE)
level_1_text_6 = font_2.render("Kind of feel sorry for someone so emtionless.",True,WHITE)
level_1_text_7 = font_2.render("at you.",True,WHITE)
level_1_text_8 = font_2.render("Money Makes Everyone Happy!.",True,WHITE)
level_1_text_9 = font_1.render("Ugly And Repulsive smilE.",True,BLACK)
level_1_text_10 = font_1.render("Happy, I GueSS It's OkAY",True,BLACK)
level_1_text_11 = font_2.render("Just Hurry Up And PrOceeD, i just can't",True,BLACK)
level_1_text_12 = font_2.render("stand that smile.",True,BLACK)
level_2_text_1 = font_2.render("Hey, its your parents.",True,WHITE)
level_2_text_2 = font_2.render("Looks like they want to talk to you.",True,WHITE)
level_2_text_3 = font_2.render("I say you approach them,",True,WHITE)
level_2_text_4 = font_2.render("See what they want from you.",True,WHITE)
level_2_text_5 = font_2.render("Ah. they want to see your test results.",True,WHITE)
level_2_text_6 = font_2.render("Why don't you go take the test,",True,WHITE)
level_2_text_7 = font_2.render("Ah that's right, you didn't study.",True,WHITE)
level_2_text_8 = font_2.render("O well, good luck!.",True,WHITE)
level_2_text_9 = font_3.render("There are 5 questions.",True,WHITE)
level_2_text_10 = font_3.render("Touch the correct answer",True,WHITE)
level_2_text_11 = font_3.render("with the pencil.",True,WHITE)
level_2_text_12 = font_3.render("If the pencil touches the",True,WHITE)
level_2_text_13 = font_3.render("wrong answer 3 times,",True,WHITE)
level_2_text_14 = font_3.render("then you fail the test.",True,WHITE)
level_2_text_15 = font_3.render("Grab the pencil to start.",True,WHITE)
level_2_text_15_2 = font_3.render("(Btw, your guesses ",True,WHITE)
level_2_text_15_3 = font_3.render("are always right)",True,WHITE)
level_2_text_16 = font_2.render("Question 1: 5 + 7 = ___",True,WHITE)
level_2_text_17 = font_2.render("Question 1: ",True,WHITE)
level_2_text_18 = font_2.render("Question 2: ",True,WHITE)
level_2_text_19 = font_2.render("Question 3: ",True,WHITE)
level_2_text_20 = font_2.render("Question 4: ",True,WHITE)
level_2_text_21 = font_2.render("Question 5: ",True,WHITE)
level_2_text_27 = font_2.render("Question 2: (2 x 8) + (3 x 2) = ___",True,WHITE)
level_2_text_28 = font_1.render("GUESS",True,WHITE)
level_2_text_29 = font_1.render("NEXT",True,WHITE)
level_3_text_1 = font_1.render("NEXT",True,WHITE)
next_text = font_3.render("Click NEXT to Continue",True,WHITE)
next_text_2 = font_3.render("Move pencil to NEXT",True,WHITE)
level_3_text_2 = font_2.render("Question 3: 2+2 = ___",True,WHITE)
level_3_text_3 = font_3.render("Boi, you need to stop daydreaming",True,BLACK)
level_4_text_1 = font_2.render("Question 5: Which of these isn't prime?",True,WHITE)
level_4_text_2 = font_3.render("Narrow down the answers",True,WHITE)
level_4_text_3 = font_3.render("until there is one answer",True,WHITE)
level_4_text_4 = font_3.render("left, use the eraser to erase",True,WHITE)
level_4_text_5 = font_3.render("any unnecessary or wrong",True,WHITE)
level_4_text_6 = font_3.render("answers to the question.",True,WHITE)
level_4_text_7 = font_3.render("This question confuses you.",True,WHITE)
level_4_text_8 = font_3.render("Pick up the eraser to start.",True,WHITE)
level_5_text_1 = font_4.render("You do not know the answer,",True,WHITE)
level_5_text_2 = font_4.render("Pick the glasses up to become",True,WHITE)
level_5_text_3 = font_4.render("120% more intelligent which makes",True,WHITE)
level_5_text_4 = font_4.render("you able to identify  1 wrong answer.",True,WHITE)
level_5_text_5 = font_4.render("Touch the wrong answer with the",True,WHITE)
level_5_text_6 = font_4.render("pencil to erase it and identify",True,WHITE)
level_5_text_7 = font_4.render("the next wrong answer.",True,WHITE)
level_5_text_8 = font_4.render("Continue until the answer is found.",True,WHITE)
level_5_text_9 = font_4.render("Pick up the glasses to start.",True,WHITE)
level_5_text_10 = font_2.render("Question 4: \"Something you have no idea about\"?",True,WHITE)
level_6_text_1 = font_2.render("Moment of truth, go get your test",True,WHITE)
level_6_text_2 = font_2.render("and show it to your parents",True,WHITE)
level_6_text_3 = font_2.render("OoooOOoOooh, you starting to get real nervous",True,WHITE)
level_6_text_4 = font_2.render("Your movement slows down and your",True,WHITE)
level_6_text_5 = font_2.render("controls are reversed for a short time.",True,WHITE)
level_6_text_6 = font_2.render("The sickness starts to well up inside you",True,WHITE)
level_6_text_7 = font_2.render("Looks like you getting real sick now.",True,WHITE)
level_6_text_8 = font_2.render("The sickness slowly starts to dissapear.",True,WHITE)
level_6_text_9 = font_2.render("Sickness dissapears and controls are restored.",True,WHITE)
level_6_text_10 = font_2.render("You remeber that you had failed the test.",True,WHITE)
level_6_text_11 = font_2.render("You feel like you are marching towards a sad place.",True,WHITE)
level_6_text_12 = font_2.render("You remeber that you had passed the test.",True,WHITE)
level_6_text_13 = font_2.render("You feel like you are marching towards a happy place.",True,WHITE)
end_text_1 = font_5.render("THanX",True,BLACK)
end_text_2 = font_5.render("U",True,BLACK)
end_text_3 = font_5.render("f0R",True,BLACK)
end_text_4 = font_5.render("PlaYIN",True,BLACK)

# Set functions for the drawn models
# Function for game screen model
def game_screen(screen,x,y):
    pygame.draw.rect(screen,WHITE,[x,y,400,400],10)

# Function for cursor model
def cursor(screen,x,y):
    pygame.draw.rect(screen,WHITE,[x,y,1,1])

# Function for red platform model
def next_level_platform(screen,x,y):
    pygame.draw.rect(screen,LIGHT_RED,[x,y,100,100])

# Function for user model
def user_model(screen,x,y):
    # Drawing code for head
    pygame.draw.polygon(screen, YELLOW, [[x+7.419*5,y+1.381*5], [x+8.736*5,y+1.031*5], [x+11.393*5,y+1.031*5], [x+13.603*5,y+2.275*5], [x+14.552*5,y+4.942*5], [x+14.781*5,y+7.601*5], [x+14.034*5,y+10.996*5], [x+12.414*5,y+14.204*5], [x+10.888*5,y+15.605*5], [x+9.081*5,y+15.605*5], [x+8.053*5,y+14.048*5], [x+6.278*5,y+11.961*5], [x+5.001*5,y+7.632*5], [x+5.655*5,y+4.019*5]])
    # Drawing code for eyes
    pygame.draw.polygon(screen, WHITE, [[x+8.409*5,y+3.998*5],[x+9.207*5,y+4.865*5],[x+8.271*5,y+5.801*5], [x+7.542*5,y+4.795*5]])
    pygame.draw.polygon(screen, WHITE, [[x+11.392*5,y+3.581*5],[x+12.536*5,y+4.795*5],[x+12.051*5,y+5.766*5], [x+11.392*5,y+4.483*5]])
    pygame.draw.line(screen, BLACK, [x+8.074*5,y+4.881*5], [x+8.491*5,y+4.881*5], 8)
    pygame.draw.line(screen, BLACK, [x+11.842*5,y+4.737*5], [x+12.186*5,y+4.737*5], 8)
    # Drawing code for mouth

# Function for user model with a smile
def user_model_upgraded(screen,x,y):
    # Drawing code for head
    pygame.draw.polygon(screen, YELLOW, [[x+7.419*5,y+1.381*5], [x+8.736*5,y+1.031*5], [x+11.393*5,y+1.031*5], [x+13.603*5,y+2.275*5], [x+14.552*5,y+4.942*5], [x+14.781*5,y+7.601*5], [x+14.034*5,y+10.996*5], [x+12.414*5,y+14.204*5], [x+10.888*5,y+15.605*5], [x+9.081*5,y+15.605*5], [x+8.053*5,y+14.048*5], [x+6.278*5,y+11.961*5], [x+5.001*5,y+7.632*5], [x+5.655*5,y+4.019*5]])
    # Drawing code for eyes
    pygame.draw.polygon(screen, WHITE, [[x+8.409*5,y+3.998*5],[x+9.207*5,y+4.865*5],[x+8.271*5,y+5.801*5], [x+7.542*5,y+4.795*5]])
    pygame.draw.polygon(screen, WHITE, [[x+11.392*5,y+3.581*5],[x+12.536*5,y+4.795*5],[x+12.051*5,y+5.766*5], [x+11.392*5,y+4.483*5]])
    pygame.draw.line(screen, BLACK, [x+8.074*5,y+4.881*5], [x+8.491*5,y+4.881*5], 8)
    pygame.draw.line(screen, BLACK, [x+11.842*5,y+4.737*5], [x+12.186*5,y+4.737*5], 8)
    # Drawing code for mouth
    pygame.draw.polygon(screen, DARK_RED, [[x+6.558*5,y+7.036*5],[x+8.579*5,y+9.14*5],[x+9.182*5,y+8.772*5],[x+9.74*5,y+9.11*5],[x+10.078*5,y+8.787*5],[x+10.651*5,y+9.081*5],[x+13.563*5,y+6.338*5],[x+11.268*5,y+9.419*5],[x+10.372*5,y+9.918*5],[x+9.74*5,y+9.522*5],[x+8.447*5,y+9.845*5]])
    pygame.draw.polygon(screen, DARK_RED, [[x+6.558*5,y+7.036*5],[x+8.288*5,y+11.502*5],[x+9.38*5,y+12.013*5],[x+10.522*5,y+12.013*5],[x+12.168*5,y+10.887*5],[x+13.563*5,y+6.338*5],[x+13.042*5,y+10.162*5],[x+12.305*5,y+12.596*5],[x+10.553*5,y+13.647*5],[x+9.631*5,y+13.647*5],[x+8.137*5,y+12.448*5],[x+7.381*5,y+10.807*5]])
    pygame.draw.polygon(screen, WHITE, [[x+6.558*5,y+7.036*5],[x+8.447*5,y+9.845*5],[x+9.74*5,y+9.522*5],[x+10.372*5,y+9.918*5],[x+11.268*5,y+9.419*5],[x+13.563*5,y+6.338*5],[x+12.168*5,y+10.887*5],[x+10.522*5,y+12.013*5],[x+9.38*5,y+12.013*5],[x+8.288*5,y+11.502*5]])
    pygame.draw.line(screen, BLACK, [x+7.502*5,y+8.44*5], [x+7.502*5,y+9.489*5], 2)
    pygame.draw.line(screen, BLACK, [x+8.161*5,y+9.419*5], [x+8.161*5,y+11.106*5], 2)
    pygame.draw.line(screen, BLACK, [x+9.094*5,y+9.683*5], [x+9.094*5,y+11.78*5], 2)
    pygame.draw.line(screen, BLACK, [x+10.056*5,y+9.72*5], [x+10.056*5,y+11.937*5], 2)
    pygame.draw.line(screen, BLACK, [x+10.82*5,y+9.669*5], [x+10.82*5,y+11.735*5], 2)
    pygame.draw.line(screen, BLACK, [x+11.687*5,y+8.973*5], [x+11.687*5,y+11.196*5], 2)
    pygame.draw.line(screen, BLACK, [x+12.416*5,y+7.879*5], [x+12.416*5,y+10.096*5], 2)
    pygame.draw.line(screen, BLACK, [x+7.891*5,y+10.41*5], [x+12.158*5,y+10.41*5], 2)

# Function for smiling user model with a pencil
def user_model_upgraded_with_pencil(screen,x,y):
    screen.blit(pencil_image, [x, y])
    user_model_upgraded(screen,x_pos,y_pos)

# Function for smiling user model with an eraser
def user_model_upgraded_with_eraser(screen,x,y):
    screen.blit(eraser_image, [x, y])
    user_model_upgraded(screen,x_pos,y_pos)

# Function for smiling user model with glasses
def user_model_upgraded_with_glasses(screen,x,y):
    user_model_upgraded(screen,x_pos,y_pos)
    screen.blit(glasses_image, [x+25,y+18])
    screen.blit(pencil_image, [x, y])

# Set the variables for math and logic calculations
got_test=False
x_pos = 50
y_pos = 100
x_speed = 0
y_speed = 0
level = 0
level_1_happy = False
level_2_game = False
met_parents = False
got_pencil = False
got_eraser=False
level_2_game_start = False
question_1 = False
question_2 = False
wrong_counter = 0
question_1_correct = False
question_1_incorrect = False
question_2_correct = False
question_2_incorrect = False
question_3_correct = False
question_3_incorrect = False
question_4_correct = False
question_4_incorrect = False
question_5_correct = False
question_5_incorrect = False
question_2_start=False
question_3=False
question_3_start = False
question_4 = False
question_4_start=False
question_5=False
question_5_start=False
moving_x_eight = 75
moving_y_eight = 250
moving_x_fifty=175
moving_y_fifty=250
moving_x_one_thousand=275
moving_y_one_thousand=250
moving_x_four=375
moving_y_four=250
changing_x_eight =-2
changing_y_eight =1
changing_x_fifty=-1
changing_y_fifty=1
changing_x_one_thousand=1
changing_y_one_thousand=1
changing_x_four=2
changing_y_four=1
moving_x_five = 100
moving_y_five = 100
moving_x_seven = 200
moving_y_seven = 100
moving_x_twelve = 300
moving_y_twelve = 100
changing_x_five = 2
changing_x_seven = 3
changing_x_twelve = 5
changing_y_five = 1
changing_y_seven = 4
changing_y_twelve = 5
moving_x_fourteen = 70
moving_y_fourteen = 100
moving_x_nineteen= 230
moving_y_nineteen = 100
moving_x_sixteen = 380
moving_y_sixteen = 100
moving_x_twenty_four = 380
moving_y_twenty_four = 260
moving_x_twenty_two = 380
moving_y_twenty_two = 420
moving_x_twenty = 230
moving_y_twenty = 420
moving_x_thirty_two = 70
moving_y_thirty_two = 420
moving_x_twelve_2 = 70
moving_y_twelve_2 = 260
changing_x_fourteen = -1
changing_y_fourteen =-1
changing_x_nineteen =0
changing_y_nineteen=-1
changing_x_sixteen=1
changing_y_sixteen=-1
changing_x_twenty_four=1
changing_y_twenty_four=0
changing_x_twenty_two=1
changing_y_twenty_two=1
changing_x_twenty=0
changing_y_twenty=1
changing_x_thirty_two=-1
changing_y_thirty_two=1
changing_x_twelve_2=-1
changing_y_twelve_2 =0
moving_x_two=60
moving_y_two=100
moving_x_three=110
moving_y_three=100
moving_x_five_2=60
moving_y_five_2=150
moving_x_seven_2=380
moving_y_seven_2=100
moving_x_eleven=380
moving_y_eleven=150
moving_x_one_hundred_one=330
moving_y_one_hundred_one=100
moving_x_fourty_three=60
moving_y_fourty_three=420
moving_x_sixty_one=110
moving_y_sixty_one=420
moving_x_eighty_five=60
moving_y_eighty_five=370
moving_x_nineteen_2=380
moving_y_nineteen_2=420
moving_x_one_fifty_seven=380
moving_y_one_fifty_seven=370
moving_x_seventeen=330
moving_y_seventeen=420
changing_x_two=-1
changing_y_two=-1
changing_x_three=-1
changing_y_three=-2
changing_x_five_2=-1
changing_y_five_2=-3
changing_x_seven_2=1
changing_y_seven_2=-1
changing_x_eleven=1
changing_y_eleven=-2
changing_x_one_hundred_one=1
changing_y_one_hundred_one=-3
changing_x_fourty_three=-1
changing_y_fourty_three=1
changing_x_sixty_one=-1
changing_y_sixty_one=2
changing_x_eighty_five=-1
changing_y_eighty_five=3
changing_x_nineteen_2=1
changing_y_nineteen_2=1
changing_x_one_fifty_seven=1
changing_y_one_fifty_seven=2
changing_x_seventeen=1
changing_y_seventeen=3
moving_x_answer_1=100
moving_x_answer_2=230
moving_x_answer_3=350
moving_x_answer_4=100
moving_x_answer_5=350
moving_y_answer_1=200
moving_y_answer_2=150
moving_y_answer_3=200
moving_y_answer_4=320
moving_y_answer_5=320
changing_x_answer_1=0
changing_x_answer_2=0
changing_x_answer_3=0
changing_x_answer_4=0
changing_x_answer_5=0
changing_y_answer_1=0
changing_y_answer_2=0
changing_y_answer_3=0
changing_y_answer_4=0
changing_y_answer_5=0
stop=True
test_failed=False
got_glasses=False
blit_two_image=True
blit_three_image=True
blit_five_2_image=True
blit_seven_2_image=True
blit_eleven_image=True
blit_one_hundred_one_image=True
blit_fourty_three_image=True
blit_sixty_one_image=True
blit_nineteen_2_image=True
blit_one_fifty_seven_image=True
blit_seventeen_image=True
blit_answer_1_image=False
blit_answer_2_image=False
blit_answer_3_image=False
blit_answer_4_image=False
blit_answer_5_image=False
blit_incorrect_image_1=False
blit_incorrect_image_2=False
blit_incorrect_image_3=False
blit_incorrect_image_4=False
blit_incorrect_image_5=False
erase_counter=0
question_1_next=False
question_2_next=False
question_3_next=False
question_4_next=False
question_5_next=False
fill_black=True
fill_black_2=False
blit_fade_in_background_image_1=False
blit_fade_in_background_image_2=False
blit_sick_background_image=False
blit_fade_out_sick_background_image_1=False
blit_fade_out_sick_background_image_2=False
slow_effect=False
reverse_effect=False
parents_change=False



# -------- Main Program Loop --------------#
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
            #To check if the controls or speed were affected
                # To check for the reverse effect
                if reverse_effect==True:
                    x_speed = 1
                # To check for the slow effect
                elif slow_effect==True:
                    x_speed = -1
                # Movement if there are no effects
                else:
                    x_speed = -3

            elif event.key == pygame.K_RIGHT:
            #To check if the controls or speed were affected
                # To check for the reverse effect
                if reverse_effect==True:
                    x_speed = -1
                # To check for the slow effect
                elif slow_effect==True:
                    x_speed = 1
                # Movement if there are no effects
                else:
                    x_speed = 3

            elif event.key == pygame.K_UP:
            #To check if the controls or speed were affected
                # To check for the reverse effect
                if reverse_effect==True:
                    y_speed = 1
                # To check for the slow effect
                elif slow_effect==True:
                    y_speed = -1
                # Movement if there are no effects
                else:
                    y_speed = -3

            elif event.key == pygame.K_DOWN:
            #To check if the controls or speed were affected
                # To check for the reverse effect
                if reverse_effect==True:
                    y_speed = -1
                # To check for the slow effect
                elif slow_effect==True:
                    y_speed = 1
                # Movement if there are no effects
                else:
                    y_speed = 3

        # If user let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # Variables set here needed to be inside loop
    x_pos += x_speed
    y_pos += y_speed
    mouse_pos=pygame.mouse.get_pos()
    mouse_x_pos=mouse_pos[0]
    mouse_y_pos=mouse_pos[1]

#------------------------------------------------------------------------#

    # To set the beginning level
    if level == 0:
        # Fill the screen with black
        screen.fill(BLACK)
        # Draw a red platform at a certain location
        next_level_platform(screen,300,380)
        # Blit texts at a certain location
        screen.blit(level_0_text_1, [80,50])
        screen.blit(level_0_text_2, [125,100])
        screen.blit(level_0_text_5, [120,200])
        screen.blit(level_0_text_0, [140,250])
        # To draw user model
        user_model(screen,x_pos,y_pos)
        # If user model is within these co-ordinats, then proceed to the next level
        if x_pos>250 and x_pos<400 and y_pos>380 and y_pos<420:
            level +=1
        # To reset user model if user model exits the screen
        if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
            x_pos=100
            y_pos=100

#------------------------------------------------------------------------#

    # To set the first level
    if level == 1:
        # Code for level 1 before money is taken
        if level_1_happy == False:
            # Fill the screen with black
            screen.fill(BLACK)
            # Display text on screen
            screen.blit(level_1_text_5, [90,100])
            screen.blit(level_1_text_7, [90,150])
            screen.blit(level_1_text_6, [90,200])
            screen.blit(level_1_text_1, [90,250])
            screen.blit(level_1_text_8, [90,300])
            screen.blit(level_1_text_2, [90,350])
            # Display money image on screen
            screen.blit(money_image, [550, 50])
            # Display the user model
            user_model(screen,x_pos,y_pos)
            # To prevent user model from exiting screen
            if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
                x_pos=300
                y_pos=380

        # Code for level 1 after money is taken
        else:
            # Set a background image
            screen.blit(background_image, [0, 0])
            # Display text on screen
            screen.blit(level_1_text_3, [100,100])
            screen.blit(level_1_text_4, [100,200])
            screen.blit(level_1_text_9, [100,150])
            screen.blit(level_1_text_10, [100,250])
            screen.blit(level_1_text_11, [200,350])
            screen.blit(level_1_text_12, [200,370])
            # Display next level platform
            next_level_platform(screen,100,300)
            # Display user model with a smile
            user_model_upgraded(screen,x_pos,y_pos)

        # To fill the screen with white for a quick second and change screens
        if x_pos>550 and x_pos<600 and y_pos>50 and y_pos<100 and level_1_happy==False:
            screen.fill(WHITE)
            level_1_happy=True

        # To prevent user model from leaving the screen
        if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
            x_pos=550
            y_pos=50

        # To proceed to the next level once user model is at the red platform
        if x_pos>50 and x_pos<150 and y_pos>300 and y_pos<340:
            level+=1

#------------------------------------------------------------------------#

    # To set the second level
    if level==2:
        # Fills the screen with black
        screen.fill(BLACK)
        # Code for before the user model gets to the parents model
        if met_parents==False:
            # Displays text on screen
            screen.blit(level_2_text_1, [100,50])
            screen.blit(level_2_text_2, [100,100])
            screen.blit(level_2_text_3, [100,150])
            screen.blit(level_2_text_4, [100,200])
            # Displays the parents image
            screen.blit(parents_image, [600, 400])
            # Displays the user model
            user_model_upgraded(screen,x_pos,y_pos)
            # To prevent user model from leaving the screen
            if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
                x_pos=100
                y_pos=300
            # To change screen when user model meets parents
            if x_pos>550 and x_pos<650 and y_pos>350 and y_pos<450:
                met_parents = True

        # To change screens when user meets parents and the game had not started
        elif met_parents==True and level_2_game==False:
            # Displays text on screen
            screen.blit(level_2_text_5, [100,200])
            screen.blit(level_2_text_6, [100,250])
            screen.blit(level_2_text_7, [100,300])
            screen.blit(level_2_text_8, [100,350])
            # Displays parents on screen
            screen.blit(parents_image, [600, 400])
            # Displays test image on screen
            screen.blit(test_image, [220, 100])
            # Displays the user model
            user_model_upgraded(screen,x_pos,y_pos)
            # To prevent user model from leaving the screen
            if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
                x_pos=600
                y_pos=400

        # Code for after user meets parents and picks up test
        if met_parents == True and x_pos>193 and y_pos>55 and x_pos<259 and y_pos<129:
            # Sets the game variale as true when user model picks up test
            level_2_game = True

        # Code for when the game variable is true
        if level_2_game == True:
            # Sets the background in question 3 when the numbers hit the top of the game box
            if changing_y_eight!=1:
                # Displays the background image
                screen.blit(background_image, [0, 0])
            # If its not question 3 then the screen is filled with black
            else:
                # Fills the screen with black
                screen.fill(BLACK)
                # Displays parents on screen
                screen.blit(parents_image, [600, 400])

            # Draws the game box
            game_screen(screen,50,85)
            # To check if user had picked up the pencil
            if got_pencil==False:
                # Displays pencil image
                screen.blit(pencil_image, [250, 400])
                # Displays user model
                user_model_upgraded(screen,x_pos,y_pos)
            # Checks if the user picked up the eraser
            elif got_eraser==True:
                # Displays user model with an eraser
                user_model_upgraded_with_eraser(screen,x_pos,y_pos)
            # Checks if the user had picked up glasses
            elif got_glasses==True:
                # Displays user model with glasses
                user_model_upgraded_with_glasses(screen,x_pos,y_pos)
            # Checks is the use picked up the pencil
            elif got_pencil == True:
                # Displays user model with pencil
                user_model_upgraded_with_pencil(screen,x_pos,y_pos)

            # To Start the game when user model picks up the pencil
            if x_pos>198 and y_pos>341 and x_pos<223 and y_pos<384:
                got_pencil = True
                level_2_game_start = True

            # To set the level to 100 which displays a failed game over screen and offers a retry if user leaves the box
            if x_pos>370 or x_pos<36 or y_pos>405 or y_pos<85:
                level = 100

            # To make the answers bounce around inside of the box
            if moving_x_five>=395 or moving_x_five<=56:
                changing_x_five *= -1
            if moving_x_seven>=395 or moving_x_seven<=56:
                changing_x_seven *= -1
            if moving_x_twelve>=395 or moving_x_twelve<=56:
                changing_x_twelve *= -1
            if moving_y_five>=430 or moving_y_five<=92:
                changing_y_five *= -1
            if moving_y_seven>=430 or moving_y_seven<=92:
                changing_y_seven *= -1
            if moving_y_twelve>=430 or moving_y_twelve<=92:
                changing_y_twelve *= -1

            # Code for text when game is not started
            if level_2_game_start==False:
                # Displays text on screen
                screen.blit(level_2_text_9, [470,85])
                screen.blit(level_2_text_10, [470,100])
                screen.blit(level_2_text_11, [470,115])
                screen.blit(level_2_text_12, [470,130])
                screen.blit(level_2_text_13, [470,145])
                screen.blit(level_2_text_14, [470,160])
                screen.blit(level_2_text_15, [470,200])
                screen.blit(level_2_text_15_2, [470,230])
                screen.blit(level_2_text_15_3, [470,245])
            # Code for text when game has started
            elif level_2_game_start==True:
                # Displays text on screen
                screen.blit(level_2_text_17, [500,50])
                screen.blit(level_2_text_18, [500,80])
                screen.blit(level_2_text_19, [500,110])
                screen.blit(level_2_text_20, [500,140])
                screen.blit(level_2_text_21, [500,170])

                # To display the correct and incorrect questions beside the questions when user gets a question right or wrong
                # To display the correct question 1 image
                if question_1_correct==True:
                    screen.blit(correct_image,[650,50])
                # To display the incorrect question 1 image
                elif question_1_incorrect==True:
                    screen.blit(incorrect_image,[650,50])
                # To display the correct question 2 image
                if question_2_correct==True:
                    screen.blit(correct_image,[650,80])
                # To display the incorrect question 2 image
                elif question_2_incorrect==True:
                    screen.blit(incorrect_image,[650,80])
                # To display the correct question 3 image
                if question_3_correct==True:
                    screen.blit(correct_image,[650,110])
                # To display the incorrect question 3 image
                elif question_3_incorrect==True:
                    screen.blit(incorrect_image,[650,110])
                # To display the correct question 4 image
                if question_4_correct==True:
                    screen.blit(correct_image,[650,140])
                # To display the incorrect question 4 image
                elif question_4_incorrect==True:
                    screen.blit(incorrect_image,[650,140])
                # To display the correct question 5 image
                if question_5_correct==True:
                    screen.blit(correct_image,[650,170])
                # To display the incorrect question 5 image
                elif question_5_incorrect==True:
                    screen.blit(incorrect_image,[650,170])
                #------------------------------------------------------------------------#
                # To set the screen for question 1
                if question_1 == False:
                    # To make the answeres move
                    moving_x_five -= changing_x_five
                    moving_x_seven -= changing_x_seven
                    moving_x_twelve -= changing_x_twelve
                    moving_y_five -= changing_y_five
                    moving_y_seven -= changing_y_seven
                    moving_y_twelve -= changing_y_twelve
                    # Displays text on screen
                    screen.blit(level_2_text_28, [300,100])
                    screen.blit(level_2_text_16, [50,50])
                    # Displays answer images
                    screen.blit(five_image, [moving_x_five,moving_y_five])
                    screen.blit(seven_image, [moving_x_seven,moving_y_seven])
                    screen.blit(twelve_image, [moving_x_twelve,moving_y_twelve])
                    # Code if the user touches the wrong answer five
                    if (x_pos>moving_x_five and x_pos<moving_x_five+50 and y_pos>moving_y_five and y_pos<moving_y_five+50) or (x_pos+20>moving_x_five and x_pos+20<moving_x_five+50 and y_pos+20>moving_y_five and y_pos+20<moving_y_five+50) or (x_pos+20>moving_x_five and x_pos+20<moving_x_five+50 and y_pos>moving_y_five and y_pos<moving_y_five+50) or (x_pos>moving_x_five and x_pos<moving_x_five+50 and y_pos+20>moving_y_five and y_pos+20<moving_y_five+50):
                        wrong_counter += 1
                        question_1 = True
                        question_1_incorrect=True
                    # Code if the user touches the wrong answer seven
                    if (x_pos>moving_x_seven and x_pos<moving_x_seven+50 and y_pos>moving_y_seven and y_pos<moving_y_seven+50) or (x_pos+20>moving_x_seven and x_pos+20<moving_x_seven+50 and y_pos+20>moving_y_seven and y_pos+20<moving_y_seven+50) or (x_pos+20>moving_x_seven and x_pos+20<moving_x_seven+50 and y_pos>moving_y_seven and y_pos<moving_y_seven+50) or (x_pos>moving_x_seven and x_pos<moving_x_seven+50 and y_pos+20>moving_y_seven and y_pos+20<moving_y_seven+50):
                        wrong_counter += 1
                        question_1 = True
                        question_1_incorrect = True
                    # Code if the user touches the right answer twelve
                    if (x_pos>moving_x_twelve and x_pos<moving_x_twelve+50 and y_pos>moving_y_twelve and y_pos<moving_y_twelve+50) or (x_pos+20>moving_x_twelve and x_pos+20<moving_x_twelve+50 and y_pos+20>moving_y_twelve and y_pos+20<moving_y_twelve+50) or (x_pos+20>moving_x_twelve and x_pos+20<moving_x_twelve+50 and y_pos>moving_y_twelve and y_pos<moving_y_twelve+50) or (x_pos>moving_x_twelve and x_pos<moving_x_twelve+50 and y_pos+20>moving_y_twelve and y_pos+20<moving_y_twelve+50):
                        question_1 = True
                        question_1_correct=True
                    # Code if the user touches the guess text
                    if (x_pos>298 and y_pos>100 and x_pos<438 and y_pos<128) or (x_pos+20>298 and y_pos>100 and x_pos+20<438 and y_pos<128):
                        question_1_correct=True
                        question_1=True
                #------------------------------------------------------------------------#
                # Break screen for user
                elif question_1==True and question_1_next==False:
                    # Displays text
                    screen.blit(next_text,[500,300])
                    screen.blit(level_3_text_1,[500,350])
                    # To proceed when user presses the next button
                    if (event.type==pygame.MOUSEBUTTONDOWN) and (mouse_x_pos>500 and mouse_y_pos>355 and mouse_x_pos<614 and mouse_y_pos<390):
                        question_1_next=True
                #------------------------------------------------------------------------#
                # Code for quesiton 2
                elif question_2 == False:
                    # Code to make answers bounce around inside the box
                    if moving_x_fourteen>=395 or moving_x_fourteen<=56:
                        changing_x_fourteen *= -1
                    if moving_x_nineteen>=395 or moving_x_nineteen<=56:
                        changing_x_nineteen *= -1
                    if moving_x_sixteen>=395 or moving_x_sixteen<=56:
                        changing_x_sixteen *= -1
                    if moving_x_twenty_four>=395 or moving_x_twenty_four<=56:
                        changing_x_twenty_four *= -1
                    if moving_x_twenty_two>=395 or moving_x_twenty_two<=56:
                        changing_x_twenty_two *= -1
                    if moving_x_twenty>=395 or moving_x_twenty<=56:
                        changing_x_twenty *= -1
                    if moving_x_thirty_two>=395 or moving_x_thirty_two<=56:
                        changing_x_thirty_two *= -1
                    if moving_x_twelve_2>=395 or moving_x_twelve_2<=56:
                        changing_x_twelve_2 *= -1
                    if moving_y_fourteen>=430 or moving_y_fourteen<=92:
                        changing_y_fourteen *= -1
                    if moving_y_nineteen>=430 or moving_y_nineteen<=92:
                        changing_y_nineteen *= -1
                    if moving_y_sixteen>=430 or moving_y_sixteen<=92:
                        changing_y_sixteen *= -1
                    if moving_y_twenty_four>=430 or moving_y_twenty_four<=92:
                        changing_y_twenty_four *= -1
                    if moving_y_twenty_two>=430 or moving_y_twenty_two<=92:
                        changing_y_twenty_two *= -1
                    if moving_y_twenty>=430 or moving_y_twenty<=92:
                        changing_y_twenty *= -1
                    if moving_y_thirty_two>=430 or moving_y_thirty_two<=92:
                        changing_y_thirty_two *= -1
                    if moving_y_twelve_2>=430 or moving_y_twelve_2<=92:
                        changing_y_twelve_2 *= -1

                    # Code for before the question starts
                    if question_2_start==False:
                        # Displays text
                        screen.blit(next_text_2,[500,300])
                        screen.blit(level_2_text_27, [50,50])
                        screen.blit(level_2_text_29, [200,250])
                        # To start the question when user proceeds to the next with the pencil
                        if (x_pos>200 and x_pos<310 and y_pos>250 and y_pos<280) or (x_pos+20>200 and x_pos+20<310 and y_pos+20>250 and y_pos+20<280) or (x_pos+20>200 and x_pos+20<310 and y_pos>250 and y_pos<280) or (x_pos>200 and x_pos<310 and y_pos+20>250 and y_pos+20<280):
                            question_2_start=True

                    # Code for after the question starts
                    if question_2_start==True:
                        # To move the answers around
                        moving_x_fourteen -= changing_x_fourteen
                        moving_y_fourteen -= changing_y_fourteen
                        moving_x_nineteen -= changing_x_nineteen
                        moving_y_nineteen -= changing_y_nineteen
                        moving_x_sixteen -= changing_x_sixteen
                        moving_y_sixteen -= changing_y_sixteen
                        moving_x_twenty_four -= changing_x_twenty_four
                        moving_y_twenty_four -= changing_y_twenty_four
                        moving_x_twenty_two -= changing_x_twenty_two
                        moving_y_twenty_two -= changing_y_twenty_two
                        moving_x_twenty -= changing_x_twenty
                        moving_y_twenty -= changing_y_twenty
                        moving_x_thirty_two -= changing_x_thirty_two
                        moving_y_thirty_two -= changing_y_thirty_two
                        moving_x_twelve_2 -= changing_x_twelve_2
                        moving_y_twelve_2 -= changing_y_twelve_2
                        # Displays the answer images to the screen
                        screen.blit(fourteen_image,[moving_x_fourteen,moving_y_fourteen])
                        screen.blit(nineteen_image,[moving_x_nineteen,moving_y_nineteen])
                        screen.blit(sixteen_image,[moving_x_sixteen,moving_y_sixteen])
                        screen.blit(twenty_four_image,[moving_x_twenty_four,moving_y_twenty_four])
                        screen.blit(twenty_two_image,[moving_x_twenty_two,moving_y_twenty_two])
                        screen.blit(twenty_image,[moving_x_twenty,moving_y_twenty])
                        screen.blit(thirty_two_image,[moving_x_thirty_two,moving_y_thirty_two])
                        screen.blit(twelve_image,[moving_x_twelve_2,moving_y_twelve_2])
                        # Displays a text
                        screen.blit(level_2_text_28, [300,100])
                        # Code if user touches the wrong answer fourteen
                        if (x_pos>moving_x_fourteen and x_pos<moving_x_fourteen+50 and y_pos>moving_y_fourteen and y_pos<moving_y_fourteen+50) or (x_pos+20>moving_x_fourteen and x_pos+20<moving_x_fourteen+50 and y_pos+20>moving_y_fourteen and y_pos+20<moving_y_fourteen+50) or (x_pos+20>moving_x_fourteen and x_pos+20<moving_x_fourteen+50 and y_pos>moving_y_fourteen and y_pos<moving_y_fourteen+50) or (x_pos>moving_x_fourteen and x_pos<moving_x_fourteen+50 and y_pos+20>moving_y_fourteen and y_pos+20<moving_y_fourteen+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the wrong answer nineteen
                        if (x_pos>moving_x_nineteen and x_pos<moving_x_nineteen+50 and y_pos>moving_y_nineteen and y_pos<moving_y_nineteen+50) or (x_pos+20>moving_x_nineteen and x_pos+20<moving_x_nineteen+50 and y_pos+20>moving_y_nineteen and y_pos+20<moving_y_nineteen+50) or (x_pos+20>moving_x_nineteen and x_pos+20<moving_x_nineteen+50 and y_pos>moving_y_nineteen and y_pos<moving_y_nineteen+50) or (x_pos>moving_x_nineteen and x_pos<moving_x_nineteen+50 and y_pos+20>moving_y_nineteen and y_pos+20<moving_y_nineteen+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the wrong answer sixteen
                        if (x_pos>moving_x_sixteen and x_pos<moving_x_sixteen+50 and y_pos>moving_y_sixteen and y_pos<moving_y_sixteen+50) or (x_pos+20>moving_x_sixteen and x_pos+20<moving_x_sixteen+50 and y_pos+20>moving_y_sixteen and y_pos+20<moving_y_sixteen+50) or (x_pos+20>moving_x_sixteen and x_pos+20<moving_x_sixteen+50 and y_pos>moving_y_sixteen and y_pos<moving_y_sixteen+50) or (x_pos>moving_x_sixteen and x_pos<moving_x_sixteen+50 and y_pos+20>moving_y_sixteen and y_pos+20<moving_y_sixteen+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the wrong answer twemty-four
                        if (x_pos>moving_x_twenty_four and x_pos<moving_x_twenty_four+50 and y_pos>moving_y_twenty_four and y_pos<moving_y_twenty_four+50) or (x_pos+20>moving_x_twenty_four and x_pos+20<moving_x_twenty_four+50 and y_pos+20>moving_y_twenty_four and y_pos+20<moving_y_twenty_four+50) or (x_pos+20>moving_x_twenty_four and x_pos+20<moving_x_twenty_four+50 and y_pos>moving_y_twenty_four and y_pos<moving_y_twenty_four+50) or (x_pos>moving_x_twenty_four and x_pos<moving_x_twenty_four+50 and y_pos+20>moving_y_twenty_four and y_pos+20<moving_y_twenty_four+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the right answer twenty-two
                        if (x_pos>moving_x_twenty_two and x_pos<moving_x_twenty_two+50 and y_pos>moving_y_twenty_two and y_pos<moving_y_twenty_two+50) or (x_pos+20>moving_x_twenty_two and x_pos+20<moving_x_twenty_two+50 and y_pos+20>moving_y_twenty_two and y_pos+20<moving_y_twenty_two+50) or (x_pos+20>moving_x_twenty_two and x_pos+20<moving_x_twenty_two+50 and y_pos>moving_y_twenty_two and y_pos<moving_y_twenty_two+50) or (x_pos>moving_x_twenty_two and x_pos<moving_x_twenty_two+50 and y_pos+20>moving_y_twenty_two and y_pos+20<moving_y_twenty_two+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_correct=True
                        # Code if user touches the wrong answer twenty
                        if (x_pos>moving_x_twenty and x_pos<moving_x_twenty+50 and y_pos>moving_y_twenty and y_pos<moving_y_twenty+50) or (x_pos+20>moving_x_twenty and x_pos+20<moving_x_twenty+50 and y_pos+20>moving_y_twenty and y_pos+20<moving_y_twenty+50) or (x_pos+20>moving_x_twenty and x_pos+20<moving_x_twenty+50 and y_pos>moving_y_twenty and y_pos<moving_y_twenty+50) or (x_pos>moving_x_twenty and x_pos<moving_x_twenty+50 and y_pos+20>moving_y_twenty and y_pos+20<moving_y_twenty+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the wrong answer thirty
                        if (x_pos>moving_x_thirty_two and x_pos<moving_x_thirty_two+50 and y_pos>moving_y_thirty_two and y_pos<moving_y_thirty_two+50) or (x_pos+20>moving_x_thirty_two and x_pos+20<moving_x_thirty_two+50 and y_pos+20>moving_y_thirty_two and y_pos+20<moving_y_thirty_two+50) or (x_pos+20>moving_x_thirty_two and x_pos+20<moving_x_thirty_two+50 and y_pos>moving_y_thirty_two and y_pos<moving_y_thirty_two+50) or (x_pos>moving_x_thirty_two and x_pos<moving_x_thirty_two+50 and y_pos+20>moving_y_thirty_two and y_pos+20<moving_y_thirty_two+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the wrong answer twelve
                        if (x_pos>moving_x_twelve_2 and x_pos<moving_x_twelve_2+50 and y_pos>moving_y_twelve_2 and y_pos<moving_y_twelve_2+50) or (x_pos+20>moving_x_twelve_2 and x_pos+20<moving_x_twelve_2+50 and y_pos+20>moving_y_twelve_2 and y_pos+20<moving_y_twelve_2+50) or (x_pos+20>moving_x_twelve_2 and x_pos+20<moving_x_twelve_2+50 and y_pos>moving_y_twelve_2 and y_pos<moving_y_twelve_2+50) or (x_pos>moving_x_twelve_2 and x_pos<moving_x_twelve_2+50 and y_pos+20>moving_y_twelve_2 and y_pos+20<moving_y_twelve_2+50):
                            wrong_counter += 1
                            question_2 = True
                            question_2_incorrect=True
                        # Code if user touches the guess text
                        if (x_pos>298 and y_pos>100 and x_pos<438 and y_pos<128) or (x_pos+20>298 and y_pos>100 and x_pos+20<438 and y_pos<128):
                            question_2_correct=True
                            question_2=True
                #------------------------------------------------------------------------#
                # Break screen for user
                elif question_2==True and question_2_next==False:
                    # Displays text
                    screen.blit(next_text,[500,300])
                    screen.blit(level_3_text_1,[500,350])
                    # Code for when user presses next with cursor
                    if (event.type==pygame.MOUSEBUTTONDOWN) and (mouse_x_pos>500 and mouse_y_pos>355 and mouse_x_pos<614 and mouse_y_pos<390):
                        question_2_next=True
                #------------------------------------------------------------------------#
                # Code for quesion 3
                elif question_3==False:
                    # Code for before question starts
                    if question_3_start==False:
                        # Displays text
                        screen.blit(next_text_2,[500,300])
                        screen.blit(level_3_text_1, [200,360])
                    # Displays the quesiton text
                    screen.blit(level_3_text_2, [50,50])

                    # Code to make sure answers bounce around in the box
                    if moving_x_eight>=395 or moving_x_eight<=56:
                        changing_x_eight *= -1
                    if moving_x_fifty>=395 or moving_x_fifty<=56:
                        changing_x_fifty *= -1
                    if moving_x_one_thousand>=395 or moving_x_one_thousand<=56:
                        changing_x_one_thousand *= -1
                    if moving_x_four>=395 or moving_x_four<=56:
                        changing_x_four *= -1
                    if moving_y_eight>=430 or moving_y_eight<=92:
                        changing_y_eight *= -1
                    if moving_y_fifty>=430 or moving_y_fifty<=92:
                        changing_y_fifty *= -1
                    if moving_y_one_thousand>=430 or moving_y_one_thousand<=92:
                        changing_y_one_thousand *= -1
                    if moving_y_four>=430 or moving_y_four<=92:
                        changing_y_four *= -1

                    # Code for when user is on top of the next button
                    if (x_pos>200 and y_pos>365 and x_pos<315 and y_pos<400) or (x_pos+20>200 and y_pos>365 and x_pos+20<315 and y_pos<400) or (x_pos>200 and y_pos+20>365 and x_pos<315 and y_pos+20<400) or (x_pos+20>200 and y_pos+20>365 and x_pos+20<315 and y_pos+20<400):
                            question_3_start=True

                    # Code for when the question starts
                    if question_3_start==True:
                        # Code to move answer images
                        moving_x_eight -= changing_x_eight
                        moving_x_fifty -= changing_x_fifty
                        moving_x_one_thousand -= changing_x_one_thousand
                        moving_x_four -= changing_x_four
                        moving_y_eight -= changing_y_eight
                        moving_y_fifty -= changing_y_fifty
                        moving_y_one_thousand -= changing_y_one_thousand
                        moving_y_four -= changing_y_four
                        # Displays a text
                        screen.blit(level_2_text_28, [300,100])
                        # To display eight image when normal
                        if changing_y_eight==1:
                            screen.blit(eight_image,[moving_x_eight,moving_y_eight])
                        # To Display Mr.Krabs when daydreaming
                        else:
                            screen.blit(mr_krabs_image,[moving_x_eight,moving_y_eight])
                            screen.blit(level_3_text_3,[100,400])
                        # To display fifty image when normal
                        if changing_y_fifty==1:
                            screen.blit(fifty_image,[moving_x_fifty,moving_y_fifty])
                        # To display Spongebob image when daydreaming
                        else:
                            screen.blit(spongebob_image,[moving_x_fifty,moving_y_fifty])
                        # To display One thousand image when normal
                        if changing_y_one_thousand==1:
                            screen.blit(one_thousand_image,[moving_x_one_thousand,moving_y_one_thousand])
                        # To display plankton image when daydreaming
                        else:
                            screen.blit(plankton_image,[moving_x_one_thousand,moving_y_one_thousand])
                        # To display four image when normal
                        if changing_y_four==1:
                            screen.blit(four_image,[moving_x_four,moving_y_four])
                        # To display patrick image when daydreaming
                        else:
                            screen.blit(patrick_image,[moving_x_four,moving_y_four])

                        # Code when pencil touches guess text
                        if (x_pos>298 and y_pos>100 and x_pos<438 and y_pos<128) or (x_pos+20>298 and y_pos>100 and x_pos+20<438 and y_pos<128):
                            question_3_correct=True
                            question_3=True
                            changing_y_eight=1
                        # Code when pencil touches wrong answer eight
                        if (x_pos>moving_x_eight and x_pos<moving_x_eight+50 and y_pos>moving_y_eight and y_pos<moving_y_eight+50) or (x_pos+20>moving_x_eight and x_pos+20<moving_x_eight+50 and y_pos+20>moving_y_eight and y_pos+20<moving_y_eight+50) or (x_pos+20>moving_x_eight and x_pos+20<moving_x_eight+50 and y_pos>moving_y_eight and y_pos<moving_y_eight+50) or (x_pos>moving_x_eight and x_pos<moving_x_eight+50 and y_pos+20>moving_y_eight and y_pos+20<moving_y_eight+50):
                            wrong_counter += 1
                            question_3 = True
                            question_3_incorrect=True
                            # Code to make sure screen does not stay as the background
                            changing_y_eight=1
                        # Code when pencil touches wrong answer fifty
                        if (x_pos>moving_x_fifty and x_pos<moving_x_fifty+50 and y_pos>moving_y_fifty and y_pos<moving_y_fifty+50) or (x_pos+20>moving_x_fifty and x_pos+20<moving_x_fifty+50 and y_pos+20>moving_y_fifty and y_pos+20<moving_y_fifty+50) or (x_pos+20>moving_x_fifty and x_pos+20<moving_x_fifty+50 and y_pos>moving_y_fifty and y_pos<moving_y_fifty+50) or (x_pos>moving_x_fifty and x_pos<moving_x_fifty+50 and y_pos+20>moving_y_fifty and y_pos+20<moving_y_fifty+50):
                            wrong_counter += 1
                            question_3 = True
                            question_3_incorrect=True
                            # Code to make sure screen does not stay as the background
                            changing_y_eight=1
                        # Code when pencil touches wrong answer one thousand
                        if (x_pos>moving_x_one_thousand and x_pos<moving_x_one_thousand+50 and y_pos>moving_y_one_thousand and y_pos<moving_y_one_thousand+50) or (x_pos+20>moving_x_one_thousand and x_pos+20<moving_x_one_thousand+50 and y_pos+20>moving_y_one_thousand and y_pos+20<moving_y_one_thousand+50) or (x_pos+20>moving_x_one_thousand and x_pos+20<moving_x_one_thousand+50 and y_pos>moving_y_one_thousand and y_pos<moving_y_one_thousand+50) or (x_pos>moving_x_one_thousand and x_pos<moving_x_one_thousand+50 and y_pos+20>moving_y_one_thousand and y_pos+20<moving_y_one_thousand+50):
                            wrong_counter += 1
                            question_3 = True
                            question_3_incorrect=True
                            # Code to make sure screen does not stay as the background
                            changing_y_eight=1
                        # Code when pencil touches right answer four
                        if (x_pos>moving_x_four and x_pos<moving_x_four+50 and y_pos>moving_y_four and y_pos<moving_y_four+50) or (x_pos+20>moving_x_four and x_pos+20<moving_x_four+50 and y_pos+20>moving_y_four and y_pos+20<moving_y_four+50) or (x_pos+20>moving_x_four and x_pos+20<moving_x_four+50 and y_pos>moving_y_four and y_pos<moving_y_four+50) or (x_pos>moving_x_four and x_pos<moving_x_four+50 and y_pos+20>moving_y_four and y_pos+20<moving_y_four+50):
                            wrong_counter += 1
                            question_3 = True
                            question_3_correct=True
                            # Code to make sure screen does not stay as the background
                            changing_y_eight=1
                #------------------------------------------------------------------------#
                # Break screen for user
                elif question_3==True and question_3_next==False:
                    # Displays text
                    screen.blit(next_text,[500,300])
                    screen.blit(level_3_text_1,[500,350])
                    # Code for when the user preses the next button
                    if (event.type==pygame.MOUSEBUTTONDOWN) and (mouse_x_pos>500 and mouse_y_pos>355 and mouse_x_pos<614 and mouse_y_pos<390):
                        question_3_next=True
                #------------------------------------------------------------------------#
                # Code for question 4
                elif question_4==False:
                    # Code to display the images as question marks when glasses is not worn or before the next x image was touched
                    # Displays the incorrect and correct answers after glasses is worn
                    if blit_answer_1_image==False:
                        screen.blit(answer_1_image,[moving_x_answer_1,moving_y_answer_1])
                    elif blit_answer_1_image==True and blit_incorrect_image_1==False:
                        screen.blit(incorrect_answer_image,[moving_x_answer_1,moving_y_answer_1])
                    if blit_answer_2_image==False:
                        screen.blit(answer_2_image,[moving_x_answer_2,moving_y_answer_2])
                    elif blit_answer_2_image==True and blit_incorrect_image_2==False:
                        screen.blit(incorrect_answer_image,[moving_x_answer_2,moving_y_answer_2])
                    if blit_answer_3_image==False:
                        screen.blit(answer_3_image,[moving_x_answer_3,moving_y_answer_3])
                    elif blit_answer_3_image==True and blit_incorrect_image_3==False:
                        screen.blit(correct_answer_image,[moving_x_answer_3,moving_y_answer_3])
                    if blit_answer_4_image==False:
                        screen.blit(answer_4_image,[moving_x_answer_4,moving_y_answer_4])
                    elif blit_answer_4_image==True and blit_incorrect_image_4==False:
                        screen.blit(incorrect_answer_image,[moving_x_answer_4,moving_y_answer_4])
                    if blit_answer_5_image==False:
                        screen.blit(answer_5_image,[moving_x_answer_5,moving_y_answer_5])
                    elif blit_answer_5_image==True and blit_incorrect_image_5==False:
                        screen.blit(incorrect_answer_image,[moving_x_answer_5,moving_y_answer_5])

                    # To reset the images in the corner is they exit the box
                    if moving_x_answer_1>=395 or moving_x_answer_1<=56:
                        moving_x_answer_1=70
                    if moving_y_answer_1>=430 or moving_y_answer_1<=92:
                        moving_y_answer_1=100
                    if moving_x_answer_2>=395 or moving_x_answer_2<=56:
                        moving_x_answer_2=230
                    if moving_y_answer_2>=430 or moving_y_answer_2<=92:
                        moving_y_answer_2=100
                    if moving_x_answer_3>=395 or moving_x_answer_3<=56:
                        moving_x_answer_3=380
                    if moving_y_answer_3>=430 or moving_y_answer_3<=92:
                        moving_y_answer_3=100
                    if moving_x_answer_4>=395 or moving_x_answer_4<=56:
                        moving_x_answer_4=70
                    if moving_y_answer_4>=430 or moving_y_answer_4<=92:
                        moving_y_answer_4=420
                    if moving_x_answer_5>=395 or moving_x_answer_5<=56:
                        moving_x_answer_5=380
                    if moving_y_answer_5>=430 or moving_y_answer_5<=92:
                        moving_y_answer_5=420

                    # To draw a black rectangle to cover up the questions
                    pygame.draw.rect(screen,BLACK,[495,45,250,230])
                    # Displays text over the black box
                    screen.blit(level_5_text_1,[465,100])
                    screen.blit(level_5_text_2,[465,125])
                    screen.blit(level_5_text_3,[465,150])
                    screen.blit(level_5_text_4,[465,175])
                    screen.blit(level_5_text_5,[465,200])
                    screen.blit(level_5_text_6,[465,225])
                    screen.blit(level_5_text_7,[465,250])
                    screen.blit(level_5_text_8,[465,300])
                    screen.blit(level_5_text_9,[465,325])
                    screen.blit(level_5_text_10, [50,50])

                    # To move the images in a random generated pattern
                    moving_x_answer_1 -= changing_x_answer_1
                    moving_y_answer_1 -= changing_y_answer_1
                    moving_x_answer_2 -= changing_x_answer_2
                    moving_y_answer_2 -= changing_y_answer_2
                    moving_x_answer_3 -= changing_x_answer_3
                    moving_y_answer_3 -= changing_y_answer_3
                    moving_x_answer_4 -= changing_x_answer_4
                    moving_y_answer_4 -= changing_y_answer_4
                    moving_x_answer_5 -= changing_x_answer_5
                    moving_y_answer_5 -= changing_y_answer_5

                    # Code for before question starts
                    if question_4_start==False:
                        # Dis[;ays glasses
                        screen.blit(glasses_image,[240,350])
                        # Code for when user picks up glasses
                        if x_pos>190 and y_pos>265 and x_pos<275 and y_pos<335:
                            question_4_start=True
                            blit_answer_1_image=True
                            got_glasses=True

                    # Code for when question 4 starts
                    if question_4_start==True:
                        # Set the changing answers from 0 to random genereated numbers so they start to move after question starts
                        changing_x_answer_1=random.randint(-5,5)
                        changing_x_answer_2=random.randint(-5,5)
                        changing_x_answer_3=random.randint(-5,5)
                        changing_x_answer_4=random.randint(-5,5)
                        changing_x_answer_5=random.randint(-5,5)
                        changing_y_answer_1=random.randint(-5,5)
                        changing_y_answer_2=random.randint(-5,5)
                        changing_y_answer_3=random.randint(-5,5)
                        changing_y_answer_4=random.randint(-5,5)
                        changing_y_answer_5=random.randint(-5,5)

                        # Code for when the pencil touches answer 1 as an x
                        if ((x_pos>moving_x_answer_1 and x_pos<moving_x_answer_1+50 and y_pos>moving_y_answer_1 and y_pos<moving_y_answer_1+50) or (x_pos+20>moving_x_answer_1 and x_pos+20<moving_x_answer_1+50 and y_pos+20>moving_y_answer_1 and y_pos+20<moving_y_answer_1+50) or (x_pos+20>moving_x_answer_1 and x_pos+20<moving_x_answer_1+50 and y_pos>moving_y_answer_1 and y_pos<moving_y_answer_1+50) or (x_pos>moving_x_answer_1 and x_pos<moving_x_answer_1+50 and y_pos+20>moving_y_answer_1 and y_pos+20<moving_y_answer_1+50)) and blit_answer_1_image==True:
                            # Sets question 4 as the next answer to be touched
                            blit_answer_4_image=True
                            # Removes answer 1 from display
                            blit_incorrect_image_1=True
                        # Code for when the pencil touches the answer 1 as a question mark
                        elif (x_pos>moving_x_answer_1 and x_pos<moving_x_answer_1+50 and y_pos>moving_y_answer_1 and y_pos<moving_y_answer_1+50) or (x_pos+20>moving_x_answer_1 and x_pos+20<moving_x_answer_1+50 and y_pos+20>moving_y_answer_1 and y_pos+20<moving_y_answer_1+50) or (x_pos+20>moving_x_answer_1 and x_pos+20<moving_x_answer_1+50 and y_pos>moving_y_answer_1 and y_pos<moving_y_answer_1+50) or (x_pos>moving_x_answer_1 and x_pos<moving_x_answer_1+50 and y_pos+20>moving_y_answer_1 and y_pos+20<moving_y_answer_1+50):
                            question_4=True
                            question_4_incorrect=True
                            wrong_counter=+1

                        # Code for when the pencil touches answer 2 as an x
                        if ((x_pos>moving_x_answer_2 and x_pos<moving_x_answer_2+50 and y_pos>moving_y_answer_2 and y_pos<moving_y_answer_2+50) or (x_pos+20>moving_x_answer_2 and x_pos+20<moving_x_answer_2+50 and y_pos+20>moving_y_answer_2 and y_pos+20<moving_y_answer_2+50) or (x_pos+20>moving_x_answer_2 and x_pos+20<moving_x_answer_2+50 and y_pos>moving_y_answer_2 and y_pos<moving_y_answer_2+50) or (x_pos>moving_x_answer_2 and x_pos<moving_x_answer_2+50 and y_pos+20>moving_y_answer_2 and y_pos+20<moving_y_answer_2+50)) and blit_answer_2_image==True:
                            # Sets question 5 as the next answer to be touched
                            blit_answer_5_image=True
                            # Removes answer 2 from display
                            blit_incorrect_image_2=True
                        # Code for when the pencil touches the answer 2 as a question mark
                        elif (x_pos>moving_x_answer_2 and x_pos<moving_x_answer_2+50 and y_pos>moving_y_answer_2 and y_pos<moving_y_answer_2+50) or (x_pos+20>moving_x_answer_2 and x_pos+20<moving_x_answer_2+50 and y_pos+20>moving_y_answer_2 and y_pos+20<moving_y_answer_2+50) or (x_pos+20>moving_x_answer_2 and x_pos+20<moving_x_answer_2+50 and y_pos>moving_y_answer_2 and y_pos<moving_y_answer_2+50) or (x_pos>moving_x_answer_2 and x_pos<moving_x_answer_2+50 and y_pos+20>moving_y_answer_2 and y_pos+20<moving_y_answer_2+50):
                            question_4=True
                            question_4_incorrect=True
                            wrong_counter=+1

                        # Code for when the pencil touches answer 3 as the final answer
                        if ((x_pos>moving_x_answer_3 and x_pos<moving_x_answer_3+50 and y_pos>moving_y_answer_3 and y_pos<moving_y_answer_3+50) or (x_pos+20>moving_x_answer_3 and x_pos+20<moving_x_answer_3+50 and y_pos+20>moving_y_answer_3 and y_pos+20<moving_y_answer_3+50) or (x_pos+20>moving_x_answer_3 and x_pos+20<moving_x_answer_3+50 and y_pos>moving_y_answer_3 and y_pos<moving_y_answer_3+50) or (x_pos>moving_x_answer_3 and x_pos<moving_x_answer_3+50 and y_pos+20>moving_y_answer_3 and y_pos+20<moving_y_answer_3+50)) and blit_answer_3_image==True:
                            question_4=True
                            question_4_correct=True
                        # Code for when the pencil touches the answer 3 as a question mark
                        elif (x_pos>moving_x_answer_3 and x_pos<moving_x_answer_3+50 and y_pos>moving_y_answer_3 and y_pos<moving_y_answer_3+50) or (x_pos+20>moving_x_answer_3 and x_pos+20<moving_x_answer_3+50 and y_pos+20>moving_y_answer_3 and y_pos+20<moving_y_answer_3+50) or (x_pos+20>moving_x_answer_3 and x_pos+20<moving_x_answer_3+50 and y_pos>moving_y_answer_3 and y_pos<moving_y_answer_3+50) or (x_pos>moving_x_answer_3 and x_pos<moving_x_answer_3+50 and y_pos+20>moving_y_answer_3 and y_pos+20<moving_y_answer_3+50):
                            question_4=True
                            question_4_incorrect=True
                            wrong_counter=+1

                        # Code for when the pencil touches answer 4 as an x
                        if ((x_pos>moving_x_answer_4 and x_pos<moving_x_answer_4+50 and y_pos>moving_y_answer_4 and y_pos<moving_y_answer_4+50) or (x_pos+20>moving_x_answer_4 and x_pos+20<moving_x_answer_4+50 and y_pos+20>moving_y_answer_4 and y_pos+20<moving_y_answer_4+50) or (x_pos+20>moving_x_answer_4 and x_pos+20<moving_x_answer_4+50 and y_pos>moving_y_answer_4 and y_pos<moving_y_answer_4+50) or (x_pos>moving_x_answer_4 and x_pos<moving_x_answer_4+50 and y_pos+20>moving_y_answer_4 and y_pos+20<moving_y_answer_4+50)) and blit_answer_4_image==True:
                            # Sets question 2 as the next answer to be touched
                            blit_answer_2_image=True
                            # Removes answer 4 from display
                            blit_incorrect_image_4=True
                        # Code for when the pencil touches the answer 4 as a question mark
                        elif (x_pos>moving_x_answer_4 and x_pos<moving_x_answer_4+50 and y_pos>moving_y_answer_4 and y_pos<moving_y_answer_4+50) or (x_pos+20>moving_x_answer_4 and x_pos+20<moving_x_answer_4+50 and y_pos+20>moving_y_answer_4 and y_pos+20<moving_y_answer_4+50) or (x_pos+20>moving_x_answer_4 and x_pos+20<moving_x_answer_4+50 and y_pos>moving_y_answer_4 and y_pos<moving_y_answer_4+50) or (x_pos>moving_x_answer_4 and x_pos<moving_x_answer_4+50 and y_pos+20>moving_y_answer_4 and y_pos+20<moving_y_answer_4+50):
                            question_4=True
                            question_4_incorrect=True
                            wrong_counter=+1

                        # Code for when the pencil touches answer 5 as an x
                        if ((x_pos>moving_x_answer_5 and x_pos<moving_x_answer_5+50 and y_pos>moving_y_answer_5 and y_pos<moving_y_answer_5+50) or (x_pos+20>moving_x_answer_5 and x_pos+20<moving_x_answer_5+50 and y_pos+20>moving_y_answer_5 and y_pos+20<moving_y_answer_5+50) or (x_pos+20>moving_x_answer_5 and x_pos+20<moving_x_answer_5+50 and y_pos>moving_y_answer_5 and y_pos<moving_y_answer_5+50) or (x_pos>moving_x_answer_5 and x_pos<moving_x_answer_5+50 and y_pos+20>moving_y_answer_5 and y_pos+20<moving_y_answer_5+50)) and blit_answer_5_image==True:
                            # Sets answer 3 as the next answer to be touched
                            blit_answer_3_image=True
                            # Removes answer 5 from display
                            blit_incorrect_image_5=True
                        # Code for when the pencil touches answer 5 as a questoin mark
                        elif (x_pos>moving_x_answer_5 and x_pos<moving_x_answer_5+50 and y_pos>moving_y_answer_5 and y_pos<moving_y_answer_5+50) or (x_pos+20>moving_x_answer_5 and x_pos+20<moving_x_answer_5+50 and y_pos+20>moving_y_answer_5 and y_pos+20<moving_y_answer_5+50) or (x_pos+20>moving_x_answer_5 and x_pos+20<moving_x_answer_5+50 and y_pos>moving_y_answer_5 and y_pos<moving_y_answer_5+50) or (x_pos>moving_x_answer_5 and x_pos<moving_x_answer_5+50 and y_pos+20>moving_y_answer_5 and y_pos+20<moving_y_answer_5+50):
                            question_4=True
                            question_4_incorrect=True
                            wrong_counter=+1
                #------------------------------------------------------------------------#
                # Break screen for user
                elif question_4==True and question_4_next==False:
                    # Remove glasses from user model
                    got_glasses=False
                    # Display text
                    screen.blit(next_text,[500,300])
                    screen.blit(level_3_text_1,[500,350])
                    # Code for when user presses the next button
                    if (event.type==pygame.MOUSEBUTTONDOWN) and (mouse_x_pos>500 and mouse_y_pos>355 and mouse_x_pos<614 and mouse_y_pos<390):
                        question_4_next=True
                #------------------------------------------------------------------------#
                # Code for question 5
                elif question_5==False:
                    # To display a black rectangle over the questoins
                    pygame.draw.rect(screen,BLACK,[495,45,250,230])
                    # Displays text
                    screen.blit(level_4_text_1,[50,50])
                    screen.blit(level_4_text_2,[465,100])
                    screen.blit(level_4_text_3,[465,150])
                    screen.blit(level_4_text_4,[465,200])
                    screen.blit(level_4_text_5,[465,250])
                    screen.blit(level_4_text_6,[465,300])
                    screen.blit(level_4_text_8,[465,375])
                    # Code for before question 5 starts
                    if question_5_start==False:
                        # Display eraser image
                        screen.blit(eraser_image,[250,260])
                        # Changes screem when user model gets eraser
                        if x_pos>195 and y_pos>204 and x_pos<227 and y_pos<245:
                            got_eraser=True
                            question_5_start=True

                    # Code to make sure answers bounce around inside of the rectangle
                    if moving_x_two>=395 or moving_x_two<=56:
                        changing_x_two *= -1
                    if moving_y_two>=430 or moving_y_two<=92:
                        changing_y_two *= -1
                    if moving_x_three>=395 or moving_x_three<=56:
                        changing_x_three *= -1
                    if moving_y_three>=430 or moving_y_three<=92:
                        changing_y_three *= -1
                    if moving_x_five_2>=395 or moving_x_five_2<=56:
                       changing_x_five_2 *= -1
                    if moving_y_five_2>=430 or moving_y_five_2<=92:
                        changing_y_five_2 *= -1
                    if moving_x_seven_2>=395 or moving_x_seven_2<=56:
                       changing_x_seven_2 *= -1
                    if moving_y_seven_2>=430 or moving_y_seven_2<=92:
                       changing_y_seven_2 *= -1
                    if moving_x_eleven>=395 or moving_x_eleven<=56:
                        changing_x_eleven *= -1
                    if moving_y_eleven>=430 or moving_y_eleven<=92:
                        changing_y_eleven *= -1
                    if moving_x_one_hundred_one>=395 or moving_x_one_hundred_one<=56:
                        changing_x_one_hundred_one *= -1
                    if moving_y_one_hundred_one>=430 or moving_y_one_hundred_one<=92:
                        changing_y_one_hundred_one *= -1
                    if moving_x_fourty_three>=395 or moving_x_fourty_three<=56:
                        changing_x_fourty_three *= -1
                    if moving_y_fourty_three>=430 or moving_y_fourty_three<=92:
                        changing_y_fourty_three *= -1
                    if moving_x_sixty_one>=395 or moving_x_sixty_one<=56:
                       changing_x_sixty_one *= -1
                    if moving_y_sixty_one>=430 or moving_y_sixty_one<=92:
                        changing_y_sixty_one *= -1
                    if moving_x_eighty_five>=395 or moving_x_eighty_five<=56:
                        changing_x_eighty_five *= -1
                    if moving_y_eighty_five>=430 or moving_y_eighty_five<=92:
                        changing_y_eighty_five *= -1
                    if moving_x_nineteen_2>=395 or moving_x_nineteen_2<=56:
                        changing_x_nineteen_2 *= -1
                    if moving_y_nineteen_2>=430 or moving_y_nineteen_2<=92:
                        changing_y_nineteen_2 *= -1
                    if moving_x_one_fifty_seven>=395 or moving_x_one_fifty_seven<=56:
                        changing_x_one_fifty_seven *= -1
                    if moving_y_one_fifty_seven>=430 or moving_y_one_fifty_seven<=92:
                        changing_y_one_fifty_seven *= -1
                    if moving_x_seventeen>=395 or moving_x_seventeen<=56:
                        changing_x_seventeen *= -1
                    if moving_y_seventeen>=430 or moving_y_seventeen<=92:
                        changing_y_seventeen *= -1

                    # Code for when question 5 starts
                    if question_5_start==True:
                        # Code to move the images
                        moving_x_two -= changing_x_two
                        moving_x_three -= changing_x_three
                        moving_x_five_2 -= changing_x_five_2
                        moving_x_seven_2 -= changing_x_seven_2
                        moving_x_eleven -= changing_x_eleven
                        moving_x_one_hundred_one -= changing_x_one_hundred_one
                        moving_x_fourty_three -= changing_x_fourty_three
                        moving_x_sixty_one -= changing_x_sixty_one
                        moving_x_eighty_five -= changing_x_eighty_five
                        moving_x_nineteen_2 -= changing_x_nineteen_2
                        moving_x_one_fifty_seven -= changing_x_one_fifty_seven
                        moving_x_seventeen -= changing_x_seventeen
                        moving_y_two -= changing_y_two
                        moving_y_three -= changing_y_three
                        moving_y_five_2 -= changing_y_five_2
                        moving_y_seven_2 -= changing_y_seven_2
                        moving_y_eleven -= changing_y_eleven
                        moving_y_one_hundred_one -= changing_y_one_hundred_one
                        moving_y_fourty_three -= changing_y_fourty_three
                        moving_y_sixty_one -= changing_y_sixty_one
                        moving_y_eighty_five -= changing_y_eighty_five
                        moving_y_nineteen_2 -= changing_y_nineteen_2
                        moving_y_one_fifty_seven -= changing_y_one_fifty_seven
                        moving_y_seventeen -= changing_y_seventeen
                        # Always display the eighty-five image as it is the answer
                        screen.blit(eighty_five_image,[moving_x_eighty_five,moving_y_eighty_five])
                        # Code to erase the images when touched
                        if blit_two_image==True:
                            screen.blit(two_image,[moving_x_two,moving_y_two])
                        if blit_three_image==True:
                            screen.blit(three_image,[moving_x_three,moving_y_three])
                        if blit_five_2_image==True:
                            screen.blit(five_image,[moving_x_five_2,moving_y_five_2])
                        if blit_seven_2_image==True:
                            screen.blit(seven_image,[moving_x_seven_2,moving_y_seven_2])
                        if blit_eleven_image==True:
                            screen.blit(eleven_image,[moving_x_eleven,moving_y_eleven])
                        if blit_one_hundred_one_image==True:
                            screen.blit(one_hundred_one_image,[moving_x_one_hundred_one,moving_y_one_hundred_one])
                        if blit_fourty_three_image==True:
                            screen.blit(fourty_three_image,[moving_x_fourty_three,moving_y_fourty_three])
                        if blit_sixty_one_image==True:
                            screen.blit(sixty_one_image,[moving_x_sixty_one,moving_y_sixty_one])
                        if blit_nineteen_2_image==True:
                            screen.blit(nineteen_image,[moving_x_nineteen_2,moving_y_nineteen_2])
                        if blit_one_fifty_seven_image==True:
                            screen.blit(one_fifty_seven_image,[moving_x_one_fifty_seven,moving_y_one_fifty_seven])
                        if blit_seventeen_image==True:
                            screen.blit(seventeen_image,[moving_x_seventeen,moving_y_seventeen])

                        # Code if eighty-five is touched
                        if (x_pos>moving_x_eighty_five and x_pos<moving_x_eighty_five+50 and y_pos>moving_y_eighty_five and y_pos<moving_y_eighty_five+50) or (x_pos+20>moving_x_eighty_five and x_pos+20<moving_x_eighty_five+50 and y_pos+20>moving_y_eighty_five and y_pos+20<moving_y_eighty_five+50) or (x_pos+20>moving_x_eighty_five and x_pos+20<moving_x_eighty_five+50 and y_pos>moving_y_eighty_five and y_pos<moving_y_eighty_five+50) or (x_pos>moving_x_eighty_five and x_pos<moving_x_eighty_five+50 and y_pos+20>moving_y_eighty_five and y_pos+20<moving_y_eighty_five+50):
                            question_5=True
                            question_5_incorrect=True
                            wrong_counter=+1
                        # Code to make the question correct when every other aside from eighty-five is touched
                        if erase_counter==11:
                            question_5=True
                            question_5_correct=True
                        # Code to erase the two image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_two and x_pos<moving_x_two+50 and y_pos>moving_y_two and y_pos<moving_y_two+50) or (x_pos+20>moving_x_two and x_pos+20<moving_x_two+50 and y_pos+20>moving_y_two and y_pos+20<moving_y_two+50) or (x_pos+20>moving_x_two and x_pos+20<moving_x_two+50 and y_pos>moving_y_two and y_pos<moving_y_two+50) or (x_pos>moving_x_two and x_pos<moving_x_two+50 and y_pos+20>moving_y_two and y_pos+20<moving_y_two+50):
                            blit_two_image=False
                            erase_counter+=1
                            moving_x_two=1000
                            moving_y_two=1000
                            changing_x_two=0
                            changing_y_two=0
                        # Code to erase the three image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_three and x_pos<moving_x_three+50 and y_pos>moving_y_three and y_pos<moving_y_three+50) or (x_pos+20>moving_x_three and x_pos+20<moving_x_three+50 and y_pos+20>moving_y_three and y_pos+20<moving_y_three+50) or (x_pos+20>moving_x_three and x_pos+20<moving_x_three+50 and y_pos>moving_y_three and y_pos<moving_y_three+50) or (x_pos>moving_x_three and x_pos<moving_x_three+50 and y_pos+20>moving_y_three and y_pos+20<moving_y_three+50):
                            blit_three_image=False
                            erase_counter+=1
                            moving_x_three=1000
                            moving_y_three=1000
                            changing_x_three=0
                            changing_y_three=0
                        # Code to erase the five image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_five_2 and x_pos<moving_x_five_2+50 and y_pos>moving_y_five_2 and y_pos<moving_y_five_2+50) or (x_pos+20>moving_x_five_2 and x_pos+20<moving_x_five_2+50 and y_pos+20>moving_y_five_2 and y_pos+20<moving_y_five_2+50) or (x_pos+20>moving_x_five_2 and x_pos+20<moving_x_five_2+50 and y_pos>moving_y_five_2 and y_pos<moving_y_five_2+50) or (x_pos>moving_x_five_2 and x_pos<moving_x_five_2+50 and y_pos+20>moving_y_five_2 and y_pos+20<moving_y_five_2+50):
                            blit_five_2_image=False
                            erase_counter+=1
                            moving_x_five_2=1000
                            moving_y_five_2=1000
                            changing_x_five_2=0
                            changing_y_five_2=0
                        # Code to erase the seven image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_seven_2 and x_pos<moving_x_seven_2+50 and y_pos>moving_y_seven_2 and y_pos<moving_y_seven_2+50) or (x_pos+20>moving_x_seven_2 and x_pos+20<moving_x_seven_2+50 and y_pos+20>moving_y_seven_2 and y_pos+20<moving_y_seven_2+50) or (x_pos+20>moving_x_seven_2 and x_pos+20<moving_x_seven_2+50 and y_pos>moving_y_seven_2 and y_pos<moving_y_seven_2+50) or (x_pos>moving_x_seven_2 and x_pos<moving_x_seven_2+50 and y_pos+20>moving_y_seven_2 and y_pos+20<moving_y_seven_2+50):
                            blit_seven_2_image=False
                            erase_counter+=1
                            moving_x_seven_2=1000
                            moving_y_seven_2=1000
                            changing_x_seven_2=0
                            changing_y_seven_2=0
                        # Code to erase the eleven image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_eleven and x_pos<moving_x_eleven+50 and y_pos>moving_y_eleven and y_pos<moving_y_eleven+50) or (x_pos+20>moving_x_eleven and x_pos+20<moving_x_eleven+50 and y_pos+20>moving_y_eleven and y_pos+20<moving_y_eleven+50) or (x_pos+20>moving_x_eleven and x_pos+20<moving_x_eleven+50 and y_pos>moving_y_eleven and y_pos<moving_y_eleven+50) or (x_pos>moving_x_eleven and x_pos<moving_x_eleven+50 and y_pos+20>moving_y_eleven and y_pos+20<moving_y_eleven+50):
                            blit_eleven_image=False
                            erase_counter+=1
                            moving_x_eleven=1000
                            moving_y_eleven=1000
                            changing_x_eleven=0
                            changing_y_eleven=0
                        # Code to erase the one hundred and one image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_one_hundred_one and x_pos<moving_x_one_hundred_one+50 and y_pos>moving_y_one_hundred_one and y_pos<moving_y_one_hundred_one+50) or (x_pos+20>moving_x_one_hundred_one and x_pos+20<moving_x_one_hundred_one+50 and y_pos+20>moving_y_one_hundred_one and y_pos+20<moving_y_one_hundred_one+50) or (x_pos+20>moving_x_one_hundred_one and x_pos+20<moving_x_one_hundred_one+50 and y_pos>moving_y_one_hundred_one and y_pos<moving_y_one_hundred_one+50) or (x_pos>moving_x_one_hundred_one and x_pos<moving_x_one_hundred_one+50 and y_pos+20>moving_y_one_hundred_one and y_pos+20<moving_y_one_hundred_one+50):
                            blit_one_hundred_one_image=False
                            erase_counter+=1
                            moving_x_one_hundred_one=1000
                            moving_y_one_hundred_one=1000
                            changing_x_one_hundred_one=0
                            changing_y_one_hundred_one=0
                        # Code to erase the fourty three image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_fourty_three and x_pos<moving_x_fourty_three+50 and y_pos>moving_y_fourty_three and y_pos<moving_y_fourty_three+50) or (x_pos+20>moving_x_fourty_three and x_pos+20<moving_x_fourty_three+50 and y_pos+20>moving_y_fourty_three and y_pos+20<moving_y_fourty_three+50) or (x_pos+20>moving_x_fourty_three and x_pos+20<moving_x_fourty_three+50 and y_pos>moving_y_fourty_three and y_pos<moving_y_fourty_three+50) or (x_pos>moving_x_fourty_three and x_pos<moving_x_fourty_three+50 and y_pos+20>moving_y_fourty_three and y_pos+20<moving_y_fourty_three+50):
                            blit_fourty_three_image=False
                            erase_counter+=1
                            moving_x_fourty_three=1000
                            moving_y_fourty_three=1000
                            changing_x_fourty_three=0
                            changing_y_fourty_three=0
                        # Code to erase the sixty one image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_sixty_one and x_pos<moving_x_sixty_one+50 and y_pos>moving_y_sixty_one and y_pos<moving_y_sixty_one+50) or (x_pos+20>moving_x_sixty_one and x_pos+20<moving_x_sixty_one+50 and y_pos+20>moving_y_sixty_one and y_pos+20<moving_y_sixty_one+50) or (x_pos+20>moving_x_sixty_one and x_pos+20<moving_x_sixty_one+50 and y_pos>moving_y_sixty_one and y_pos<moving_y_sixty_one+50) or (x_pos>moving_x_sixty_one and x_pos<moving_x_sixty_one+50 and y_pos+20>moving_y_sixty_one and y_pos+20<moving_y_sixty_one+50):
                            blit_sixty_one_image=False
                            erase_counter+=1
                            moving_x_sixty_one=1000
                            moving_y_sixty_one=1000
                            changing_x_sixty_one=0
                            changing_y_sixty_one=0
                        # Code to erase the nineteen image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_nineteen_2 and x_pos<moving_x_nineteen_2+50 and y_pos>moving_y_nineteen_2 and y_pos<moving_y_nineteen_2+50) or (x_pos+20>moving_x_nineteen_2 and x_pos+20<moving_x_nineteen_2+50 and y_pos+20>moving_y_nineteen_2 and y_pos+20<moving_y_nineteen_2+50) or (x_pos+20>moving_x_nineteen_2 and x_pos+20<moving_x_nineteen_2+50 and y_pos>moving_y_nineteen_2 and y_pos<moving_y_nineteen_2+50) or (x_pos>moving_x_nineteen_2 and x_pos<moving_x_nineteen_2+50 and y_pos+20>moving_y_nineteen_2 and y_pos+20<moving_y_nineteen_2+50):
                            blit_nineteen_2_image=False
                            erase_counter+=1
                            moving_x_nineteen_2=1000
                            moving_y_nineteen_2=1000
                            changing_x_nineteen_2=0
                            changing_y_nineteen_2=0
                        # Code to erase the one hundred and fifty seven image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_one_fifty_seven and x_pos<moving_x_one_fifty_seven+50 and y_pos>moving_y_one_fifty_seven and y_pos<moving_y_one_fifty_seven+50) or (x_pos+20>moving_x_one_fifty_seven and x_pos+20<moving_x_one_fifty_seven+50 and y_pos+20>moving_y_one_fifty_seven and y_pos+20<moving_y_one_fifty_seven+50) or (x_pos+20>moving_x_one_fifty_seven and x_pos+20<moving_x_one_fifty_seven+50 and y_pos>moving_y_one_fifty_seven and y_pos<moving_y_one_fifty_seven+50) or (x_pos>moving_x_one_fifty_seven and x_pos<moving_x_one_fifty_seven+50 and y_pos+20>moving_y_one_fifty_seven and y_pos+20<moving_y_one_fifty_seven+50):
                            blit_one_fifty_seven_image=False
                            erase_counter+=1
                            moving_x_one_fifty_seven=1000
                            moving_y_one_fifty_seven=1000
                            changing_x_one_fifty_seven=0
                            changing_y_one_fifty_seven=0
                        # Code to erase the seventeen image and set its position far away so it will not continue to bounce around invisible and add extra to the erase counter
                        if (x_pos>moving_x_seventeen and x_pos<moving_x_seventeen+50 and y_pos>moving_y_seventeen and y_pos<moving_y_seventeen+50) or (x_pos+20>moving_x_seventeen and x_pos+20<moving_x_seventeen+50 and y_pos+20>moving_y_seventeen and y_pos+20<moving_y_seventeen+50) or (x_pos+20>moving_x_seventeen and x_pos+20<moving_x_seventeen+50 and y_pos>moving_y_seventeen and y_pos<moving_y_seventeen+50) or (x_pos>moving_x_seventeen and x_pos<moving_x_seventeen+50 and y_pos+20>moving_y_seventeen and y_pos+20<moving_y_seventeen+50):
                            blit_seventeen_image=False
                            erase_counter+=1
                            moving_x_seventeen=1000
                            moving_y_seventeen=1000
                            changing_x_seventeen=0
                            changing_y_seventeen=0
                #------------------------------------------------------------------------#
                # Break for user to see his results of the test
                elif question_5==True and question_5_next==False:
                    # Displays text
                    screen.blit(next_text,[500,300])
                    screen.blit(level_3_text_1,[500,350])
                    # Code to proceed when the user presses the next button
                    if (event.type==pygame.MOUSEBUTTONDOWN) and (mouse_x_pos>500 and mouse_y_pos>355 and mouse_x_pos<614 and mouse_y_pos<390):
                        question_5_next=True
                        level+=1
                #------------------------------------------------------------------------#


#------------------------------------------------------------------------#

    # Code for level 3
    # Set the test failed to true is user had got more than 2 wrong
    if wrong_counter>2:
        test_failed=True      
    if level==3:   
        # Set fill_black_2 as first so events will not move back if you go backwards, until you get over the sickness part, the last part where the background changes to light or dark is able to change as you move back and forth       
        # To see first if fill_black_2 is true
        if fill_black_2==True:
            # Fills the screen with black
            screen.fill(BLACK)
            # To see if the user had failed the test
            if test_failed==False:
                # Displays text when user is before a certain distance
                if x_pos<400 and y_pos<300:
                    screen.blit(level_6_text_9,[0,100])
                    screen.blit(level_6_text_12,[0,200])
                    screen.blit(level_6_text_13,[0,300])
            # To see if the user had passed the test
            if test_failed==True:
                # Displays text when user is before a certain distance
                if x_pos<400 and y_pos<300:
                    screen.blit(level_6_text_9,[0,100])
                    screen.blit(level_6_text_10,[0,200])
                    screen.blit(level_6_text_11,[0,300])
            # Set the reverse effect to True
            reverse_effect=False
            # Use the stop command to pause the user movement and force them to press down the keys again so they can't hold down the arrow keys and bypass the effects
            if stop==False:
                x_speed=0
                y_speed=0
                stop=True
            # Change the look of the parents after a certain distance
            if got_test==True and x_pos>360 and y_pos>270:
                parents_change=True
            # To see if the user had failed the test
            if test_failed==True:
                # Display different background as the user gets closer to the parents
                if x_pos>460 and y_pos>370:
                    screen.blit(hell_background_image,[0,0])
                elif x_pos>410 and y_pos>320:
                    screen.blit(light_hell_background_image,[0,0])
                elif x_pos>360 and y_pos>270:
                    screen.blit(very_light_hell_background_image,[0,0])
                # Proceed to the next level when user model reaches parents
                if x_pos>591 and y_pos>408:
                    level+=1
            # To see if the user had passed the test
            if test_failed==False:
                # Display different backgrounds as the user gets closer to the parents
                if x_pos>460 and y_pos>370:
                    screen.blit(heaven_background_image,[0,0])
                elif x_pos>435 and y_pos>330:
                    screen.blit(light_heaven_background_image,[0,0])
                elif x_pos>410 and y_pos>300:
                    screen.blit(very_light_heaven_background_image,[0,0])
                elif x_pos>360 and y_pos>270:
                    screen.blit(very_very_very_light_heaven_background_image,[0,0])
                # Proceed to the next level when user reaches the parents
                if x_pos>591 and y_pos>408:
                    level+=1

        # See of fill_black is true
        elif fill_black==True:
            # Fills the screen black
            screen.fill(BLACK)

        # To see if the fade out sick background image 2 is true
        elif blit_fade_out_sick_background_image_2==True:
            # Displays the fade out sick background 2
            screen.blit(fade_out_sick_background_image_2,[0,0])

        # To see if the fade out sick background image 1 is true
        elif blit_fade_out_sick_background_image_1==True:
            # Displays the fade out sick background 1
            screen.blit(fade_out_sick_background_image_1,[0,0])
            #Displays a text
            screen.blit(level_6_text_8,[50,300])

        # To see if the sick background image is true
        elif blit_sick_background_image==True:
            # Displays the sick background
            screen.blit(sick_background_image,[0,0])
            # Displays a text
            screen.blit(level_6_text_7,[20,200])

        # To see if the fade in sick background image 2 is true
        elif blit_fade_in_background_image_2==True:
            # Displays the fade in background image 2
            screen.blit(fade_in_background_image_2,[0,0])
            # Displays a text
            screen.blit(level_6_text_6,[50,100])

        # To see if the fade out sick background image 1 is true
        elif blit_fade_in_background_image_1==True:
            # Displays the fade in background image 1
            screen.blit(fade_in_background_image_1,[0,0])
            # Displats text on screen
            screen.blit(level_6_text_3,[50,100])
            screen.blit(level_6_text_4,[20,200])
            screen.blit(level_6_text_5,[50,300])

        # To check is the change in appearance of parents is False
        if parents_change==False:
            # Displays regular parents image
            screen.blit(parents_image, [600, 400])
        # Parents change is true, display angel parents if user passed test
        elif test_failed==False:
            screen.blit(angel_parents_image, [600, 400])
        # Parents change is true, display devil parents if user failed test
        elif test_failed==True:
            screen.blit(devil_parents_image, [600, 400])

        # To make sure user gets the test before anything else happens
        if got_test==False:
            # Displays text
            screen.blit(test_image,[10,10])
            screen.blit(level_6_text_1,[150,200])
            screen.blit(level_6_text_2,[200,250])

        # Displayes the user model
        user_model_upgraded(screen,x_pos,y_pos)

        # To reset the user model's position if it wanders off screen
        if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
            x_pos=100
            y_pos=100

        # To make sure the user gets the test before the changing backgrounds are able to take effect
        if x_pos>0 and y_pos>-15 and x_pos<40 and y_pos<40:
            got_test=True

        # To start all the effects once user gets to a certain point
        if got_test==True and x_pos>100 and y_pos>80 and blit_fade_in_background_image_1==False:
            # To set the fill_black as false so it won't interfere with the backgrounds
            fill_black=False
            # Display the first background image
            blit_fade_in_background_image_1=True
            # Slow down the movement speed of the user model
            slow_effect=True
            # Reverse user's controls
            reverse_effect=True
            # Stop the user when he gets to a certain point so the user is not able to hold down the arrow keys and bypass the slow and reverse effects
            if stop==True:
                # Set x speed to 0
                x_speed=0
                # Set y speed to 0
                y_speed=0
                # Set stop to False so user will be able to move again after stopped
                stop=False

        # Sets the visivility of the backgrounds to visible after the user gets to a certain point
        if got_test==True and x_pos>140 and y_pos>110:
            blit_fade_in_background_image_2=True
        if got_test==True and x_pos>180 and y_pos>140:
            blit_sick_background_image=True
        if got_test==True and x_pos>220 and y_pos>170:
            blit_fade_out_sick_background_image_1=True
        if got_test==True and x_pos>280 and y_pos>200:
            blit_fade_out_sick_background_image_2=True
        if got_test==True and x_pos>320 and y_pos>230:
            fill_black_2=True

#------------------------------------------------------------------------#

    # Code for ending screen
    if level==4:
        # Display the background image
        screen.blit(background_image,[0,0])
        # Display texts on screen
        screen.blit(end_text_1,[200,0])
        screen.blit(end_text_2,[270,125])
        screen.blit(end_text_3,[250,250])
        screen.blit(end_text_4,[260,375])

#------------------------------------------------------------------------#

    # Code for the failed level screen if user model leaves game box during level 2
    if level==100:
        # Fills the screen with black
        screen.fill(BLACK)
        # Displays text on screen
        screen.blit(game_over_text_1, [100,200])
        screen.blit(game_over_text_2, [100,300])
        # Displays next level platform
        next_level_platform(screen,400,350)
        # Displays user model
        user_model_upgraded(screen,x_pos,y_pos)
        # Sets all the variables back to original so that level can be restarted
        level_2_game = False
        met_parents = False
        got_pencil = False
        got_eraser=False
        level_2_game_start = False
        question_1 = False
        question_2 = False
        wrong_counter = 0
        question_1_correct = False
        question_1_incorrect = False
        question_2_correct = False
        question_2_incorrect = False
        question_3_correct = False
        question_3_incorrect = False
        question_4_correct = False
        question_4_incorrect = False
        question_5_correct = False
        question_5_incorrect = False
        blit_fade_in_background_image_1=False
        question_2_start=False
        question_3=False
        question_3_start = False
        question_4 = False
        question_4_start=False
        question_5=False
        question_5_start=False
        moving_x_eight = 75
        moving_y_eight = 250
        moving_x_fifty=175
        moving_y_fifty=250
        moving_x_one_thousand=275
        moving_y_one_thousand=250
        moving_x_four=375
        moving_y_four=250
        changing_x_eight =-2
        changing_y_eight =1
        changing_x_fifty=-1
        changing_y_fifty=1
        changing_x_one_thousand=1
        changing_y_one_thousand=1
        changing_x_four=2
        changing_y_four=1
        moving_x_five = 100
        moving_y_five = 100
        moving_x_seven = 200
        moving_y_seven = 100
        moving_x_twelve = 300
        moving_y_twelve = 100
        changing_x_five = 2
        changing_x_seven = 3
        changing_x_twelve = 5
        changing_y_five = 1
        changing_y_seven = 4
        changing_y_twelve = 5
        moving_x_fourteen = 70
        moving_y_fourteen = 100
        moving_x_nineteen= 230
        moving_y_nineteen = 100
        moving_x_sixteen = 380
        moving_y_sixteen = 100
        moving_x_twenty_four = 380
        moving_y_twenty_four = 260
        moving_x_twenty_two = 380
        moving_y_twenty_two = 420
        moving_x_twenty = 230
        moving_y_twenty = 420
        moving_x_thirty_two = 70
        moving_y_thirty_two = 420
        moving_x_twelve_2 = 70
        moving_y_twelve_2 = 260
        changing_x_fourteen = -1
        changing_y_fourteen =-1
        changing_x_nineteen =0
        changing_y_nineteen=-1
        changing_x_sixteen=1
        changing_y_sixteen=-1
        changing_x_twenty_four=1
        changing_y_twenty_four=0
        changing_x_twenty_two=1
        changing_y_twenty_two=1
        changing_x_twenty=0
        changing_y_twenty=1
        changing_x_thirty_two=-1
        changing_y_thirty_two=1
        changing_x_twelve_2=-1
        changing_y_twelve_2 =0
        moving_x_two=60
        moving_y_two=100
        moving_x_three=110
        moving_y_three=100
        moving_x_five_2=60
        moving_y_five_2=150
        moving_x_seven_2=380
        moving_y_seven_2=100
        moving_x_eleven=380
        moving_y_eleven=150
        moving_x_one_hundred_one=330
        moving_y_one_hundred_one=100
        moving_x_fourty_three=60
        moving_y_fourty_three=420
        moving_x_sixty_one=110
        moving_y_sixty_one=420
        moving_x_eighty_five=60
        moving_y_eighty_five=370
        moving_x_nineteen_2=380
        moving_y_nineteen_2=420
        moving_x_one_fifty_seven=380
        moving_y_one_fifty_seven=370
        moving_x_seventeen=330
        moving_y_seventeen=420
        changing_x_two=-1
        changing_y_two=-1
        changing_x_three=-1
        changing_y_three=-2
        changing_x_five_2=-1
        changing_y_five_2=-3
        changing_x_seven_2=1
        changing_y_seven_2=-1
        changing_x_eleven=1
        changing_y_eleven=-2
        changing_x_one_hundred_one=1
        changing_y_one_hundred_one=-3
        changing_x_fourty_three=-1
        changing_y_fourty_three=1
        changing_x_sixty_one=-1
        changing_y_sixty_one=2
        changing_x_eighty_five=-1
        changing_y_eighty_five=3
        changing_x_nineteen_2=1
        changing_y_nineteen_2=1
        changing_x_one_fifty_seven=1
        changing_y_one_fifty_seven=2
        changing_x_seventeen=1
        changing_y_seventeen=3
        moving_x_answer_1=100
        moving_x_answer_2=230
        moving_x_answer_3=350
        moving_x_answer_4=100
        moving_x_answer_5=350
        moving_y_answer_1=200
        moving_y_answer_2=150
        moving_y_answer_3=200
        moving_y_answer_4=320
        moving_y_answer_5=320
        changing_x_answer_1=0
        changing_x_answer_2=0
        changing_x_answer_3=0
        changing_x_answer_4=0
        changing_x_answer_5=0
        changing_y_answer_1=0
        changing_y_answer_2=0
        changing_y_answer_3=0
        changing_y_answer_4=0
        changing_y_answer_5=0
        got_glasses=False
        blit_two_image=True
        blit_three_image=True
        blit_five_2_image=True
        blit_seven_2_image=True
        blit_eleven_image=True
        blit_one_hundred_one_image=True
        blit_fourty_three_image=True
        blit_sixty_one_image=True
        blit_nineteen_2_image=True
        blit_one_fifty_seven_image=True
        blit_seventeen_image=True
        blit_answer_1_image=False
        blit_answer_2_image=False
        blit_answer_3_image=False
        blit_answer_4_image=False
        blit_answer_5_image=False
        blit_incorrect_image_1=False
        blit_incorrect_image_2=False
        blit_incorrect_image_3=False
        blit_incorrect_image_4=False
        blit_incorrect_image_5=False
        erase_counter=0
        question_1_next=False
        question_2_next=False
        question_3_next=False
        question_4_next=False
        question_5_next=False
        # To set the level back to level 2 for a retry
        if x_pos>350 and x_pos<450 and y_pos>350 and y_pos<390:
            level = 2
        # To prevent user model from leaving the screen
        if x_pos>680 or x_pos<-50 or y_pos>460 or y_pos<0:
            x_pos=100
            y_pos=300

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()