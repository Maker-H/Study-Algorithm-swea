words = ["eat", "tea", "tan", "ate", "nat", "bat"]



idx = 0
sorted_words = []

while idx != len(words):
    sorted_words.append(sorted(list(words[idx])))
    idx += 1

anagram = {}
count = 0

for word in sorted_words:
    if word not in sorted_words:
        anagram[word] = (count)
    elif word in sorted_words:
        anagram[word].update(count)
    count += 1
    


print(type(anagram))

# for key in anagram.keys():
#     anagram.get(key)
    

