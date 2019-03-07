import sys
text = sys.stdin
all_text = [a.strip() for a in text]
print("Words containing 17 letters:", [a for a in all_text if len(a) == 17])
print("Words containing 18+ letters:", [a for a in all_text if len(a) > 17])
print("Shortest word containing all vowels:", sorted([a for a in all_text if "a" in a.lower() and "e" in a.lower() and "i" in a.lower() and "o" in a.lower() and "u" in a.lower()], key=len)[0])
print("Words with 4 a's:", [a for a in all_text if a.lower().count("a") == 4])
print("Words with 2+ q's:", [a for a in all_text if a.lower().count("q") >= 2])
print("Words containing cie:", [a for a in all_text if "cie" in a.lower()])
print("Anagrams of angle:", [a for a in all_text if a.lower() != "angle" and len(a) == 5 and "a" in a.lower() and "n" in a.lower() and "g" in a.lower() and "l" in a.lower() and "e" in a.lower()])
print("Words ending in iary:", len([a for a in all_text if a.lower().endswith("iary")]))
amount_of_es = max([a.lower().count("e") for a in all_text])
print("Words with most e's:", [a for a in all_text if a.lower().count("e") == amount_of_es])
