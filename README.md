###Comparare Algoritmi de Sortare

Acest proiect implementează, testează și compară performanța mai multor algoritmi de sortare pe seturi de date generate aleatoriu. Se analizează timpii de execuție în funcție de dimensiunea și distribuția datelor pentru a evidenția avantajele și dezavantajele fiecărui algoritm.

## Algoritmi Implementați

- **Radix Sort** (baza 10)
- **Radix Sort** (baza 2^16)
- **Merge Sort**
- **Shell Sort**
- **Quick Sort** (cu pivot ales ca mediana din 3)
- **Heap Sort**
- **Bucket Sort** (pentru numere reale în intervalul [0, 1))

## Descriere

Proiectul are ca scop evaluarea performanței diferiților algoritmi de sortare pe diverse seturi de teste, generate conform specificațiilor din fișierul `tests.in`. Fiecare test conține două valori: 
- **N** – numărul de elemente ce trebuie sortate
- **Max** – valoarea maximă posibilă pentru elementele generate

Rezultatele sunt afișate în consolă și salvate în fișierul `results.txt`.


### Utilizarea aplicatiei

- Asigură-te că fișierul `tests.in` este prezent în același director cu scriptul.
- Deschide un terminal și rulează:
     ```
     python sortari.py
     ```
- Rezultatele vor fi afișate în consolă și salvate în `results.txt`.

