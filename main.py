import sorozat
import bevezetes
bevezetes.autok()
lottoszamok = sorozat.generalt_lottoszamok()  # Generáljuk a lottószámokat
egyjegyuek = sorozat.egyjegyuek_szama(lottoszamok)  # Számoljuk meg az egyjegyű számokat
sorozat.konzol_kiir(lottoszamok, egyjegyuek)  # Kiírás a konzolra
sorozat.file_kiir(lottoszamok, egyjegyuek)  # Kiírás fájlba

