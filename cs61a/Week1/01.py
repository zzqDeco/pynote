
# Numeric expressions
2023
2000 + 23
1 + 2 * 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)

# Combinations
'draw'
'draw'[0]
{w[0] for w in words}

# Data
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
