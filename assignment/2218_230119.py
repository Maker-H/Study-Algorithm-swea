words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

answer = {}

for word in words:
    sorted_word = "".join(sorted(list(word)))
    if sorted_word not in answer:
        answer[sorted_word] = [word]
    elif sorted_word in answer:
        answer[sorted_word].append(word)

print(answer)


#professor
anagrams = {}
for word in words:
    key = ''.join(sorted(word))
    if not anagrams.get(key):
        anagrams[key] = [word]
    else:
        anagrams[key].append(word)

print(anagrams)
print(list(anagrams.values))