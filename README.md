# Hyrje
Python project implementing classical ciphers: Single Letter Grille Cipher and Tap Code Cipher. Encrypts and decrypts messages while demonstrating knowledge of classical cryptography, algorithm implementation, and GitHub repository management.

# Ekzekutimi i programit

Për të ekzekutuar programin, ndiqni hapat e mëposhtëm:

### 1. Sigurohuni që keni të instaluar Python në sistemin tuaj

Programi është shkruar në Python, prandaj është e domosdoshme që Python të jetë i instaluar dhe i konfiguruar siç duhet në kompjuterin tuaj.
Nëse Python nuk është i instaluar, programi nuk do të mund të ekzekutohet fare.

### 2. Hapni terminalin në folderin e projektit

Hapni folderin e projektit ku ndodhen file-t e projektit, në folderin `ciphers` veçanërisht aty ku gjendet file `main.py`. Sigurohuni që të gjitha file-t e nevojshme (p.sh. algoritmet dhe main file) janë në të njëjtin folder për të shmangur gabimet gjatë importimit.

### 3. Ekzekutoni programin

Në terminal shkruani komandën:

```bash
python main.py
```
Pas ekzekutimit, programi fillon menjëherë dhe shfaq menunë kryesore interaktive në terminal.

## Program Features

Programi është interaktiv dhe i bazuar në menu, ku përdoruesi mund të:

- Zgjedhë një nga dy algoritmet kriptografike (Single-Letter Grille ose Tap Code)
- Jap plaintext-in për enkriptim
- Marrë rezultatin e enkriptimit (ciphertext)
- Kryejë automatikisht dekriptimin për të rikthyer tekstin origjinal
- Shikojë vizualizimin hap pas hapi të procesit të enkriptimit/dekriptimit (opsional)
- Dal nga programi 

Programi është ndërtuar për të demonstruar qartë procesin e enkriptimit dhe dekriptimit dhe për të ndihmuar në kuptimin e funksionimit të algoritmeve kriptografike duke mundësuar vizualizimin e procesit.

### Dalja nga programi

Për të dalë nga programi, përdoruesi duhet të zgjedhë opsionin e daljes nga menuja ose të shkruajë një input që nuk i përket opsioneve të ofruara.
Në këtë rast, programi do të mbyllet dhe do të shfaqet një mesazh konfirmimi që programi është mbyllur me sukses.

# Përshkrimi i algoritmeve
## Tap Code Cipher

### Enkriptimi

### Dekriptimi

## Single-Letter Grille Cipher
**Grille Cipher** është një teknikë kriptografike me origjinë në shekullin XVI, e shpikur nga matematikani italian Girolamo Cardano rreth vitit 1550. Ajo është përdorur në komunikime diplomatike dhe ushtarake gjatë shekujve XVII–XIX. Metoda bazohet në përdorimin e një grille që vendoset mbi një fletë, ku vetëm shkronjat e dukshme përmes këtyre hapjeve formojnë mesazhin sekret dhe grille rrotullohet disa herë (zakonisht 90 shkallë).

Ne kemi implementuar variantin **Single-Letter Grille**, i cili është një formë e thjeshtuar e metodës klasike. Ndryshe nga Grille Cipher tradicional, ky variant nuk përdor rotacion të maskës. Çdo hapje në maskë korrespondon me vetëm një karakter, dhe përdoret vetëm një herë gjatë procesit të enkriptimit. Kjo e bën algoritmin më të thjeshtë për implementim, por edhe më pak fleksibël krahasuar me versionin klasik.

Sot kjo teknikë konsiderohet e pasigurt dhe nuk përdoret në kriptografinë moderne, pasi është e ndjeshme ndaj analizave si brute-force dhe analiza frekuencore. Megjithatë, ajo mbetet një shembull i rëndësishëm historik dhe një mënyrë e mirë për të kuptuar bazat e fshehjes së informacionit (steganografisë).

### Enkriptimi

Enkriptimi në Single Letter Grille bëhet duke vendosur plainttext-in në një matricë duke përdorur një grille.

**1.** Fillimisht krijohet një matricë bosh me madhësi 6x6 në rastin tonë. 

**2.** Më pas definohet maska (grille), e cila përcakton saktë pozicionet ku do të vendosen shkronjat, ku çdo pozicion përdoret vetëm një herë dhe nuk ka rotacion të maskës.  

**3.** Plaintext-i merret dhe secili karakter vendoset vetëm në pozicionet e parapërcaktuara të maskës, një nga një sipas rendit të tij.

**4.** Pozicionet e mbetura në matricë mbushen me karaktere të rastësishme (shkronja dhe numra), për të fshehur strukturën e mesazhit.

**5.** Në fund, matrica lexohet rresht pas rreshti për të krijuar tekstin e enkriptuar (ciphertext).

**Ideja kryesore:** Meqë karakteret mbushëse janë të rastësishme, i njëjti mesazh mund të prodhojë ciphertext të ndryshëm sa herë ekzekutohet dhe vetëm personi që posedon maskën e saktë mund të gjej mesazhin origjinal.

### Dekriptimi

Dekriptimi në Single Letter Grille bëhet duke përdorur të njëjtën grille (maskë) që është përdorur gjatë enkriptimit.

**1.** Fillimisht ciphertext-i ndahet në blloqe prej 36 karakteresh (6x6).

**2.** Çdo bllok i ciphertext-it vendoset në një matricë 6x6, duke u mbushur matrica me karaktere rresht pas rreshti.

**3.** Më pas aplikohet maska(grille), e cila përcakton saktë pozicionet ku gjendet plaintext-i.

**4.** Karakteret lexohen vetëm nga pozicionet e paracaktuara të maskës, një nga një sipas rendit të tyre.

**5.** Karakteret e lexuara bashkohen për të formuar mesazhin origjinal (plaintext).

**6.** Në fund hiqen karakteret 'X' të përdorura si padding gjatë enkriptimit.

**Ideja kryesore:** Vetëm duke përdorur të njëjtën maskë mund të identifikohen pozicionet e sakta në matricë dhe të gjendet mesazhi origjinal.

# Shembuj të ekzekutimit
