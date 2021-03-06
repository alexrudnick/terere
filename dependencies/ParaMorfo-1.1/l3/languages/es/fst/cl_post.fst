-> se

# se as IO before 3,2p DO
se -> sD  <se:>   [oi=[-1,-2,-p,+xpl],od=[-1,-2,-p,+xpl]];[oi=[-1,+p,+xpl],od=[-1,+p,+xpl]]
se -> sT  <se:>   [+refl,sj=[-1,-2,-p]];[+refl,sj=[-1,+p]]
# no se: either not reflexive or refl:1 or refl:2s,fam
se -> T   [:]      [-refl] ; [+refl,sj=[+1]] ; [+refl,sj=[+2]]

#  se te
sT -> stM <te:>   [od=[-1,+2,-p,+xpl],oi=[-2],sj=[-2]] ; [oi=[-1,+2,-p,+xpl],od=[-2],sj=[-2]]
#  se os
sT -> stM <os:>   [od=[-1,+2,+p,+xpl],oi=[-2],sj=[-2]] ; [oi=[-1,+2,+p,+xpl],od=[-2],sj=[-2]]
# No explicit 2fam dob or iob; no 2fam refl
sT -> sM   [:]     
# te
T -> tM   <te:>   [od=[-1,+2,-p,+xpl],oi=[-2],sj=[-2]] ; [oi=[-1,+2,-p,+xpl],od=[-2],sj=[-2]] ; [+refl,sj=[-1,+2,-p]]
# os
T -> tM   <os:>   [od=[-1,+2,+p,+xpl],oi=[-2],sj=[-2]] ; [oi=[-1,+2,+p,+xpl],od=[-2],sj=[-2]] ; [+refl,sj=[-1,+2,+p]]
# No xplicit 2fam dob or iob; no 2fam refl
T -> M     [:]     [-refl] ; [+refl,sj=[-2]]

# 2 -> 1  <te:>   [od=[-1,+2,-p,+xpl],oi=[-2],sj=[-2]] ; [oi=[-1,+2,-p,+xpl],od=[-2],sj=[-2]] ; [+refl,sj=[-1,+2,-p]]
# No xplicit 2fam dob or iob; no 2fam refl
# 2 -> 1   [:]     [-refl] ; [+refl,sj=[-2]]

stM -> clend <me:>   [od=[+1,-2,-p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,-2,-p,+xpl],od=[-1],sj=[-1]]
stM -> clend <nos:>  [od=[+1,+p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,+p,+xpl],od=[-1],sj=[-1]]
stM -> stL   [:]
sM -> smL    <me:>   [od=[+1,-2,-p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,-2,-p,+xpl],od=[-1],sj=[-1]]
sM -> smL    <nos:>  [od=[+1,+p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,+p,+xpl],od=[-1],sj=[-1]]
sM -> sL     [:]
# te/os me/nos
tM -> clend  <me:>   [od=[+1,-2,-p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,-2,-p,+xpl],od=[-1],sj=[-1]] ; [+refl,sj=[+1,-2,-p]]
tM -> clend  <nos:>  [od=[+1,+p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,+p,+xpl],od=[-1],sj=[-1]] ; [+refl,sj=[+1,+p]]
tM -> tL     [:]      [-refl] ; [+refl,sj=[-1]]
M -> mL      <me:>   [od=[+1,-2,-p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,-2,-p,+xpl],od=[-1],sj=[-1]] ; [+refl,sj=[+1,-2,-p]]
M -> mL      <nos:>  [od=[+1,+p,+xpl],oi=[-1],sj=[-1]] ; [oi=[+1,+p,+xpl],od=[-1],sj=[-1]] ; [+refl,sj=[+1,+p]]
M -> L       [:]      [-refl] ; [+refl,sj=[-1]]

# se te/os l_
stL -> clend <lo:>   [od=[-1,-2,-p,-fem,+xpl]]
stL -> clend <la:>   [od=[-1,-2,-p,+fem,+xpl]]
stL -> clend <los:>  [od=[-1,+p,-fem,+xpl]]
stL -> clend <las:>  [od=[-1,+p,+fem,+xpl]]
stL -> clend <le:>   [oi=[-1,-2,-p,+xpl]] ; [od=[-1,-2,-p,+anim,+xpl]]
stL -> clend <les:>  [oi=[-1,+p,+xpl]] ; [od=[-1,+p,+anim,+xpl]]
# se te
stL -> clend  [:]     

# se me/nos l_
smL -> clend <lo:>   [od=[-1,-2,-p,-fem,+xpl]]
smL -> clend <la:>   [od=[-1,-2,-p,+fem,+xpl]]
smL -> clend <los:>  [od=[-1,+p,-fem,+xpl]]
smL -> clend <las:>  [od=[-1,+p,+fem,+xpl]]
smL -> clend <le:>   [oi=[-1,-2,-p,+xpl]] ; [od=[-1,-2,-p,+anim,+xpl]]
smL -> clend <les:>  [oi=[-1,+p,+xpl]] ; [od=[-1,+p,+anim,+xpl]]
# se me/nos
smL -> clend  [:]     

# se l_ (se: iob)
sD ->  clend <lo:>   [od=[-1,-2,-p,-fem,+xpl]]
sD ->  clend <la:>   [od=[-1,-2,-p,+fem,+xpl]]
sD ->  clend <los:>  [od=[-1,+p,-fem,+xpl]]
sD ->  clend <las:>  [od=[-1,+p,+fem,+xpl]]
sD ->  clend <le:>   [od=[-1,-2,-p,+anim,+xpl]]
sD ->  clend <les:>  [od=[-1,+p,+anim,+xpl]]

# se l_ (reflexive)
sL -> clend <lo:>    [od=[-1,-2,-p,-fem,+xpl]]
sL -> clend <la:>    [od=[-1,-2,-p,+fem,+xpl]]
sL -> clend <los:>   [od=[-1,+p,-fem,+xpl]]
sL -> clend <las:>   [od=[-1,+p,+fem,+xpl]]
sL -> clend <le:>    [oi=[-1,-2,-p,+xpl]] ; [od=[-1,-2,-p,+anim,+xpl]]
sL -> clend <les:>   [oi=[-1,+p,+xpl]] ; [od=[-1,+p,+anim,+xpl]]
# JUST se
sL -> clend  [:]      [od=[-xpl],oi=[-xpl]]

# te/os + l_
tL -> clend <lo:>    [od=[-1,-2,-p,-fem,+xpl]]
tL -> clend <la:>    [od=[-1,-2,-p,+fem,+xpl]]
tL -> clend <los:>   [od=[-1,+p,-fem,+xpl]]
tL -> clend <las:>   [od=[-1,+p,+fem,+xpl]]
tL -> clend <le:>    [oi=[-1,-2,-p,+xpl]] ; [od=[-1,-2,-p,+anim,+xpl]]
tL -> clend <les:>   [oi=[-1,+p,+xpl]] ; [od=[-1,+p,+anim,+xpl]]
# JUST te/os
tL -> clend  [:]      [od=[-xpl],oi=[+xpl],-refl] ; [oi=[-xpl],od=[+xpl],-refl] ; [+refl,oi=[-xpl],od=[-xpl]]

# me/nos + l_
mL -> clend <lo:>    [od=[-1,-2,-p,-fem,+xpl]]
mL -> clend <la:>    [od=[-1,-2,-p,+fem,+xpl]]
mL -> clend <los:>   [od=[-1,+p,-fem,+xpl]]
mL -> clend <las:>   [od=[-1,+p,+fem,+xpl]]
mL -> clend <le:>    [oi=[-1,-2,-p,+xpl]] ; [od=[-1,-2,-p,+anim,+xpl]]
mL -> clend <les:>   [oi=[-1,+p,+xpl]] ; [od=[-1,+p,+anim,+xpl]]
# JUST me/nos
mL -> clend  [:]      [od=[-xpl],oi=[+xpl],-refl] ; [oi=[-xpl],od=[+xpl],-refl] ; [+refl,oi=[-xpl],od=[-xpl]]

# JUST l_
L -> clend <lo:>     [od=[-1,-2,-p,-fem,+xpl],oi=[-xpl]]
L -> clend <la:>     [od=[-1,-2,-p,+fem,+xpl],oi=[-xpl]]
L -> clend <los:>    [od=[-1,+p,-fem,+xpl],oi=[-xpl]]
L -> clend <las:>    [od=[-1,+p,+fem,+xpl],oi=[-xpl]]
L -> clend <le:>     [oi=[-1,-2,-p,+xpl],od=[-xpl]] ; [od=[-1,-2,-p,+anim,+xpl],oi=[-xpl]]
L -> clend <les:>    [oi=[-1,+p,+xpl],od=[-xpl]] ; [od=[-1,+p,+anim,+xpl],oi=[-xpl]]
# NO CLITIC PRONOUNS
L -> clend  [:]       [od=[-xpl],oi=[-xpl],-refl]

clend ->
