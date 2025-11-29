# refvar

`refvar` é uma biblioteca leve e reativa para gerenciamento de referências em Python. Ela permite criar referências mutáveis para tipos imutáveis (como `str`, `int`, `bool`) que podem ser compartilhadas entre múltiplos módulos e atualizadas centralmente.

O objetivo principal é resolver o problema onde a importação de variáveis simples em diferentes arquivos perde o vínculo com o valor original. Além disso, a biblioteca suporta **callbacks**, permitindo executar funções automaticamente sempre que o valor é alterado.

---

## 🚀 Recursos

- Variável reativa (`Ref`)
- Callbacks disparados automaticamente quando o valor muda
- Extremamente leve (< 50 linhas)
- Zero dependências
- API simples e intuitiva:
  - `ref(value)`
  - `ref(new_value)` `.set()` para atualizar
  - `ref()` `.get()` para pegar o conteúdo 
  - `.bind()` `.unbind()` para chamar uma funcao
- Seguro por design — suporta **apenas tipos simples**

---

## ✨ Funcionalidades

- **Fonte Única da Verdade:** Passe variáveis entre módulos sem perder a referência.
- **Reatividade:** "Binde" (vincule) callbacks que disparam ao atualizar o valor.
- **Sintaxe Pythonica:** Implementa métodos mágicos (`__call__`, `__eq__`, `__bool__`, `__str__`) para uso intuitivo.
- **Leve:** Utiliza `__slots__` para alta eficiência de memória.

---

## ✅ Tipos Recomendados

`Ref` é recomendado a **valores simples e imutáveis**:

- `str`
- `int`
- `float`
- `bool`
- `None`

Isso evita comportamentos inesperados com objetos mutáveis.

## ⚠️ Não recomendado para:

- `list`
- `dict`
- `set`
- classes personalizadas
- funções
- qualquer coisa mutável

Se você precisa de programação reativa completa, use um framework —  
`refvar` foi projetado especificamente para ser leve e simples.

---

## 📦 Instalação

```bash
pip install refvar
```

---

## 🔧 Exemplo de Uso

### Exemplo Básico

```python
from refvar import Ref

x = Ref(10)

def ao_mudar(ref, novo_valor):
    print("Valor alterado para:", novo_valor)

x.bind(ao_mudar)

x(20)   # Atualiza o valor e dispara o callback

value = x()
print(value, type(value))  # 20 <class 'int'>

value = x.get()
print(value, type(value))  # 20 <class 'int'>

value = x
print(value, type(value))  # 20 <class 'ref.core.Ref'>
