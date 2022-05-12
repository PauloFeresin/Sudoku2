## exercicio 1383 do beecrowd - impacta

sudoku = []

for linhas in range(9):
    linha = []
    for colunas in range(9):
        linha.append(int(input()))
        
    sudoku.append(linhas)

print(sudoku)