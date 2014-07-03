## realizar prefijo de 3 persona, cambiando <h inicial si es necesario.

-> start

start -> start    [.-I]

# I antes de vocal o consonante salvo <h
start -> I        [I]
# insertar J antes de vocal
I -> insJ         [J:]
insJ -> start     [@W]
# no cambiar nada en otros casos
I -> start        [.-@W,<h]

# I antes de <h
# eliminar I
start -> delI     [:I]
# realizar <h como h
delI -> start     [h:<h]

start ->