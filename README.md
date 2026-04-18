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

Tap Code është një mënyrë shumë e thjeshtë për të koduar mesazhe tekstuale, ku çdo shkronjë përfaqësohet me dy grupe trokitjesh ose pikash. Ai bazohet në një matricë 5×5 të alfabetit latin dhe zakonisht shkronja **K** përfaqësohet nga **C**, sepse matrica ka vetëm 25 vende.

Për të transmetuar një shkronjë, fillimisht jepet numri i trokitjeve për rreshtin dhe pastaj, pas një pauze të shkurtër, numri i trokitjeve për kolonën. Për shembull, shkronja **B** jepet me një trokitje, pauzë, dhe pastaj dy trokitje. 

Kjo metodë është përdorur shpesh nga të burgosurit për të komunikuar mes tyre duke trokitur në mure, tuba ose shufra metalike. Tap Code konsiderohet i lehtë për t’u mësuar dhe praktik për situata ku nuk mund të flitet hapur.

Në këtë projekt, Tap Code përdoret për të enkriptuar tekstin duke e kthyer çdo shkronjë në pozicionin e saj përkatës në matricën 5×5.
### Enkriptimi
Në këtë projekt, enkriptimi me **Tap Code** është realizuar në Python duke përdorur një matricë **5x5** që përmban shkronjat e alfabetit. Çdo shkronjë përfaqësohet sipas **rreshtit** dhe **kolonës** ku ndodhet në këtë matricë. Për shkak se matrica ka vetëm 25 vende, shkronja **K** trajtohet si **C**.

Procesi i enkriptimit është ndërtuar me disa hapa të thjeshtë:

- Fillimisht krijohet matrica 5x5 e Tap Code.
- Pastaj përdoret funksioni `find_position(letter)` për të gjetur pozitën e një shkronje në matricë.
- Funksioni `encode_letter(letter)` e kthen një shkronjë në formën e saj Tap Code, duke përdorur pika për rreshtin dhe kolonën.
- Funksioni `encrypt_tap_code(text)` përdoret për të enkriptuar tekstin e plotë. Ky funksion:
  - e pastron tekstin me `strip()`
  - e kthen në shkronja të mëdha me `upper()`
  - kontrollon çdo karakter me `for`
  - enkripton vetëm shkronjat me `isalpha()`
  - i injoron karakteret e pambështetura
  - hapësirat i zëvendëson me `/`

Përveç enkriptimit kryesor, në projekt është shtuar edhe funksioni `visualize_tapcode_process(plainText)`, i cili tregon hap pas hapi procesin e shndërrimit të çdo shkronje në Tap Code. Në këtë pjesë është përdorur edhe moduli `time` me `time.sleep()` për ta bërë vizualizimin më të qartë.

Ky implementim e bën algoritmin të thjeshtë për t’u kuptuar, testuar dhe përdorur për enkriptimin e fjalëve dhe fjalive me Tap Code.

### Dekriptimi

## Single-Letter Grille Cipher
**Grille Cipher** është një teknikë kriptografike me origjinë në shekullin XVI, e shpikur nga matematikani italian Girolamo Cardano rreth vitit 1550. Ajo është përdorur në komunikime diplomatike dhe ushtarake gjatë shekujve XVII–XIX. Metoda bazohet në përdorimin e një grille që vendoset mbi një fletë, ku vetëm shkronjat e dukshme përmes këtyre hapjeve formojnë mesazhin sekret dhe grille rrotullohet disa herë (zakonisht 90 shkallë).

Ne kemi implementuar variantin **Single-Letter Grille**, i cili është një formë e thjeshtuar e metodës klasike. Ndryshe nga Grille Cipher tradicional, ky variant nuk përdor rotacion të maskës. Çdo hapje në maskë korrespondon me vetëm një karakter, dhe përdoret vetëm një herë gjatë procesit të enkriptimit. Kjo e bën algoritmin më të thjeshtë për implementim, por edhe më pak fleksibël krahasuar me versionin klasik.

Sot kjo teknikë konsiderohet e pasigurt dhe nuk përdoret në kriptografinë moderne, pasi është e ndjeshme ndaj analizave si brute-force dhe analiza frekuencore. Megjithatë, ajo mbetet një shembull i rëndësishëm historik dhe një mënyrë e mirë për të kuptuar bazat e fshehjes së informacionit (steganografisë).

### Enkriptimi

Enkriptimi në Single-Letter Grille bëhet duke vendosur plaintext-in në një matricë duke përdorur një grille.

- Fillimisht krijohet një matricë bosh, me madhësi 6x6 në rastin tonë. 

- Më pas definohet maska (grille), e cila përcakton saktë pozicionet ku do të vendosen shkronjat, ku çdo pozicion përdoret vetëm një herë dhe nuk ka rotacion të maskës.  

- Plaintext-i merret dhe secili karakter vendoset vetëm në pozicionet e parapërcaktuara të maskës, një nga një sipas rendit të tij.

- Pozicionet e mbetura në matricë mbushen me karaktere të rastësishme (shkronja dhe numra), për të fshehur strukturën e mesazhit.

- Në fund, matrica lexohet rresht pas rreshti për të krijuar tekstin e enkriptuar (ciphertext).

**Ideja kryesore:** Meqë karakteret mbushëse janë të rastësishme, i njëjti mesazh mund të prodhojë ciphertext të ndryshëm sa herë ekzekutohet dhe vetëm personi që posedon maskën e saktë mund të gjej mesazhin origjinal.

### Dekriptimi

Dekriptimi në Single Letter Grille bëhet duke përdorur të njëjtën grille (maskë) që është përdorur gjatë enkriptimit.

- Fillimisht ciphertext-i ndahet në blloqe prej 36 karakteresh (6x6).

- Çdo bllok i ciphertext-it vendoset në një matricë 6x6, duke u mbushur matrica me karaktere rresht pas rreshti.

- Më pas aplikohet maska(grille), e cila përcakton saktë pozicionet ku gjendet plaintext-i.

- Karakteret lexohen vetëm nga pozicionet e paracaktuara të maskës, një nga një sipas rendit të tyre.

- Karakteret e lexuara bashkohen për të formuar mesazhin origjinal (plaintext).

- Në fund hiqen karakteret 'X' të përdorura si padding gjatë enkriptimit.

**Ideja kryesore:** Vetëm duke përdorur të njëjtën maskë mund të identifikohen pozicionet e sakta në matricë dhe të gjendet mesazhi origjinal.

# Shembuj të ekzekutimit
