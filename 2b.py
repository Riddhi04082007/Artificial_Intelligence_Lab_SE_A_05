from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Graphics'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(Likes='maths'), StudentFacts(likes='machine learning'))
    def robotics(self):
        print("Suggessted carrer path: Robotics Engineering")
    @Rule(StudentFacts(likes='electrical'), StudentFacts(likes='Maths'))
    def mechatronics(self):
        print("Suggested Career Path: Mechatronics Engineering")  
    @Rule(StudentFacts(likes='AI'), StudentFacts(likes='DS'))
    def AIDS(self):
        print("Suggested Career Path: AI & DS Engineering")      
        
        
        

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("enter the subjects of your choice ")
    interests = input("Enter your interests separated by commas  among the following subjects : Graphics , Chemistry , Biology , Maths, Physics, Circuits , ): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
                                   
