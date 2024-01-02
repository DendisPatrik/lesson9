def merge_sort(cisla):
    dlzka = len(cisla)
    if (dlzka == 1):
        return
    stred = dlzka // 2
    lava = cisla[:stred]
    prava = cisla[stred:]
    merge_sort(lava)
    merge_sort(prava)
    merge(lava, prava, cisla)

def merge(lava, prava, cisla):
    lavaDlzka = len(lava)
    pravaDlzka = len(prava)
    lavyIndex = 0
    pravyIndex = 0
    index = 0
    while lavyIndex < lavaDlzka and pravyIndex < pravaDlzka:
        if lava[lavyIndex] < prava[pravyIndex]:
            cisla[index] = lava[lavyIndex]
            lavyIndex += 1
            index += 1
        else:
            cisla[index] = prava[pravyIndex]
            pravyIndex += 1
            index += 1

    while lavyIndex < lavaDlzka:
        cisla[index] = lava[lavyIndex]
        lavyIndex += 1
        index += 1

    while pravyIndex < pravaDlzka:
        cisla[index] = prava[pravyIndex]
        pravyIndex += 1
        index += 1

cisla = [6, 5, 2, 8, 20, 4]
merge_sort(cisla)
print(cisla)