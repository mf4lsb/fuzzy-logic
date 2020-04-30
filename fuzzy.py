# Input =
# CPU = [Lambat, sedang, cepat]
# Core = [Kurang Optimal, Optimal, sangat optimal]
# RAM = [Kecil, standar, besar]

# Output=
# Kelayakan = [biasa, standar, bagus]
# Input =
# CPU = [Lambat, sedang, cepat]
# Core = [Kurang Optimal, Optimal, sangat optimal]
# RAM = [Kecil, standar, besar]

# Output=
# Kelayakan = [biasa, standar, bagus]


import rules
import matplotlib.pyplot as plt


def check(key, data):
    if(rules.DataMaxEntry[key] < data) or (data < 0):
        return False
    return True


def data_input():
    dataUser = []
    for key in rules.inputSet:
        while True:
            if key == 'CPU':
                entry = float(input(f'Masukkan {key}: '))
            else:
                entry = int(input(f'Masukkan {key}: '))

            if check(key, entry):
                dataUser.append(entry)
                break
            else:
                True

    return dataUser


def fuzzifikasiNew(data):
    cpu, core, ram = data
    fuzzy = []
    for inputName, inputAttribute in rules.inputMyFuzzy.items():
        for attribute, values in inputAttribute.items():
            if inputName == "CPU":
                temp = rules.fuzzifikasiTrapesium(values, cpu)
            elif inputName == "Core":
                temp = rules.fuzzifikasiTrapesium(values, core)
            else:
                temp = rules.fuzzifikasiTrapesium(values, ram)
            fuzzy.append([attribute, round(temp, 2)])
    return fuzzy


def inferensi(cpu, core, ram):
    inferens = []
    print("\nRules yang digunakan adalah: ")
    for cpuType, cpuValue in cpu:
        for coreType, coreValue in core:
            for ramType, ramValue in ram:
                inferens.append(rules.fuzzy_rules(
                    cpuType, cpuValue, coreType, coreValue, ramType, ramValue))
    return inferens


def defuzzifikasi(biasa, bagus, sampleTitik):
    hasil, cobaBiasa, cobaBagus, k, l, tempMiring = (0 for i in range(6))
    for i in range(0, 101, sampleTitik):
        if i == 0:
            pass
        elif i <= 50:  # Nilai kelayakan Biasa
            cobaBiasa = i * biasa
            hasil += cobaBiasa
            k += 1
        elif i == 60:
            if (biasa and bagus) <= 0.5:
                if biasa > bagus:
                    cobaBiasa = i * biasa
                    hasil += cobaBiasa
                    k += 1
                else:
                    cobaBagus = i * bagus
                    hasil += cobaBagus
                    l += 1
            else:
                pass

        else:  # Nilai kelayakan Bagus
            cobaBagus = i * bagus
            hasil += cobaBagus
            l += 1
    hasil = round(hasil / ((biasa * k) + (bagus * l)), 2)
    return hasil


if __name__ == "__main__":

    i = 0
    data = data_input()
    nilai = fuzzifikasiNew(data)
    cpu, core, ram = ([] for i in range(3))
    for jenis, nilaiJenis in nilai:
        if jenis == "Lambat" or jenis == "Sedang" or jenis == "Cepat":
            cpu.append([jenis, nilaiJenis])
        if jenis == "Kurang Optimal" or jenis == "Optimal" or jenis == "Sangat Optimal":
            core.append([jenis, nilaiJenis])
        if jenis == "Kecil" or jenis == "Standar" or jenis == "Besar":
            ram.append([jenis, nilaiJenis])

    # Fuzzifikasi
    j = 0
    print(f'\nNilai Fuzzifikasi:')
    for keys, values in rules.inputSet.items():
        print(f'- {keys} ')
        for value in values:
            if nilai[j] != 0 and nilai[j][1] != 0:
                print(f'{value}: {nilai[j][1]}')
            j += 1

    # Inferensi
    temp, temp2 = ([] for i in range(2))
    nilaiInferensi = inferensi(cpu, core, ram)
    for NK, nilai in nilaiInferensi:
        if NK == "Biasa":
            temp.append(nilai)
        else:
            temp2.append(nilai)

    inferensiBiasa = max(temp)
    inferensiBagus = max(temp2)

    print(f"\nHasil Inferensi: \n"
          f"Biasa: {inferensiBiasa}\n"
          f"Bagus: {inferensiBagus}")

    sampleTitik = 10  # Sample titik diberikan nilai 10

    # Defuzzifikasi
    nilaiDefuzzifikasi = defuzzifikasi(
        inferensiBiasa, inferensiBagus, sampleTitik)
    print(
        f'\nSample Titik: {sampleTitik}\n'
        f'\nHasil Deffuzifikasi: \nNilai Kelayakan Kualitas: {nilaiDefuzzifikasi}')

    # Tabel Keanggotaan
    fig = plt.figure(figsize=(8, 6))
    # Inputan CPU
    ax1 = fig.add_subplot(221)
    t1 = [0, 1, 2, 2.4]
    t2 = [1, 1, 1, 0]
    x1 = [2, 2.4, 2.6, 3]
    x2 = [0, 1, 1, 0]
    z1 = [2.6, 3, 3.1]
    z2 = [0, 1, 1]
    plt.plot(t1, t2, label="Lambat")
    plt.plot(x1, x2, label="Sedang")
    plt.plot(z1, z2, label="Cepat")
    plt.xlabel('GHz (Speed)')
    plt.ylabel('\u03BC')
    plt.title("CPU", fontsize="20", color="red")
    plt.legend()

    # Inputan Core
    ax2 = fig.add_subplot(222)
    x1 = [0, 2, 4]
    x2 = [1, 1, 0]
    t1 = [2, 4, 6, 8]
    t2 = [0, 1, 1, 0]
    z1 = [6, 8, 9]
    z2 = [0, 1, 1]
    plt.plot(x1, x2, label="Kurang Optimal")
    plt.plot(t1, t2, label="Optimal")
    plt.plot(z1, z2, label="Sangat Optimal")
    plt.xlabel('Jumlah')
    plt.ylabel('\u03BC')
    plt.title("Core", fontsize="20", color="red")
    plt.legend()

    # Inputan RAM
    ax3 = fig.add_subplot(223)
    t1 = [0, 1, 2, 4]
    t2 = [1, 1, 1, 0]
    x1 = [2, 4, 8, 16]
    x2 = [0, 1, 1, 0]
    z1 = [8, 16, 20]
    z2 = [0, 1, 1]
    plt.plot(t1, t2, label="Kecil")
    plt.plot(x1, x2, label="Standard")
    plt.plot(z1, z2, label="Besar")
    plt.title("RAM", fontsize="20", color="red")
    plt.xlabel('Gigabyte')
    plt.ylabel('\u03BC')
    plt.legend()

    # Outputan Nilai Kelayakan
    ax4 = fig.add_subplot(224)
    t1 = [0, 50, 70]
    t2 = [1, 1, 0]
    x1 = [50, 70, 80, 100]
    x2 = [0, 1, 1, 1]
    plt.plot(t1, t2, label="Biasa")
    plt.plot(x1, x2, label="Bagus")
    plt.title("Nilai Kelayakan", fontsize="12", color="green")
    plt.xlabel('Kualitas')
    plt.ylabel('\u03BC')
    plt.legend()

    fig.tight_layout()
    plt.show()
