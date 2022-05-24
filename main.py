# Check if a word is an anagrams 
# Example:
# find_anagrams("den", "end") --> True



def find_anagrams(word1, word2):
    # [assignment] Add your code here
    list1=[]
    list2=[]
    for x in  word1:
        if x !=' ':
            list1.append(x)
    for x in  word2:
        if x !=' ':
            list2.append(x)
    if len(word1) != len(word2):
        return False
    elif all(item in list1 for item in list2):
        return True
    else:
         return False


print(find_anagrams('endo','deno'))
