## realizar prefijo de 3 persona, cambiando <h inicial si es necesario.

-> start

start -> start    [.-I,^]

# I<h -> h
start -> delI     [:I]
delI -> start     [h:<h]

# realize I as i otherwise
start -> I        [i:I]
# I antes de vocal o consonante salvo <h
# insertar J antes de vocal
I -> insJ         [J:]
insJ -> start     [@W]
# no cambiar nada en otros casos
I -> start        [.-@W,<h]

# ^<h -> r
start -> ^        [:^]
^ -> start        [r:<h]
# just delete ^ in other cases
^ -> start        [.-<h]

start ->