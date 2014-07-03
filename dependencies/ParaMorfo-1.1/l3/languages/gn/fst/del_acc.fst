## Deaccent accented characters and delete ! before *.

-> start

start -> start   [.-@V,!,*]
start -> start   [:*]

start -> deacc   [a:á;e:é;i:í;o:ó;u:ú;y:ý;:!]
deacc -> deacc   [a:á;e:é;i:í;o:ó;u:ú;y:ý;:!]
deacc -> deacc   [.-@V,!,*]
deacc -> end     [:*]

start -> nodeacc   [á;é;í;ó;ú;ý;!]
nodeacc -> nodeacc [.-*]

start ->
nodeacc ->
end ->

