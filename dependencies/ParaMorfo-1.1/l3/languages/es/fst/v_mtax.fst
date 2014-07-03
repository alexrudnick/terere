###
### Morfotaxis de verbos españoles
###
### +- AL = América Latina (sin o con vosotros)

-> start

# irregular participles
start -> pps    +irr_part+

start -> prepron  [:]     [pos=v]
### old version with pre-clitics
## start -> prepron >cl_pre<
## if no pre-clitics, either tenseless or continuous participle (possible post-clitics)
## or not clitics at all
##        [tam=[-tmp]] ; [tam=[+ger]] 
###

# prefixes which begin some irregular verbs
prepron           +prefix+
prepron -> stem   [:]

stem -> stem_e  +verbs_e+
stem -> stem_a  +verbs_a+
stem -> stem_i  +verbs_i+
# these specify different destination states
stem              +vb_irr+
stem -> caer      [:]
caer              +caer+
stem -> decir     [:]
decir             +decir+
stem -> ducir     [:]
ducir             +ducir+
stem -> poner     [:]
poner             +poner+
stem -> tener     [:]
tener             +tener+
stem -> traer     [:]
traer             +traer+
stem -> venir     [:]
venir             +venir+
stem -> ver       [:]
ver               +ver+

# Presente 2,3,1p; imperativo familiar; infinitivo; imperfecto (no futuro, pretérito, subjuntivo, presente 1s)
stem_a -> stem_a1      [:]     [tam=[-prt,-fut]]
stem_e -> stem_e1      [:]     [tam=[-prt,-fut]]
stem_i -> stem_i1      [:]     [tam=[-prt,-fut]]

# Subjuntivo presente, presente 1s ##, imperativo formal
stem_a -> a_sub_prs1   [:]     [tam=[-prt,-fut,-ipf,-ger,-part,-inf]]
stem_e -> e_sub_prs1   [:]     [tam=[-prt,-fut,-ipf,-ger,-part,-inf]]
stem_i -> e_sub_prs1   [:]     [tam=[-prt,-fut,-ipf,-ger,-part,-inf]]

# Imperativo
stem_a1 -> postpron <`a:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
stem_e1 -> postpron <`e:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
stem_i1 -> postpron <`e:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
# vos
stem_a1 -> postpron  <'a:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
stem_e1 -> postpron  <'e:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
stem_i1 -> postpron  <'i:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,-p]]
# vosotros
stem_a1 -> postpron  <'ad:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,+p]]
stem_e1 -> postpron  <'ed:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,+p]]
stem_i1 -> postpron  <'id:>    [tam=[-tmp,+imv,-ger,-part,-inf],sj=[-1,+2,+p]]

# Presente
# 1s
a_sub_prs1 -> person    [o:]    [tam=[-sub,-cnd,-imv,+tmp],sj=[+1,-2,-p]]
e_sub_prs1 -> person    [o:]    [tam=[-sub,-cnd,-imv,+tmp],sj=[+1,-2,-p]]
# 2s vos, presente
stem_a1 -> end    <ás:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,-p]]
stem_e1 -> end    <és:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,-p]]
stem_i1 -> end    <ís:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,-p]]
# 2p vosotros, presente
stem_a1 -> end    <áis:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,+p]]
stem_e1 -> end    <éis:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,+p]]
stem_i1 -> end    <ís:>     [tam=[-sub,-ipf,-cnd,-imv,+tmp],sj=[-1,+2,+p]]
# otras
stem_a1 -> prs    [a:]     [tam=[-sub,-ipf,-cnd,-imv,+tmp]]
stem_e1 -> prs    [e:]     [tam=[-sub,-ipf,-cnd,-imv,+tmp]]
# becomes e when not stressed
stem_i1 -> prs    [I:]     [tam=[-sub,-ipf,-cnd,-imv,+tmp]]
prs -> person    [:]      [sj=[+p]] ; [sj=[-1]]

# Futuro
stem_a -> fut    <ar':>   [tam=[+fut,-imv,-prt,-sub,+tmp]]
stem_e -> fut    <er':>   [tam=[+fut,-imv,-prt,-sub,+tmp]]
stem_i -> fut    <ir':>   [tam=[+fut,-imv,-prt,-sub,+tmp]]
# yo, nosotros, vosotros
fut -> person    [e:]     [sj=[+1],tam=[-cnd,+tmp]];[sj=[+2,+p],tam=[-cnd,+tmp]]
fut -> person    [a:]     [sj=[-1],tam=[-cnd,+tmp]]

# Condicional
fut -> person    <ía:>    [tam=[+cnd]]

# Subjuntivo presente, imperativo (sing formal, plur (1st, 2nd (gram 3rd) person))
a_sub_prs1 -> person <`e:>   [tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[-1]];[tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+1,-p]]
# nosotros, vosotros
a_sub_prs1 -> person <'e:>   [tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+1,+p]];[tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+2,+p],-AL]
e_sub_prs1 -> person <`a:>   [tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[-2]];[tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+1,-p]]
# nosotros, vosotros
e_sub_prs1 -> person <'a:>   [tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+1,+p]];[tam=[+sub,+tmp,-ger,-part,-inf,-imv],sj=[+2,+p],-AL]

# Imperfecto
stem_a1 -> person <'aba:>  [tam=[+ipf,-imv,-sub,+tmp]]
stem_e1 -> person <ía:>    [tam=[+ipf,-imv,-sub,+tmp]]
stem_i1 -> person <ía:>    [tam=[+ipf,-imv,-sub,+tmp]]

# Pretérito

# Orthographic changes may precede 1s é
# yo
stem_a -> end    [é:]     [tam=[+prt,-imv,-fut,+tmp],sj=[+1,-p]]
# 3s
stem_a -> end    [ó:]     [tam=[+prt,-imv,-fut,+tmp],sj=[-1,-2,-p]]
# vos, plur
stem_a -> prt2   [a:]     [tam=[+prt,-sub,-imv,-fut,+tmp],sj=[+2,-p]] ; [tam=[+prt,-sub,+tmp],sj=[+p]]
# subj
stem_a -> prt2   <'a:>    [tam=[+prt,+sub,-imv,-fut,+tmp]]

stem_e -> ie_prt [:]      [tam=[+prt,+tmp]]
stem_i -> ie_prt [:]      [tam=[+prt,+tmp]]

ie_prt -> end     [í:]    [sj=[+1,-p],tam=[-sub]]
ie_prt -> end     <ió:>   [sj=[-1,-2,-p],tam=[-sub]]
# vos, vosotros, nosotros
ie_prt -> prt2    [i:]    [sj=[+2],tam=[-sub]] ; [sj=[+1,+p],tam=[-sub]]
ie_prt -> prt2    <i'e:>  [sj=[-1,+p]] ; [tam=[+sub]]

irr_prt -> end    [e:]    [sj=[+1,-p],tam=[-sub,+tmp]]
irr_prt -> end    [o:]    [sj=[-1,-2,-p],tam=[-sub,+tmp]]
# vos, vosotros, nosotros
irr_prt -> prt2   [i:]    [sj=[+2],tam=[-sub,+tmp]] ; [sj=[+1,+p],tam=[-sub,+tmp]]
# 3p
irr_prt -> prt2   <i'e:>  [sj=[-1,+p],tam=[-sub,+tmp]] ; [tam=[+sub,+tmp]]

# Special person endings for preterite
prt2 -> end      <ste:>   [tam=[-sub],sj=[-1,+2,-p]]
# vosotros
prt2 -> end      <steis:> [tam=[-sub],sj=[-1,+2,+p]]
prt2 -> end      <mos:>   [tam=[-sub],sj=[+1,+p]]
prt2 -> end      <ron:>   [tam=[-sub],sj=[-1,+p]]

# Subjuntivo imperfecto
prt2 -> person    <ra:>    [tam=[+sub,-imv]]
prt2 -> person    <se:>    [tam=[+sub,-imv]]

# Infinitivo
stem_a1 -> inf    <'ar:>
stem_e1 -> inf    <'er:>
stem_i1 -> inf    <'ir:>
inf -> postpron  [:]      [tam=[-imv,-ipf,-sub,-tmp,-ger,-part,+inf]]

# Gerundio
stem_a1 -> ppr  <'ando:> 
stem_e1 -> ppr  <i'endo:>
stem_i1 -> ppr  <i'endo:>
ppr -> postpron  [:]      [tam=[-imv,-ipf,-sub,-tmp,+ger,-part,-inf]]

# Participio
stem_a1 -> pps       <ad:>
stem_e1 -> pps       <id:>
stem_i1 -> pps       <id:>
pps -> adjsuff      [:]    [pos=v,tam=[-imv,-ipf,-sub,-tmp,-ger,+part,-inf],-refl,oi=[-xpl],od=[-xpl]]

# Person endings for most tenses/moods
# Don't consider hables, pongas, etc. to be imperative
person -> end      [s:]    [tam=[-imv],sj=[-1,+2,-p]]
# vosotros
person -> end      <is:>   [tam=[-imv],sj=[-1,+2,+p],-AL]
person -> mos1     <mo:>   [sj=[+1,+p]]
mos1 -> end        [s:]    [tam=[-sub]];[tam=[+sub,+prt]]
mos1 -> postpron   [s:]    [-refl,tam=[+sub,-prt]]
mos1 -> postpron   [:]     [+refl,tam=[+sub,-prt]]
# 2, 3 pers plur non-imperative
person -> end      [n:]    [sj=[-1,+p],tam=[-sub]];[sj=[-1,+p],tam=[+sub,+prt]]
# 2 pers (3 gram) plur imperative
person -> postpron [n:]    [sj=[-1,-2,+p],tam=[+sub,-prt]];[sj=[-1,+2,+p],tam=[+sub,-prt],+AL]
# sing non-imperative; 1st or 3rd person
person -> end      [:]     [sj=[-p,-2],tam=[-sub]];[sj=[-p,-2],tam=[+sub,+prt]]
# 2 pers sing polite (3 gram) imperative
person -> postpron [:]     [sj=[-1,-2,-p],tam=[+sub,-prt]]

# Object suffixes for imperative, pres part, and infinitive

postpron -> end   >cl_post<

# Adjective suffixes for past part

adjsuff -> end     [o:]    [ref=[+xpl,-fem,-p]]
adjsuff -> end     [a:]    [ref=[+xpl,+fem,-p]]
adjsuff -> end     <os:>   [ref=[+xpl,-fem,+p]]
adjsuff -> end     <as:>   [ref=[+xpl,+fem,+p]]

end ->
