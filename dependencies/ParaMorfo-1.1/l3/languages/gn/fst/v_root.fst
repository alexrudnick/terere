## possible verb roots, up to 4 syllables
## "syllable": CV(V);  @R@r(@r)
##             CuVV
##   first "syllable" can have no C
## [ignores where real syllable breaks are]
## spanish roots (like alkila) not handled
## no constraints on nasality or vowel sequences other than uVV

-> start

## syllable 1

# first consonant of "syllable" 1 is optional
start -> C1   [@F;:]
C1 -> end     [@L]
# uV(V)
C1 -> C1u     [u]
C1u -> S1     [@r]
C1u -> end    [@L]
C1u -> C1uV   [@r]
C1uV -> S1    [@r]
C1uV -> end   [@L]
# other vowels
C1 -> V1      [@r]  # -u
C1 -> S1      [@r]
V1 -> end     [@L]
V1 -> S1      [@r]

## syllable 2

S1 -> C2      [@R]
C2 -> end     [@L]
# uV(V)
C2 -> C2u     [u]
C2u -> S2     [@r]
C2u -> end    [@L]
C2u -> C2uV   [@r]
C2uV -> S2    [@r]
C2uV -> end   [@L]
# other vowels
C2 -> V2      [@r]  # -u
C2 -> S2      [@r]
V2 -> end     [@L]
V2 -> S2      [@r]

# syllable 3

S2 -> C3      [@R]
C3 -> end     [@L]
# uV(V)
C3 -> C3u     [u]
C3u -> S3     [@r]
C3u -> end    [@L]
C3u -> C3uV   [@r]
C3uV -> S3    [@r]
C3uV -> end   [@L]
# other vowels
C3 -> V3      [@r]  # -u
C3 -> S3      [@r]
V3 -> end     [@L]
V3 -> S3      [@r]

## syllable 4

S3 -> C4      [@R]
C4 -> end     [@L]
# uV(V)
C4 -> C4u     [u]
C4u -> end    [@L]
C4u -> C4uV   [@r]
C4uV -> end   [@L]
# other vowels
C4 -> V4      [@r]  # -u
V4 -> end     [@L]

end ->