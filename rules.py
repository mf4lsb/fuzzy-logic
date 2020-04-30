inputSet = {
    'CPU': ['Lambat', 'Sedang', 'Cepat'],
    'Core': ['Kurang Optimal', 'Optimal', 'Sangat Optimal'],
    'RAM': ['Kecil', 'Standar', 'Besar']
}

outputSet = {
    'Kelayakan': ['Biasa', 'Standar', 'Bagus']
}

DataMaxEntry = {
    'CPU': 5,
    'Core': 16,
    'RAM': 32
}

fuzzy_1_1, fuzzy_1_2, fuzzy_1_3 = 0, 0, 0
fuzzy_2_1, fuzzy_2_2, fuzzy_2_3 = 0, 0, 0
fuzzy_3_1, fuzzy_3_2, fuzzy_3_3 = 0, 0, 0


inputMyFuzzy = {
    'CPU': {
        'Lambat': [0, 0, 2, 2.4],
        'Sedang': [2, 2.4, 2.6, 3],
        'Cepat': [2.6, 3, 4, 0]
    },
    'Core': {
        'Kurang Optimal': [0, 0, 2, 4],
        'Optimal': [2, 4, 6, 8],
        'Sangat Optimal': [6, 8, 16, 0]
    },
    'RAM': {
        'Kecil': [0, 0, 2, 4],
        'Standar': [2, 4, 8, 16],
        'Besar': [8, 16, 32, 0]
    },
}


def fuzzifikasiTrapesium(values, x):
    a, b, c, d = values
    if a < x < b:
        return (x - a) / (b - a)
    elif c < x < d:
        return (d - x) / (d - c)
    elif b <= x <= c:
        return 1
    elif x <= a or x >= d:
        return 0


def fuzzy_rules(cpuType, cpuValue, coreType, coreValue, ramType, ramValue):

    # Kondisi CPU Lambat
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "1. IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "2. IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Standar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "3. IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Besar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "4. IF CPU = Lambat AND Core = Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "5. IF CPU = Lambat AND Core = Optimal AND RAM = Standar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "6. IF CPU = Lambat AND Core = Optimal AND RAM = Besar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "7. IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "8. IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Standar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "9. IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Besar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]

    # Kondisi CPU Sedang
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "10. IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "11. IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Standar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "12. IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Besar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "13. IF CPU = Sedang AND Core = Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "14. IF CPU = Sedang AND Core = Optimal AND RAM = Standar THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "15. IF CPU = Sedang AND Core = Optimal AND RAM = Besar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "16. IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "17. IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Standar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "18. IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Besar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]

    # Kondisi CPU Cepat
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "19. IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Kecil THEN Kualitas = Biasa")
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "20. IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Standar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "21. IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Besar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "22. IF CPU = Cepat AND Core = Optimal AND RAM = Kecil THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "23. IF CPU = Cepat AND Core = Optimal AND RAM = Standar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "24. IF CPU = Cepat AND Core = Optimal AND RAM = Besar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Kecil":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "25. IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Kecil THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Standar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "26. IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Standar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Besar":
        if min(cpuValue, coreValue, ramValue) != 0:
            print(
                "27. IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Besar THEN Kualitas = Bagus")
        return ["Bagus", min(cpuValue, coreValue, ramValue)]

#     # rules:
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Lambat AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # 2

#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Sedang AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # 3

#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Cepat AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Bagus
