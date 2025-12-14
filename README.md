# Trabalho Final – Computação Gráfica  
**Curvas de Bézier, Superfícies e Rendering (Phong)**

Este repositório contém a implementação completa de **todas as tarefas do PDF**, com os códigos **organizados em arquivos separados**, conforme solicitado.

---

> [!CAUTION] Usuário Linux/Ubuntu
> caso o erro a seguir aconteça:
> _OpenGL.error.Error: Attempt to retrieve context when no valid context_
> no `terminal` ou no `.bashrc` execute
> ```bash 
> export PYOPENGL_PLATFORM='glx'
> ```
> isso deve consertar o erro e permitir que a janela apareça.

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

**Scripts utilizados**

`superfices/varredura.py`

**Como executar**

### 6.1 Asa de Avião: Extra
**O que é atendido**

- Superfície de varredura com redução de escala

- Simulação do perfil de uma asa

- Escala proporcional ao parâmetro da trajetória

**Script utilizado**

`superfices/asa_aviao.py`

## 7 Rendering com Modelo de Iluminação de Phong

**O que é atendido**

- Modelo de iluminação de Phong

- Materiais distintos

- Fonte de luz configurável

- Cena interativa

- Base para múltiplas luzes

**Scripts utilizados**

`rendering/phong.py`

`rendering/cena.py`

**Como executar**

```bash
cd rendering
python3 cena.py
```

