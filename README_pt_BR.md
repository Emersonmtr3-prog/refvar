# refvar

Um sistema de variável reativa para Python, leve e sem dependências.  
`refvar` permite armazenar valores simples e executar callbacks automaticamente sempre que o valor é alterado.

Ideal para pequenas aplicações, controle de estado ou padrões reativos simples — sem precisar de frameworks.

---

## 🚀 Recursos

- Variável reativa (`Ref`)
- Callbacks disparados automaticamente quando o valor muda
- Extremamente leve (< 50 linhas)
- Zero dependências
- API simples e intuitiva:
  - `ref(value)`
  - `ref(new_value)` para atualizar
  - `.get()`, `.set()`, `.bind()`, `.unbind()`
- Seguro por design — suporta **apenas tipos simples**

---

## ⚠ Tipos Suportados

`Ref` é intencionalmente limitado a **valores simples e imutáveis**:

- `str`
- `int`
- `float`
- `bool`
- `None`

Isso evita comportamentos inesperados com objetos mutáveis.

### ❌ Não recomendado para:

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
print(x.value)  # 20
