import Geometriya

radius = 5
uzunlik = 10
eni = 8
a = 3
b = 4
c = 5
d = 6
S = 20

aylana_uzunligi = Geometriya.AylanaUzunligi(radius)
print("Aylananing uzunligi:", aylana_uzunligi)

aylana_diametri = Geometriya.AylanaDiametri(radius)
print("Aylananing diametri:", aylana_diametri)

doira_yuzi = Geometriya.DoiraYuzi(radius)
print("Doira yuzi:", doira_yuzi)

uchburchak_yuzasi = Geometriya.IxtiyoriyUchburchakYuzasi(a, b, c, radius)
print("Uchburchakning yuzasi:", uchburchak_yuzasi)

uchburchak_perimetri = Geometriya.IxtiyoriyUchburchakPerimetri(a, b, c)
print("Uchburchakning perimetri:", uchburchak_perimetri)

tugri_burchakli_uchburchak_yuzasi = Geometriya.TugriBurchakliUchburchakYuzasi(uzunlik, eni)
print("Tugri burchakli uchburchakuzunligi:", tugri_burchakli_uchburchak_yuzasi)

tugri_burchakli_uchburchak_perimetri = Geometriya.TugriBurchakliUchburchakPerimetri(uzunlik, eni, a)
print("Tugri burchakli uchburchak perimetri:", tugri_burchakli_uchburchak_perimetri)

turtburchak_yuzasi = Geometriya.IxtiyoriyTurtburchakYuzasi(a, b, c, d, radius)
print("Turtburchakning yuzasi:", turtburchak_yuzasi)

kvadrat_yuzi = Geometriya.KvadratYuzasi(uzunlik)
print("Kvadratning yuzi:", kvadrat_yuzi)

kvadrat_perimetri = Geometriya.KvadratPerimetri(uzunlik)
print("Kvadratning perimetri:", kvadrat_perimetri)

turtburchak_yuzi = Geometriya.TugriTurtburchakYuzasi(uzunlik, eni, S)
print("Turtburchakning yuzi:", turtburchak_yuzi)

turtburchak_perimetri = Geometriya.TugriTurtburchakPerimetri(uzunlik, eni, a)
print("Turtburchakning perimetri:", turtburchak_perimetri)

aylana_radiusi = Geometriya.KvgaTashqiChizilganAylanaRadiusi(S)
print("Aylana radiusi:", aylana_radiusi)

yarim_perimetr = Geometriya.YarimPerimetr(a, b, c, d)
print("Yarim perimetr:", yarim_perimetr)

geron_formulasi = Geometriya.GeronFormulasi(yarim_perimetr, a, b, c, d)
print("Geron formulasi:", geron_formulasi)

romb_yuzi = Geometriya.RombYuzasi(uzunlik, eni)
print("Rombning yuzi:", romb_yuzi)

rombning1_diametri = Geometriya.Rombning1Diametri(uzunlik, a)
print("Rombning 1-diametri:", rombning1_diametri)

rombning2_diametri = Geometriya.Rombning2Diametri(eni, b)
print("Rombning 2-diametri:", rombning2_diametri)

trapetsiya_yuzi = Geometriya.TrapetsiyaYuzasi(uzunlik, eni, a)
print("Trapetsiyaning yuzi:", trapetsiya_yuzi)

trapetsiya_balandligi = Geometriya.TrapetsiyaBalandligi(S, uzunlik, eni)
print("Trapetsiyaning balandligi:", trapetsiya_balandligi)

trapetsiya_urtachizigi = Geometriya.TrapetsiyaUrtaChizigi(uzunlik, eni)
print("Trapetsiyaning o'rta chizigi:", trapetsiya_urtachizigi)




