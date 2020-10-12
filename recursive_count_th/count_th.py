'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case
    if len(word) < 2:
        return 0
    # Recurse base case:
    elif word[:2] == 'th':
        # 'th' found, increase count and recurse on word
        return count_th(word[1:]) + 1
    else:
        # 'th' not found, continue recursion on word
        return count_th(word[1:])
    
    
