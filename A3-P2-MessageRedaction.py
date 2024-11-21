#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:   W0499622
#Student Name:  Jack Leonard

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # notes: im assuming that im only redacting letters regardless of casing

    notQuit = True #this boolean is for exiting the loop
    

    while notQuit: # if user types quit then user program ends
        redactLettersList = [] # im making the letters to redact as a list so i can use .contains later
        finalSentence = "" #this will be used to keep original casing in the final print

        originalSentence = input("Type a phrase (or quit to exit program): ")   #inputs
        lowerSentence = originalSentence.lower() #using lower to making comparing characters easier
        if lowerSentence == "quit":
            notQuit = False # forces the program to end
            continue

        lettersToRedact = input("Type a comma seperated list of letters to redact: ").lower() #^^^^
    
        for i in range(len(lettersToRedact)): # fills up the list of characters to be redacted
            if lettersToRedact[i] != ",":
                redactLettersList.append(lettersToRedact[i]) #adds the character to the list
            
        for i in range(len(redactLettersList)): #creates redacted list only it doesnt include original casing
            lowerSentence = lowerSentence.replace(redactLettersList[i], "_") # replaces specified characters with _
        
        for i in range(len(originalSentence)): # this loop is used to create the redacted sentence with original casing
            if lowerSentence[i] == "_": #if the character in the lower sentence was redacted it replaces it here with _
                finalSentence += "_" # then the underscore is appended onto our final string
            else:
                finalSentence += originalSentence[i] #if character wasnt redacted adds the character

        numberRedacted = finalSentence.count("_") # returns the number of characters we redacted
        
        print("The number of letters redacted is {0}".format(numberRedacted)) #prints number of redacted characters
        print("Redacted sentence {0}".format(finalSentence)) #prints redacted sentence
    # YOUR CODE ENDS HERE

main()