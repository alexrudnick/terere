## Deaccent accented vowels before other accented vowels
## repurahéireína -> repuraheireína

-> start

start -> start    [.-@V]
start -> retacc   [@V]
retacc -> retacc  [.-@V]

start -> deacc    [a:á;e:é;i:í;o:ó;u:ú;y:ý;A:Á;E:É;I:Í;O:Ó;U:Ú;Y:Ý]
deacc -> deacc    [.-@V]
deacc -> deacc    [a:á;e:é;i:í;o:ó;u:ú;y:ý]
deacc -> end      [@V]
end -> end        [.]

start ->
retacc ->
end ->