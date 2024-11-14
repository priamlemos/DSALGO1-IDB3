from PositionalList import PositionalList as PositionalList

P = PositionalList()

P.add_first(1)
P.add_first(72)
P.add_first(81)
P.add_first(25)
P.add_first(65)
P.add_first(91)
P.add_last(11)

def insertion_sort_descending(L):
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_descending(P)
print("The Descending order are: ")
# Print the sorted elements
for x in P:
    print(x)

def insertion_sort_ascending(L):
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_ascending(P)
print("The Ascending order are: ")
# Print the sorted elements
for x in P:
    print(x)


