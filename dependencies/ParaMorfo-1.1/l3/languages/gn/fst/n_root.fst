## possible verb roots, up to 5 "syllables"
##   C(u)V(V)
## accented V only possible before final "syllable"
## C optional in first syllable
## spanish roots (like alkila) not handled
## no constraints on nasality or vowel sequences other than uVV

-> start

## final syllable (following accented vowel)
# possibly no consonant
Sf -> Cf      [@R;:]
# at most one vowel in this final syllable
Cf -> end     [@l]

## syllable 1
# initial consonant, could be uppercase
start -> C1   [@F]
# the one obligatory vowel, could be uppercase
start -> V1a  [@L]
# initial accented vowel, could be uppercase
start -> Sf   [@V]
C1 -> V1a     [@l]
C1 -> V1u     [u]
V1u -> V1a    [@l]
# possible third vowel
V1a -> V1b    [@l;:]
# ways to end
# one vowel
C1 -> end     [@l]
# u + another vowel
V1u -> end    [@l]
# (u) + two vowels
V1a -> end    [@l;:]
# accented vowel (only possible before final syllable (Sf)
C1 -> Sf      [@a]

## syllable 2
V1b -> C2     [@R]
# if three vowels, the first is u
C2 -> V2u     [u;:]
# the one obligatory vowel
V2u -> V2a    [@l]
# possible third vowel
V2a -> V2b    [@l;:]
# ways to end
# one vowel
C2 -> end     [@l]
# u + another vowel
V2u -> end    [@l]
# (u) + two vowels
V2a -> end    [@l]
# accented vowel (only possible before final syllable (Sf)
V2u -> Sf     [@a]

## syllable 3
V2b -> C3     [@R]
# if three vowels, the first is u
C3 -> V3u     [u;:]
# the one obligatory vowel
V3u -> V3a    [@l]
# possible third vowel
V3a -> V3b    [@l;:]
# ways to end
# one vowel
C3 -> end     [@l]
# u + another vowel
V3u -> end    [@l]
# (u) + two vowels
V3a -> end    [@l]
# accented vowel (only possible before final syllable (Sf)
V3u -> Sf     [@a]

## syllable 4
V3b -> C4     [@R]
# if three vowels, the first is u
C4 -> V4u     [u;:]
# the one obligatory vowel
V4u -> V4a    [@l]
# possible third vowel
V4a -> V4b    [@l;:]
# ways to end
# one vowel
C4 -> end     [@l]
# u + another vowel
V4u -> end    [@l]
# (u) + two vowels
V4a -> end    [@l]
# accented vowel (only possible before final syllable (Sf)
V4u -> Sf     [@a]

end ->