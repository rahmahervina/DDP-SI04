from animals import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna_ikan}, dan hewan ini jenisnya ikan {self.jenis_ikan}')

print('---Cetak Ikan---')
nemo = ikan('Ikan nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()

koi = ikan('Ikan koi', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
koi.cetak_ikan()