### Accent vowel right before first !
### Delete other !s

-> start

start -> start     [.-@v]

start -> vplain    [a;e;i;o;u;y]
vplain -> start    [.-@v,!]
vplain -> vplain   [a;e;i;o;u;y]
vplain -> vother   [ã;ẽ;ĩ;õ;ũ;ỹ;á;é;í;ó;ú;ý]
vplain -> acc      [á:a;é:e;í:i;ó:o;ú:u;ý:y]

start -> vother    [ã;ẽ;ĩ;õ;ũ;ỹ;á;é;í;ó;ú;ý]
vother -> start    [.-@v,!]
vother -> start    [:!]
vother -> vother   [ã;ẽ;ĩ;õ;ũ;ỹ;á;é;í;ó;ú;ý]
vother -> vplain   [a;e;i;o;u;y]
vother -> acc      [á:a;é:e;í:i;ó:o;ú:u;ý:y]

start -> acc       [á:a;é:e;í:i;ó:o;ú:u;ý:y]
acc -> accented    [:!]

# One character has already been accented; just
# delete all other !s
accented -> accented  [.-!]
accented -> accented  [:!]

vplain ->
vother ->
start ->
accented ->
