# ReqPlan – Sistema de Gerenciamento de Requisitos

Aplicação web para cadastro, organização e acompanhamento de requisitos de software.

## Tecnologias

- **Python 3** — linguagem principal
- **Flask** — microframework web
- **Bootstrap 5** — estilização via CDN
- **HTML + Jinja2** — templates

> Os dados são armazenados em memória (dicionário Python). Ao reiniciar o servidor, os dados são apagados — sem banco de dados necessário.

## Como executar

### 1. Instale a dependência
```
pip install flask
```

### 2. Execute a aplicação
```
python app.py
```

### 3. Acesse no navegador
```
http://localhost:5000
```

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Cadastro de projetos | Nome, descrição e data de início |
| Cadastro de requisitos | Título, descrição, tipo, prioridade |
| Tipos | Funcional / Não Funcional |
| Prioridades | Alta / Média / Baixa |
| Status | Aberto / Em desenvolvimento / Concluído |
| Filtros | Por tipo, prioridade e status |
| Métricas | Total, funcionais, não funcionais, concluídos, % progresso |
| Barra de progresso | Percentual de requisitos concluídos |

---

## Estrutura do Projeto

```
ReqPlan/
├── app.py                   # Modelos OOP + rotas Flask
├── requirements.txt         # Dependências Python
├── templates/
│   ├── base.html            # Layout base (navbar + Bootstrap)
│   ├── index.html           # Lista de projetos
│   ├── projeto_form.html    # Formulário criar/editar projeto
│   ├── projeto_detalhe.html # Detalhes, métricas e lista de requisitos
│   └── requisito_form.html  # Formulário criar/editar requisito
└── static/
    └── style.css            # Estilos personalizados
```

---

## Conceitos de OOP aplicados

- **Encapsulamento** — atributos privados com prefixo `__` (name mangling do Python)
- **Getters e setters** — métodos `get_x()` / `set_x()` para acesso controlado
- **Classe `Requisito`** — encapsula id, título, descrição, tipo, prioridade e status
- **Classe `Projeto`** — encapsula lista de requisitos e expõe métodos de manipulação
- **`adicionar_requisito(r)`** — adiciona um requisito ao projeto
- **`remover_requisito(req_id)`** — remove um requisito pelo id
- **`calcular_percentual_concluido()`** — calcula o percentual de requisitos com status "Concluido"
