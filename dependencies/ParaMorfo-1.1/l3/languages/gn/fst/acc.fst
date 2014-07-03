## Delete ! before or after accented vowels.

-> start

start -> start    [.-@V,!]

# acc: at least one accented vowel
start -> acc      [@V]

# del: at least one ! has been deleted
# there must be an accented vowel: @V
start -> del      [:!]
# there must be at least one more segment
del -> delX       [.-@V]
delX -> del       [:!]
delX -> delX      [.-@V]
delX -> acc       [@V]
del -> acc        [@V]
# further ! must be deleted
acc -> accdel     [:!]
# must be at least one more segment after deleted !
accdel -> acc     [.-!]
acc -> acc        [.-!]

# ret: at least one ! has been retained
# there can be no accented vowel: @V
start -> ret      [!]
ret -> ret        [!]
ret -> ret        [.-@V,!]

start ->
acc ->
ret ->