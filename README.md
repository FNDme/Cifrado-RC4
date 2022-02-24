# RC4 Cipher

El cifrado RC4 es uno de los sistemas de cifrado en flujo más utilizados, aún habiendo sido excluido de cualquier estandar de alta seguridad.

## Utilización
```
python GUI.py
```

## Cómo funciona
Este cifrado se basa en los siguientes dos algoritmos, uno se encarga de generar el estado inicial a partir de una clave, y el otro de generar el byte que usaremos para realizar la suma binaria con lo que vayamos a cifrar:

- Key Scheduling Algorithm:
    ```
    for i = 0 to 255 {
        S[i] = i;
        K[i] = seed[i mod seed.length];
    }
    j = 0;
    for i = 0 to 255 {
        j = (j + S[i] + K[i]) mod 256;
        swap(S[i], S[j]);
    }
    ```
- Pseudo.Random Generation Algorithm:
    ```
    i = 0;
    j = 0;
    for everyByteOfData {
        i = (i + 1) mod 256;
        j = (j + S[i]) mod 256;
        swap(S[i], S[j]);
        t = (S[i] + S[j]) mod 256;
        Use S[t] value
    }
    ```
    
## Contribuir
Las solicitudes de modificación son bienvenidas. Para los cambios importantes, por favor, abra una cuestión en primer lugar para discutir lo que le gustaría cambiar.

Por favor, asegúrese de actualizar las pruebas según corresponda.