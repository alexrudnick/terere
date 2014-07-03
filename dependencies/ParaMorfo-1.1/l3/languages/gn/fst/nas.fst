-> start

start -> start       [.-@M]

start -> nasalize    [m:B;n:D;ñ:J]
start -> nonnas      [mb:B;nd:D;j:J]

nonnas -> nonnas     [j:J]
nonnas -> nonnas     [@x-%]
nonnas -> end        [%]

nasalize -> nasalize [@x-%]
nasalize -> nasalize [m:B;n:D;ñ:J]

nasalize -> nonnas   [mb:B;nd:D]
nasalize -> nas      [@N]

nas -> nonnas        [mb:B;nd:D;j:J]
nas -> nasalize      [m:B;n:D;ñ:J]
nas -> nas           [@N;@x]

# after word boundary
end -> end           [.]

nas ->
nonnas ->
start ->
end ->
