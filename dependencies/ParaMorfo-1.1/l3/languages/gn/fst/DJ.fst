-> start

start -> start       [.-@M]

start -> nasalize    [n:D;ñ:J]
start -> nonnas      [nd:D;j:J]

nonnas -> nonnas     [j:J]
nonnas -> nonnas     [@x-%]
nonnas -> end        [%]

nasalize -> nasalize [@x-%]
nasalize -> nasalize [n:D;ñ:J]

nasalize -> nonnas   [nd:D]
nasalize -> nas      [@N]

nas -> nonnas        [nd:D;j:J]
nas -> nasalize      [n:D;ñ:J]
nas -> nas           [@N;@x]

# after word boundary
end -> end           [.]

nas ->
nonnas ->
start ->
end ->
