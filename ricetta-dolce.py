# Dati della ricetta:
# Ingredienti:
albumi = 180  # ml
zucchero = 125  # g
farina_manitoba = 120  # g
cacao_amaro = 30  # g
latte = 150  # ml
olio_semi = 70  # ml
lievito_dolci = 1  # bustina (trascurabile per le macro)

# Macronutrienti per 100 g di ciascun ingrediente (approssimativi)
# Fonti generali per i valori di macronutrienti:

# Albumi: 100 g = 10 g di proteine, 0 g di grassi, 0 g di carboidrati
albumi_proteine = 10 / 100
albumi_grassi = 0 / 100
albumi_carboidrati = 0 / 100

# Zucchero: 100 g = 0 g di proteine, 0 g di grassi, 100 g di carboidrati
zucchero_proteine = 0 / 100
zucchero_grassi = 0 / 100
zucchero_carboidrati = 100 / 100

# Farina Manitoba: 100 g = 12 g di proteine, 1 g di grassi, 75 g di carboidrati
farina_proteine = 12 / 100
farina_grassi = 1 / 100
farina_carboidrati = 75 / 100

# Cacao amaro: 100 g = 20 g di proteine, 10 g di grassi, 50 g di carboidrati
cacao_proteine = 20 / 100
cacao_grassi = 10 / 100
cacao_carboidrati = 50 / 100

# Latte: 100 ml = 3.3 g di proteine, 3.7 g di grassi, 4.7 g di carboidrati
latte_proteine = 3.3 / 100
latte_grassi = 3.7 / 100
latte_carboidrati = 4.7 / 100

# Olio di semi: 100 ml = 0 g di proteine, 100 g di grassi, 0 g di carboidrati
olio_semi_proteine = 0 / 100
olio_semi_grassi = 100 / 100
olio_semi_carboidrati = 0 / 100

# Calorie per 100g di ciascun ingrediente (approssimativi)
# Albumi: 52 kcal
calorie_albumi = 52 / 100

# Zucchero: 400 kcal
calorie_zucchero = 400 / 100

# Farina Manitoba: 360 kcal
calorie_farina = 360 / 100

# Cacao amaro: 250 kcal
calorie_cacao = 250 / 100

# Latte: 60 kcal
calorie_latte = 60 / 100

# Olio di semi: 900 kcal
calorie_olio = 900 / 100

# Ora calcoliamo la quantità totale di ciascun macronutriente nella ricetta

# Proteine
proteine_totali = (
    albumi * albumi_proteine + 
    zucchero * zucchero_proteine + 
    farina_manitoba * farina_proteine + 
    cacao_amaro * cacao_proteine + 
    latte * latte_proteine + 
    olio_semi * olio_semi_proteine
)

# Grassi
grassi_totali = (
    albumi * albumi_grassi + 
    zucchero * zucchero_grassi + 
    farina_manitoba * farina_grassi + 
    cacao_amaro * cacao_grassi + 
    latte * latte_grassi + 
    olio_semi * olio_semi_grassi
)

# Carboidrati
carboidrati_totali = (
    albumi * albumi_carboidrati + 
    zucchero * zucchero_carboidrati + 
    farina_manitoba * farina_carboidrati + 
    cacao_amaro * cacao_carboidrati + 
    latte * latte_carboidrati + 
    olio_semi * olio_semi_carboidrati
)

# Calorie totali
calorie_totali = (
    albumi * calorie_albumi + 
    zucchero * calorie_zucchero + 
    farina_manitoba * calorie_farina + 
    cacao_amaro * calorie_cacao + 
    latte * calorie_latte + 
    olio_semi * calorie_olio
)

# Peso totale della ricetta
peso_totale = albumi + zucchero + farina_manitoba + cacao_amaro + latte + olio_semi

# Macro e calorie per 100g
macro_per_100g = {
    "Proteine (g)": (proteine_totali / peso_totale) * 100,
    "Grassi (g)": (grassi_totali / peso_totale) * 100,
    "Carboidrati (g)": (carboidrati_totali / peso_totale) * 100,
    "Calorie (kcal)": (calorie_totali / peso_totale) * 100
}

peso_totale, macro_per_100g


macro_totali_completi = {
    "Proteine (g)": proteine_totali,
    "Grassi (g)": grassi_totali,
    "Carboidrati (g)": carboidrati_totali,
    "Calorie (kcal)": calorie_totali
}

macro_totali_completi
