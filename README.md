# Trabalho Final – Computação Gráfica  
## Guilherme Dias Correa - 22352926
**Curvas de Bézier, Superfícies e Rendering (Phong)**

Este repositório contém a implementação completa de **todas as tarefas do PDF**, com os códigos **organizados em arquivos separados**, conforme solicitado.

---

> [!CAUTION] Usuário Linux/Ubuntu
caso o erro a seguir aconteça:

_OpenGL.error.Error: Attempt to retrieve context when no valid context_

no `terminal` ou no `.bashrc` execute

 ```bash 

export PYOPENGL_PLATFORM='glx'

```

isso deve consertar o erro e permitir que a janela apareça.

---
## 1 Estrutura de Diretorios

```
trabalho_final/
│
├── bezier/          # Exercícios 1 e 2
│   ├── de_casteljau.py
│   ├── bezier_utils.py
│   ├── grau_reducao.py
│   ├── grau_aumento.py
│   └── main_bezier.py
│
├── superfices/      # Exercícios 3 e 4
│   ├── revolucao.py
│   ├── varredura.py
│   └── asa_aviao.py
│
├── rendering/       # Exercício 5
│   ├── phong.py
│   └── cena.py
│
├── requirements.txt
└── README.md

```

---

## 2 Instalação do ambiente

### 2.1 Criar ambiente virtual (opcional, recomendado)

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```
### 2.2 Instalar requerimentos
```bash
pip install -r req.txt
```

## 3 Redução de Grau de Curva de Bézier: Exercício 1


**O que é atendido**

- Redução de curva cúbica → quadrática

- Manutenção dos pontos extremos

- Cálculo de Q1 = (3/4)P1 + (1/4)P2

- Avaliação do erro máximo

- Uso do algoritmo de De Casteljau

- Comparação gráfica entre as curvas

**Testes utilizados**

- **Teste 1**: Curva cúbica simples com pontos de controle [(0,0), (1,2), (3,1), (4,0)]
  - Validação: Verificação se os pontos extremos são mantidos
  - Cálculo do erro máximo entre as curvas original e reduzida
  - Comparação visual das duas curvas

- **Teste 2**: Curva com maior curvatura [(0,0), (0,3), (4,3), (4,0)]
  - Análise do comportamento do erro em curvas mais complexas
  - Verificação da aproximação quadrática

- **Validação**: 
  - Erro máximo calculado usando distância euclidiana
  - Plotagem comparativa mostrando diferenças visuais
  - Preservação dos pontos P0 e P3 como Q0 e Q2

**Scripts utilizados**

```
bezier/de_casteljau.py
bezier/bezier_utils.py
bezier/grau_reducao.py
bezier/main_bezier.py
```

**Como executar**

```bash
cd bezier
python main_bezier.py

```

## 4 Aumento de Grau da Curva de Bézier: Exercício 2

**O que é atendido**

- Aumento de grau n → n+1

- Curva geometricamente equivalente

- Uso de De Casteljau para desenho

- Explicação conceitual no relatório (não altera a forma, apenas redistribui pontos)

**Testes utilizados**

- **Teste 1**: Curva quadrática → cúbica
  - Pontos de controle originais: [(0,0), (2,3), (4,0)]
  - Verificação da equivalência geométrica completa

- **Teste 2**: Curva linear → quadrática
  - Teste com linha reta para validar preservação da forma
  - Confirmação que a curva permanece linear

- **Teste 3**: Curva cúbica → quártica
  - Teste de múltiplos aumentos de grau consecutivos
  - Validação da estabilidade do algoritmo

- **Validação**:
  - Comparação ponto a ponto das curvas original e aumentada
  - Verificação que a distância máxima é próxima de zero
  - Plotagem sobreposta para confirmação visual

**Scripts utilizados**

- bezier/grau_aumento.py
- bezier/de_casteljau.py

**Como testar**

Importe a função em qualquer script:
```python
from grau_aumento import aumento_grau
```

## 5 Superfície de Revolução: Exercício 3

**O que é atendido**

- Curva de Bézier como geratriz

- Revolução em torno do eixo z

- Plotagem 3D da superfície

- Código modular e extensível

**Testes utilizados**

- **Teste 1**: Curva geratriz em formato de vaso
  - Pontos de controle: [(1,0), (0.5,1), (1.5,2), (0.8,3)]
  - Revolução completa (360°) com 50 divisões angulares
  - Validação da suavidade da superfície

- **Teste 2**: Perfil de garrafa
  - Curva com estreitamento no meio
  - Verificação da continuidade da malha 3D
  - Análise da distribuição de vértices

- **Teste 3**: Superfície cônica
  - Curva linear como geratriz
  - Validação da geometria resultante
  - Comparação com cone analítico

- **Validação**:
  - Verificação da conectividade da malha
  - Análise da normalização dos vetores normais
  - Contagem correta de vértices e faces
  - Visualização interativa 3D

**Script utilizado**

- `superfices/revolucao.py`

**Como executar**
```bash
cd superficies
python3 revolucao.py
```

## 6 Superficie de Varredura: Exercicio 4

**O que é atendido**

- Curva de Bézier fechada no plano xy

- Trajetória retilínea no eixo z

- Visualização da superfície de varredura

- Perfil deslocado ao longo da trajetória

**Testes utilizados**

- **Teste 1**: Perfil circular
  - Curva fechada aproximando um círculo com 8 pontos de controle
  - Trajetória linear de z=0 a z=3
  - Validação da uniformidade do "tubo" resultante

- **Teste 2**: Perfil quadrado
  - Curva fechada em formato quadrado
  - Verificação da preservação das arestas
  - Análise da continuidade nas bordas

- **Teste 3**: Perfil em estrela
  - Forma mais complexa com pontos internos e externos
  - Teste da robustez do algoritmo
  - Validação da interpolação suave

- **Validação**:
  - Verificação do fechamento correto do perfil
  - Análise da continuidade ao longo da trajetória
  - Contagem de vértices e conectividade da malha
  - Visualização 3D com wireframe

**Scripts utilizados**

`superfices/varredura.py`

**Como executar**

### 6.1 Asa de Avião: Extra

**O que é atendido**

- Superfície de varredura com redução de escala

- Simulação do perfil de uma asa

- Escala proporcional ao parâmetro da trajetória

**Testes utilizados**

- **Teste 1**: Perfil NACA simplificado
  - Curva aerodinâmica aproximada
  - Redução de escala de 100% para 20% ao longo da envergadura
  - Validação do formato característico de asa

- **Teste 2**: Asa retangular
  - Perfil constante para comparação
  - Verificação da implementação do fator de escala
  - Análise da suavidade da transição

- **Validação**:
  - Verificação da redução progressiva do perfil
  - Manutenção das proporções aerodinâmicas
  - Análise da malha resultante
  - Comparação com perfis reais de asa

**Script utilizado**

`superfices/asa_aviao.py`

## 7 Rendering com Modelo de Iluminação de Phong

**O que é atendido**

- Modelo de iluminação de Phong

- Materiais distintos

- Fonte de luz configurável

- Cena interativa

- Base para múltiplas luzes

**Testes utilizados**

- **Teste 1**: Esfera com material metálico
  - Material com alta reflexão especular (shininess = 128)
  - Luz branca posicionada em (5, 5, 5)
  - Validação dos highlights especulares
  - Verificação da componente difusa

- **Teste 2**: Múltiplos objetos com materiais diferentes
  - Esfera vermelha (material plástico)
  - Cubo azul (material fosco)
  - Cilindro verde (material brilhante)
  - Análise da interação entre objetos e sombras

- **Teste 3**: Variação da posição da luz
  - Movimento dinâmico da fonte de luz
  - Verificação da atualização em tempo real
  - Análise do comportamento das normais

- **Teste 4**: Diferentes coeficientes de material
  - Teste com ka (ambiente), kd (difuso), ks (especular)
  - Variação do expoente de brilho (shininess)
  - Comparação visual dos efeitos

- **Validação**:
  - Verificação das equações de Phong
  - Normalização correta dos vetores
  - Cálculo adequado das componentes de cor
  - Interatividade da câmera e controles
  - Performance em tempo real

**Scripts utilizados**

`rendering/phong.py`
`rendering/cena.py`

**Como executar**

```bash
cd rendering
python3 cena.py
```

**Controles da cena**:
- Mouse: Rotação da câmera
- Scroll: Zoom
- Teclas WASD: Movimento da luz
- Espaço: Reset da posição

