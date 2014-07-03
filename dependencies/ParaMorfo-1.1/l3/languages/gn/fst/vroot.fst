## possible verb roots, up to 5 "syllables"
##   C(u)V(V)
## accented V only possible before final i
## C optional in first syllable
## spanish roots (like alkila) not handled
## no constraints on nasality or vowel sequences other than uVV

-> start

## syllable 1
# initial consonant of "syllable" 1 is optional
start -> C1   [@F;:]
# if three vowels, the first is u
C1 -> V1u     [u;:]
# the one obligatory vowel
V1u -> V1a    [@L]
# possible third vowel
V1a -> V1b    [@L;:]
# ways to end
# one vowel
C1 -> end     [@L]
# u + another vowel
V1u -> end    [@L]
# (u) + two vowels
V1a -> end    [@L]
# accented vowel (only possible as penultimate and before i)
V1u -> V1A    [@V]
V1A -> end    [i]

## syllable 2
# consonant
V1b -> C2     [@R]
# if three vowels, the first is u
C2 -> V2u     [u;:]
# the one obligatory vowel
V2u -> V2a    [@L]
# possible third vowel
V2a -> V2b    [@L;:]
# ways to end
# one vowel
C2 -> end     [@L]
# u + another vowel
V2u -> end    [@L]
# (u) + two vowels
V2a -> end    [@L]
# accented vowel (only possible as penultimate and before i)
V2u -> V2A    [@V]
V2A -> end    [i]

## syllable 3
# consonant
V2b -> C3     [@R]
# if three vowels, the first is u
C3 -> V3u     [u;:]
# the one obligatory vowel
V3u -> V3a    [@L]
# possible third vowel
V3a -> V3b    [@L;:]
# ways to end
# one vowel
C3 -> end     [@L]
# u + another vowel
V3u -> end    [@L]
# (u) + two vowels
V3a -> end    [@L]
# accented vowel (only possible as penultimate and before i)
V3u -> V3A    [@V]
V3A -> end    [i]

## syllable 4
# consonant
V3b -> C4     [@R]
# if three vowels, the first is u
C4 -> V4u     [u;:]
# the one obligatory vowel
V4u -> V4a    [@L]
# possible third vowel
V4a -> V4b    [@L;:]
# ways to end
# one vowel
C4 -> end     [@L]
# u + another vowel
V4u -> end    [@L]
# (u) + two vowels
V4a -> end    [@L]
# accented vowel (only possible as penultimate and before i)
V4u -> V4A    [@V]
V4A -> end    [i]

## syllable 5
# consonant
V4b -> C5     [@R]
# if three vowels, the first is u
C5 -> V5u     [u;:]
# the one obligatory vowel
V5u -> V5a    [@L]
# possible third vowel
V5a -> V5b    [@L;:]
# ways to end
# one vowel
C5 -> end     [@L]
# u + another vowel
V5u -> end    [@L]
# (u) + two vowels
V5a -> end    [@L]
# accented vowel (only possible as penultimate and before i)
V5u -> V5A    [@V]
V5A -> end    [i]

end ->
