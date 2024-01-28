# Your name: Rayan Mostofa
# Your student id: 4970 7916
# Your email: mostofar@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Just me 
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import random

# create a magic 8 ball class
class MagicEightBall():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
                self.answers_list = answers
                self.questions_history_list = []
                self.answers_history_list = []                        

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string with all of the questions in the questions_history_list separated by commas
    #        iIf no questions have been asked, return an empty string
    def __str__(self):
        if len(self.questions_history_list) == 0:
            return ""
        else:
            return ", ".join(self.questions_history_list)

    # Creates the get_fortune method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the magic 8 ball
    # RETURNS: a string with the answer
    def get_fortune(self, question):
        if question in self.questions_history_list:
            return "I've already answered this question"
        
        if question not in self.questions_history_list:
            r = random.randrange(0, len(self.answers_list))
            self.answers_history_list.append(r)
            return self.answers_list[r]


    # Creates play_game method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def play_game(self):
        q = input("Please enter a question: ")
        while True:            
            if q == "I'm done playing":
                print("Goodbye")
                break            
            fortune = self.get_fortune(q)
            print(fortune)
            self.questions_history_list.append(q)            
                
            q = input("Please enter the next question: ")                            


    # Create the print_answer_frequencies method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: dictionary that maps answers to frequencies
    #          if no answers have been given, return an empty dictionary
    def print_answer_frequencies(self):
        
        dictionary = {}                
        
        for item in self.answers_history_list:
            if self.answers_list[item] in dictionary:
                dictionary[self.answers_list[item]] += 1
            else:
                dictionary[self.answers_list[item]] = 1
        
        if (len(dictionary) == 0):
            return dictionary
        
        for key, value in dictionary.items():
            print(f"The answer '{key}' has been given {value} times")
        
        return dictionary
        

def test():
    answers_list = ['yes', 'no', 'maybe']
    eight_ball = MagicEightBall(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {eight_ball.answers_history_list}")
    print(f"Question History List: Expected: {[]}, Actual: {eight_ball.questions_history_list}")
    print(" ")

    print("Test __str__:")
    eight_ball.questions_history_list = ['will it snow today?', 'should I make soup?']
    expected = "will it snow today?, should I make soup?"
    print(f"Expected: {expected}, Actual: {str(eight_ball)}")
    print(" ")


    print("Testing return value of get_fortune:")
    res = eight_ball.get_fortune('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing get_fortune:")
    eight_ball.answers_list = ['yes']
    res = eight_ball.get_fortune('test question 2')
    print(f"Expected: {'yes'}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune adds answer index to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = []
    eight_ball.get_fortune('test question 2')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune does not add 'I've already answered this question' to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = [0]
    eight_ball.questions_history_list = ['test question 3']
    eight_ball.get_fortune('test question 3')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value print_answer_frequencies")
    eight_ball.answers_list = ['yes', 'no', 'maybe']
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(eight_ball.print_answer_frequencies())
    print(f"Expected: {dict}, Actual: {res}")
    print(" ")

    print("Testing return value print_answer_frequencies keys")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(list(eight_ball.print_answer_frequencies().keys())[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing print_answer_frequencies")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = eight_ball.print_answer_frequencies()
    expected = {'yes': 3, 'no': 2, 'maybe': 1}
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

def main():
#     # defines the possible answers
#     answers = ["definitely", "Most likely", "It is certain", "Maybe", "Cannot predict now", "Very doubtful", "Don't count on it", "Absolutely not"]
    
#     # creates a MagicEightBall object
#     ball = MagicEightBall(answers)

#     # initiates the game play using the play_game method
#     ball.play_game()
    
#     # shows the output of print_answer_frequencies
#     ball.print_answer_frequencies()
    test()



# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    # test() #TODO: Uncomment if you do the extra credit