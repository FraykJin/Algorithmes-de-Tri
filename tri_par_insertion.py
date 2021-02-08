#Tri par insertion ascendant

def sort_asc(tab):
    for j in range(1, len(tab)):
        cle = tab[j]
        i = j - 1
        while i >= 0 and tab[i] > cle:
            tab[i+1] = tab[i]
            i = i - 1
        tab[i+1] = cle


#Tri par insertion descendant

def sort_desc(tab):
    for j in range(1, len(tab)):
        cle = tab[j]
        i = j - 1
        while i >= 0 and cle > tab[i]:
            tab[i+1] = tab[i]
            i = i - 1
        tab[i+1] = cle


tab = [5, 2, 4, 6, 1, 3, 2]

sort_asc(tab)
print(tab, 'ascendant')
sort_desc(tab)
print(tab, 'descendant')
