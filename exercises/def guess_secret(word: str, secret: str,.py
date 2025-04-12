def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths>")
        return False
#(If we reach this line i.e. do not execute the if statement, then we know the length of word and the length of the secret are equal)
    if word[idx] != secret[idx]:
        print(f"{word[idx]} isn't the secret word's letter.")
        return False
    else:
        print(f"{word[idx]} is at index {idx} for both words! Checking next letters...")
        return guess_secret(word=word, secret=secret,idx=idx+1)
    #to avoid infinite loop we assign the current value of idx to the parameter idx and plus one
#if we have same character at same index we must move to a completely different block 
print("They are the same word!")
return True

    

