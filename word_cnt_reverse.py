# Enter your code here. Read input from STDIN. Print output to STDOUT
def test(s):
    #write your code here
    words = s.split()
    
    print("Number of words: ",len(words))

    for i in range(1, len(words), 2):
        word = words[i]
        if len(word) >= 2:
            words[i] = word[-1] + word[1:-1][::-1] + word[0]
        
    result = ' '.join(words)
    
    print("Modified Sentence: ",result)
       
    
    return

if __name__=='__main__':
    
    s=input()
    (test(s))
