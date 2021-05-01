# Unicamp_webscraper

Um webscraper que retorna se uma dada matéria foi ou será dada em um semestre.
Para utiliza-lo basta preencher as materias que você deseja verificar no disciplinas.json e rodar o script app.py.
Siga [este guia para aprender a preencher as materias](https://github.com/LuizFBR/Unicamp_webscraper#guia-para-preencher-as-mat%C3%A9rias-no-json)

### Instalando as dependências

Esse webscraper utiliza a biblioteca requests para fazer requisições no servidor da DAC e BeautifulSoup4 para o parsing do HTML retornado na requisição

1. Para instalar o BeautifulSoup:
```shell
$ python -m pip install beautifulsoup4
```
ou se você estiver usando python3
```shell
$ python3 -m pip install beautifulsoup4
```
2. Para instalar o requests:
```shell
$ python -m pip install requests
```
ou se você estiver usando python3
```shell
$ python -m pip install requests
```
### Guia para preencher as matérias no .json:
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
            "MC102",
            "MC202"
        ],
        "IFGW": [
            "F 328",
            "F 329"
        ]
    }
}
```
Aqui vemos duas entradas de semestres, 2021-1s e 2021-2s, que o scraper usará para fazer a sua busca.
1. Dentro de cada semestre coloque as siglas de instituto/faculdade, no caso temos "IC" e "IFGW".
2. Dentro de cada uma dessas siglas, coloque os códigos das disciplinas

E se quisermos verificar mais de uma disciplina dentro dadas no mesmo semestre e instituto?
Basta separarmos cada um dos códigos com uma vírgula:<br>
```JSON
{
    "2021-1s": {
        "IC": [
            "MC102",
            "MC202"
        ],
        "IFGW": [
            "F 328",
            "F 329"
        ]
    }
}
```
Após as mudanças, basta rodar o app.py novamente
