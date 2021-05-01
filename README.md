# Unicamp_webscraper

Um webscraper que retorna se uma dada matéria foi ou será dada em um semestre.
Para utiliza-lo basta preencher as materias que você deseja verificar no disciplinas.json e rodar o script app.py.

# Guia para preencher as matérias no .json:
Um exemplo do disciplinas.json:

```json
{
    "2021-1s": {
        "IC": [
            "MC102"
        ],
        "IFGW": [
            "F 328"
        ]
    },
    "2021-2s": {
        "IC": [
            "MC102"
        ],
        "IFGW": [
            "F 328"
        ]
    }
}
```
Aqui vemos duas entradas de semestres, 2021-1s e 2021-2s, que o scraper usará para fazer a sua busca.
Dentro de cada semestre coloque as siglas de instituto/faculdade, no caso temos "IC" e "IFGW".
Dentro de cada uma dessas chaves, coloque os códigos das disciplinas

E se quisermos verificar mais de uma disciplina dentro dadas no mesmo semestre e instituto?
Basta separarmos cada um dos códigos com uma vírgula:
```JSON
{
    "2021-1s": {
        "IC": [
            "MC102"
        ],
        "IFGW": [
            "F 328"
        ]
    }
}
```
