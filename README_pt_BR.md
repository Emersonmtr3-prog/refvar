# refvar

`refvar` é uma biblioteca leve, reativa e eficiente para gerenciamento de valores compartilhados em Python.  
Ela permite criar **variáveis reativas** que disparam callbacks sempre que seu conteúdo é alterado — inclusive quando o valor é mutável, como listas ou dicionários.

A biblioteca é ideal para situações onde várias partes do código precisam compartilhar uma mesma variável centralizada sem perder a referência original.

---

## 🚀 Recursos

- Variável reativa (`Ref`)
- Callbacks automáticos quando o valor é alterado
- Suporte a valores **imutáveis e mutáveis**
- Interceptação inteligente de métodos mutáveis (`append`, `pop`, `update`, etc.)
- Leve e eficiente (`__slots__`)
- Zero dependências externas
- API simples e intuitiva:
  - `ref(value)`
  - `ref(new_value)` ou `.set()`
  - `ref()` ou `.get()` para obter
  - `ref(..., raw=True)` para chamar diretamente a função armazenada
  - `.bind()` / `.unbind()` para callbacks

---

## ✨ Funcionalidades

- **Reatividade completa:** qualquer alteração dispara callbacks.
- **Compatível com tipos mutáveis:** diferentemente das versões anteriores.
- **Sintaxe Pythonica:** implementa operadores e métodos mágicos.
- **Chamadas diretas com `raw=True`:** execute o valor como função.
- **Leveza máxima:** projetado para performance e baixo uso de memória.

---

## 🧩 O que é o modo `raw=True`?

A chamada:

```python
ref(..., raw=True)
```

permite **executar diretamente o valor interno como uma função**, sem ativar o comportamento normal de *get/set* do `Ref`.

### Exemplos:

#### 1. Ref para função
```python
log = Ref(print)

log("Olá mundo!", raw=True)
```

Saída:

```
Olá mundo!
```

#### 2. Ref para função personalizada
```python
def somar(a, b):
    return a + b

f = Ref(somar)

print(f(10, 5, raw=True))  # 15
```

#### 3. Mantém reatividade totalmente separada
O modo `raw` **nunca dispara callbacks**, pois não altera `ref.value`, apenas chama o conteúdo.

### Quando usar `raw=True`?

- Quando você guarda uma função dentro de um `Ref`
- Quando você quer usar o `Ref` como proxy funcional
- Quando quer evitar a lógica reativa e apenas executar algo

---

## ✅ Tipos Recomendados

A classe `Ref` funciona bem com todos os tipos:

### Imutáveis:
- `str`
- `int`
- `float`
- `bool`
- `None`

### Mutáveis (totalmente suportados na versão 0.3.1):
- `list`
- `dict`
- `set`
- classes personalizadas
- objetos armazenáveis em qualquer estrutura Python

---

## 📦 Instalação

```bash
pip install refvar
```

---

## 🔧 Exemplo Básico (imutáveis)

```python
from refvar import Ref

x = Ref(10)

def ao_mudar(ref, novo_valor):
    print("Valor alterado para:", novo_valor)

x.bind(ao_mudar)

x(20)   # Atualiza e dispara callback

print(x())       # 20
print(x.get())   # 20
print(x)         # Ref(20)
```

---

## 🔧 Exemplo com Listas (mutáveis)

```python
lista = Ref([])

def ao_mudar(ref, novo_valor):
    print("Lista atualizada:", novo_valor)

lista.bind(ao_mudar)

lista.append(1)   # dispara callback
lista.append(2)   # dispara callback
lista.pop()       # dispara callback
```

Saída:

```
Lista atualizada: [1]
Lista atualizada: [1, 2]
Lista atualizada: [1]
```

---

## 🔧 Exemplo de Uso do `raw=True`

```python
from refvar import Ref

def dobro(n):
    return n * 2

f = Ref(dobro)

print(f(5, raw=True))  # 10
```

---

## 📘 Licença

MIT License.
