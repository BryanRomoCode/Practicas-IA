import random 
import string


characters = [] #a list with all characters

for ch in string.printable:   # String of ASCII characters which are considered printable.
                              #This is a combination of digits, ascii_letters, punctuation, and whitespace.
    characters.append(ch)
    

def rs(string): #generate random solution

    rand_solution = []

    c = 0 #count
    while c < len(string):

        rand_solution.append(random.choice(characters)) #choses a random character and puts it in the list.
                                                        #at the end, a new, random solution has been generated
        c +=1
        
    return rand_solution
        

def score(solution): #evaluates the solution

    score = len(solution) #initial value equals the length of the string
                          #every character gives or takes 1 point

    for i in range(len(solution)): #iterates through all character

        if solution[i] == target[i]:

            score -= 1  #substract a point, since we want to go to 0
    return score

 

def mutate(solution): #mutates a solution 'slightly', i.e. only 1 character

    mutated = [] #mutated solution

    i = random.randint(0,len(solution)-1) #a random number for index

    solution[i] = random.choice(characters) #mutate the char at that index with a random character

    mutated = solution

    return mutated




def main():
    
    best = rs(target) #a random solution as best
    best_score = score(best) #and its score

    evaluated_solutions = 0     
    accepted_solutions = 0
    
    while best_score > 0: #score is zero when target string has been created
        
        if(evaluated_solutions-500) % 500 == 0: #Display best so far based every 500 evaluations
            
            print('Evaluations: ',evaluated_solutions,' | Best score: ', best_score, ' | Solution: ', "".join(best)) 
     
          
        best_solution = best[:] #update/copy best_solution
        
        mutate(best_solution) #mutate it
        
        lowest_score = score(best_solution) #find its score

        if lowest_score < best_score: #if the mutattion had a better score (lower in our case), accept it
            
            best_score = lowest_score  #this becomes the best_score
            
            best = best_solution  #and this becomes the best solution
            
            accepted_solutions += 1  #increase number of accepted solution
            
        evaluated_solutions += 1 #increase number of evaluated soluitons
 

    print("\n \n", 'Evaluations: ',evaluated_solutions,' | Best score: ', best_score, ' | Solution: ', "".join(best)) 
    print('Number of Solutions Evaluated ', evaluated_solutions)
    print('Number of Solutions Accepted ', accepted_solutions)
    



y = 1
while y:

    t = input('\n Target String ') #user input

    target = [] #list with char of target strig

    for i in range(len(t)):
    
        target.append(t[i]) #puts every letter in the list
    main()
    y = int(input('\n continue? 1/0 '))