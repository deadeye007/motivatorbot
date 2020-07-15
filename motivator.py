# Motivate Me - Scratch that Motivational Quote Itch
import random, sys
from os import system, name
from time import sleep

def logo():
    print('''
#####################################################################
#
# Motivator Bot
# It's a Bot Time to Get Motivated! [VERSION 1.0]
# CODED BY: ANDREW STURM
# CREATED ON: 2020-04-20
#
#####################################################################

''')

def clear(): 
  
    # Clear command for Windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # Clear command for Mac/*nix 
    else: 
        _ = system('clear') 

def main():
    messages = ('With the new day comes new strength and new thoughts.',
                'Quality is not an act. It is a habit.',
                'Well done is better than well said.',
                'Good, better, best. Never let it rest. \'Til your good is better and your better is best.',
                'Knowing is not enough; we must apply. Willing is not enough; we must do.',
                'The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence.',
                'Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.',
                'It does not matter how slowly you go as long as you do not stop.',
                'The secret of getting ahead is getting started.',
                'Things work out best for those who make the best of how things work out.',
                'To live a creative life, we must lose our fear of being wrong.',
                'If you are not willing to risk the usual, you will have to settle for the ordinary.',
                'Trust because you are willing to accept the risk, not because it is safe or certain.',
                'Take up one idea. Make that one idea your life - think of it, dream of it, live on that idea. Let the brain, muscles, nerves, every part of your body, be full of that idea, and just leave every other idea alone. This is the way to success.',
                'Good things come to people who wait, but better things come to those who go out and get them.',
                'If you do what you always did, you will get what you always go.',
                'Success is walking from failing to failure with no loss of enthusiasm.',
                'Just when the caterpillar thought the world was ending, he turned into a butterfly.',
                'Whenever you see a successful person, you only see the public glories, never the private sacrifices to reach them.',
                'Opportunities don\'t happen, you create them.',
                'Try not to become a person of success, but rather try to become a person of value.',
                'Great minds discuss ideas; average minds discuss events; small minds discuss people.',
                'If you don\'t value your time, neither will others. Stop giving away your time and talents - start charging for it.',
                'No one can make you feel inferior without your consent.',
                'If you\'re going through hell, keep going.',
                'The ones who are crazy enough to think they can change the world, are the ones who do.',
                'What seems to us as bitter trials are often blessings in disguise.',
                'The meaning of life is to find your gift. The purpose of life is to give it away.',
                'The distance between insanity and genius is measured only by success.',
                'When you stop chasing the wrong things, you give the right things a chance to catch you.',
                'No masterpiece was ever created by a lazy artist.',
                'Happiness is a butterfly, which when pursued, is always beyond your grasp, but which, if you will sit down quietly, may alight upon you.',
                'Blessed are those who can give without remembering and take without forgetting.',
                'Do one thing every day that scares you.',
                'What\'s the point in being alive if you don\'t at least try to do something remarkable?',
                'Life is not about finding yourself. Life is about creating yourself.',
                'Knowledge is being aware of what you can do. Wisdom is knowing when not to do it.',
                'Your problem isn\'t the problem. Your reaction is the problem.',
                'There are two types of people who will tell you that you cannot make a difference in this world: those who are afraid to try and those who are afraid you will succeed.',
                'Thinking should become your capital asset, no matter whatever ups and downs you come across in your life.',
                'I find that the harder I work, the more luck I seem to have.',
                'The starting point of all achievement is desire.',
                'Success is the sum of small efforts, repeated day-in and day-out.',
                'If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work.',
                'All progress takes place outside the comfort zone.',
                'Only put off until tomorrow what you are willing to die having left unone.',
                'People often say that motivation doesn\'t last. Well, neither does bathing--that\'s why we recommend it daily.',
                'We become what we think about most of the time, and that\'s the strangest secret.',
                'The only place where success comes before work is in the dictionary.',
                'Too many of us are not living our dreams because we are living our fears.',
                'It\'s not what you look at that matters, it\'s what you see.',
                'The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself.',
                'People who succeed have momentum. The more they succeed, the more they want to succeed, and the more they find a way to succeed. Similarly, when someone is failing, the tendency is to get on a downward spiral that can even become a self-fulfilling prophecy.',
                'When I dare to be powerful, to use my strength in the service of my vision, then it becomes less and less important whether I am afraid.',
                'There is no traffic jam along the extra mile.',
                'Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.',
                'If you genuinely want something, don\'t wait for it--teach yourself to be impatient.',
                'Don\'t let the fear of losing be greater than the excitement of winning.',
                'If you want to make a permanent change, stop focusing on the size of your problems and start focusing on the size of you!',
                'You can\'t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something--your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.',
                'Success does not consist in never making mistakes, but in never making the same one a second time.',
                'I don\'t want to get to the end of my life and find that I lived just the length of it. I want to have lived the width of it as well.',
                'Motivation is what gets you started. Habit is what keeps you going.',
                'People rarely succeed unless they have fun in what they are doing.',
                'There is no chance, no destiny, no fate, that can hinder or control the firm resolve of a determined soul.',
                'Our greatest fear should not be of failure but of succeeding at things in life that don\'t really matter.',
                'A goal is not always meant to be reached; it often serves simply as something to aim at.',
                'Be miserable. Or motivate yourself. Whatever has to be done, it\'s always your choice.',
                'You measure the size of the accomplishment by the obstacles you had to overcome to reach your goals.',
                'Real difficulties can be overcome; it is only the imaginary ones that are unconquerable.',
                'Don\'t let what you cannot do interfere with what you can do.',
                'Don\'t let yesterday take up too much of today.',)
    try:
        clear()
        logo()
        print('Here\'s your random motivational quote, out of ' + str(len(messages)) + ' quotes, currently.\n\n')
        print(messages[random.randint(0,len(messages) - 1)])
    except KeyboardInterrupt:
        print("Keyboard interrupt signal detected.\nExiting...")
        sys.exit()
# Start the script
main()
