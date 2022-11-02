# Вам известен номер квартиры, этажность дома и количество квартир на этаже.
# Задача: написать функцию, которая по заданным параметрам напишет вам,
# в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

def flat(nom_kvartiry, kol_etazhei, kvartir_na_etazhe):
      nom_kvartiry = nom_kvartiry - 1
      c = kol_etazhei * kvartir_na_etazhe
      x = nom_kvartiry // c
      y = str(x+1)
      z = nom_kvartiry % c
      d = z // kvartir_na_etazhe
      s = str(d+1)
      return y + " " + "podezd", s + " " + "etazh"
print(flat(nom_kvartiry=72, kol_etazhei=5, kvartir_na_etazhe=4))


