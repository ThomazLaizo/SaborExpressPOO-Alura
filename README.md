# 🍽️ Sabor Express POO

Versão do **Sabor Express** reescrita com **Programação Orientada a Objetos**, desenvolvida em Python durante o curso da Alura. O sistema modela restaurantes, avaliações de clientes e um cardápio com diferentes tipos de item (prato, bebida e porção), cada um com sua própria regra de desconto.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![POO](https://img.shields.io/badge/paradigma-POO-blueviolet)
![Terminal](https://img.shields.io/badge/interface-terminal-black?logo=windowsterminal&logoColor=white)
![Linguagem principal](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)

> 🔗 Existe também a [versão procedural do Sabor Express](https://github.com/ThomazLaizo/SaborExpress-Alura), feita com menu interativo no terminal. Este projeto foca na modelagem com classes.

## ✨ Funcionalidades

**Restaurantes**
- Cadastro com nome (formatado automaticamente em *Title Case*) e categoria
- Controle de status **Ativo/Inativo** (todo restaurante nasce inativo)
- Listagem de todos os restaurantes em formato de tabela, com nome, categoria, média de avaliações e status

**Avaliações**
- Registro de avaliações com nome do cliente e nota
- Aceita apenas notas entre **0 (exclusive) e 5**
- Cálculo automático da **média das notas** (exibe `--` enquanto não há avaliações)

**Cardápio**
- Três tipos de item: **Prato**, **Bebida** e **Porção**
- Cada tipo tem seu **desconto próprio**:

| Item | Desconto | Atributo extra |
|---|---|---|
| Prato | 5% | `descricao` |
| Bebida | 8% | `tamanho` |
| Porção | 7% | `tamanho` |

- Apenas itens do tipo `ItemCardapio` podem ser adicionados ao cardápio
- Exibição do cardápio numerado, com nome, preço e descrição ou tamanho

## 🧠 Conceitos de POO aplicados

| Conceito | Onde aparece |
|---|---|
| **Herança** | `Prato`, `Bebida` e `Porcao` herdam de `ItemCardapio` |
| **Classe abstrata** | `ItemCardapio` usa `ABC` e define `aplicar_desconto` como método abstrato |
| **Polimorfismo** | Cada subclasse implementa `aplicar_desconto` com um percentual diferente |
| **Composição** | `Restaurante` contém listas de `Avaliacao` e de `ItemCardapio` |
| **Encapsulamento** | Atributos protegidos por convenção (`_nome`, `_preco`, `_ativo`, `_nota`...) |
| **Propriedades** | `@property` em `ativo`, `media_avaliacoes` e `exibir_cardapio` |
| **Atributo e método de classe** | Lista `restaurantes` e `@classmethod listar_restaurantes` |
| **`super()`** | Construtores das subclasses chamam `ItemCardapio.__init__` |
| **Sobrescrita de `__str__`** | Representação textual de `Restaurante` e dos itens do cardápio |
| **Verificação de tipos** | `isinstance` e `hasattr` para validar e exibir os itens |
| **Módulos e pacotes** | Código dividido em arquivos e na pasta `cardapio/` |

## 🗂️ Estrutura do projeto

```
oo-saborExpress/
└── modelos/
    ├── app.py                 # Ponto de entrada (cria restaurantes e itens de exemplo)
    ├── restaurante.py         # Classe Restaurante
    ├── avaliacao.py           # Classe Avaliacao
    └── cardapio/
        ├── itemcardapio.py    # Classe abstrata ItemCardapio
        ├── prato.py           # Prato (desconto de 5%)
        ├── bebida.py          # Bebida (desconto de 8%)
        └── porcao.py          # Porcao (desconto de 7%)
```

## ⚙️ Requisitos

- **Python 3.12 ou superior** (o código usa aspas aninhadas em f-strings, recurso das versões mais recentes)
- Nenhuma biblioteca externa é necessária

## ▶️ Como executar

Os imports do projeto são relativos à pasta `modelos/`, então o programa deve ser executado **de dentro dela**:

```bash
# 1. Clone o repositório
git clone https://github.com/ThomazLaizo/oo-saborExpress.git

# 2. Entre na pasta modelos
cd oo-saborExpress/modelos

# 3. Execute
python app.py
```

Saída esperada:

```
Cardapio do restaurante Japan In Box

1. Nome: Porção_Sushi              | Preço: R$9.3                       | Tamanho: Médio
```

## 🖥️ Exemplo de uso

```python
from restaurante import Restaurante
from cardapio.prato import Prato

restaurante = Restaurante('dona benta', 'Padaria')   # nome vira "Dona Benta"
restaurante.alterar_estado()                         # Inativo -> Ativo
restaurante.receber_avaliacao('Maria', 4.5)
restaurante.receber_avaliacao('João', 5)

pao = Prato('Pão Francês', 1.50, 'O melhor da cidade!')
pao.aplicar_desconto()                               # aplica 5% de desconto
restaurante.adicionar_cardapio(pao)

Restaurante.listar_restaurantes()
restaurante.exibir_cardapio
```

> ⚠️ Os dados ficam apenas **em memória**: ao encerrar o programa, tudo é perdido.

## 🛣️ Roadmap

- [ ] Persistência dos dados (arquivo JSON ou banco de dados)
- [ ] Menu interativo integrado às classes, como na versão procedural
- [ ] Trocar `@abstractclassmethod` (obsoleto) por `@abstractmethod`
- [ ] Transformar `exibir_cardapio` em método comum (hoje é uma `@property` que imprime)
- [ ] Arredondar o preço para 2 casas após aplicar o desconto
- [ ] Informar o usuário quando uma nota de avaliação for inválida (hoje ela é ignorada em silêncio)
- [ ] Impedir restaurantes duplicados
- [ ] Remover o atributo `itens` de `ItemCardapio`, que não é usado
- [ ] Testes automatizados

## 📄 Licença

Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Feito por **[Thomaz Laizo](https://github.com/ThomazLaizo)**.
