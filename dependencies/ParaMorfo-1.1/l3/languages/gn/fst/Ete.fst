## initial vowel of intensifier suffix
## E -> i before a,u
## E -> e before i,o,y
## E -> 0 before e
## (some disagreement about what is right in the grammars)

-> start

# consonants
start -> start   [@c]

# vowels
start -> u       [@u]
start -> e       [e;é;ẽ]
start -> o       [@o]

# vowels + E
u -> end         [i:E]
e -> end         [:E]
o -> end         [e:E]

# vowels + other segments
u -> u           [@u]
u -> e           [e;é;ẽ]
u -> o           [@o]
e -> u           [@u]
e -> e           [e;é;ẽ]
e -> o           [@o]
o -> u           [@u]
o -> e           [e;é;ẽ]
o -> o           [@o]

u -> start       [@c]
e -> start       [@c]
o -> start       [@c]

# anything goes after E
end -> end       [.]

end ->
start ->
u ->
e ->
o ->