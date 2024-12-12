from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.jenis_ular = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah {self.warna_ular} dan jenis ularnya adalah {self.jenis_ular}')

print('---Cetak Ular---')
piton = ular('Ular Piton', 'daging', 'darat', 'bertelur', 'hitam', 'berbisa')
piton.cetak_ular()

sanca = ular('Ular Sanca', 'daging', 'darat', 'bertelur', 'coklat', 'berbisa')
sanca.cetak_ular()