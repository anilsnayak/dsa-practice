def has_substring_anagram(s, anagram):
    k = len(anagram)
    
    current_substring = set(s[:k])
    anagram_set = set(anagram)
    
    if current_substring == anagram_set:
        return True
    
    for i in range(len(s) - k):
        current_substring.remove(s[i])
        current_substring.add(s[i+k])
        
        if current_substring == anagram_set:
            return True
        
    return False



s = 'greyhounds'

test_cases = ['uio', 'grey', 'hound', 'dogs', 'xyz']
for anagram in test_cases:
    result = has_substring_anagram(s, anagram)
    print(f"Does '{s}' have a substring that is an anagram of '{anagram}'? {result}")