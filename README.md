# ReqPlan

Sistema web simples para gerenciar requisitos de projetos de software.

## Tecnologias usadas

- Python 3 + Flask
- Bootstrap 5 (via CDN)
- Jinja2 (templates HTML)

Os dados ficam em memória enquanto o servidor está rodando. Ao encerrar o servidor, os dados são perdidos.

## Como rodar

Instale o Flask:
```
pip install flask
```

Execute:
```
python app.py
```

Acesse em `http://localhost:5000`

---

## O que dá pra fazer

- Criar, editar e excluir projetos
- Adicionar requisitos a cada projeto (título, descrição, tipo, prioridade)
- Alterar o status de um requisito (Aberto, Em desenvolvimento, Concluído)
- Filtrar requisitos por tipo, prioridade ou status
- Ver métricas do projeto: total de requisitos, quantos são funcionais, quantos foram concluídos, percentual de progresso

---

## Estrutura dos arquivos

```
ReqPlan/
├── app.py                    # classes e rotas
├── requirements.txt
├── templates/
│   ├── base.html             # layout base
│   ├── index.html            # lista de projetos
│   ├── projeto_form.html     # formulário de projeto
│   ├── projeto_detalhe.html  # detalhes e requisitos
│   └── requisito_form.html   # formulário de requisito
└── static/
    └── style.css
```

---

## Conceitos de OOP aplicados

O projeto usa duas classes com encapsulamento:

**Classe `Requisito`**
- Atributos privados: `__id`, `__titulo`, `__descricao`, `__tipo`, `__prioridade`, `__status`
- Métodos de acesso: `get_titulo()`, `set_titulo()`, etc.

**Classe `Projeto`**
- Atributos privados: `__id`, `__nome`, `__descricao`, `__data_inicio`, `__requisitos`
- `adicionar_requisito(r)` — adiciona um requisito à lista
- `remover_requisito(req_id)` — remove pelo id
- `calcular_percentual_concluido()` — retorna o percentual de requisitos com status "Concluido"
