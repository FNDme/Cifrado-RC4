# RC4 Cipher

The RC4 cipher is one of the most widely used stream ciphers and continues to be used despite its exclusion from security standards.

## Utilización
```
python GUI.py
```

## Cómo funciona
This cipher is based on the following steps:

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