from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# classes do sistema

class Requisito:
    def __init__(self, id, titulo, descricao, tipo, prioridade, status="Aberto"):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__tipo = tipo
        self.__prioridade = prioridade
        self.__status = status

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__tipo

    def get_prioridade(self):
        return self.__prioridade

    def get_status(self):
        return self.__status

    def set_titulo(self, v):
        self.__titulo = v

    def set_descricao(self, v):
        self.__descricao = v

    def set_tipo(self, v):
        self.__tipo = v

    def set_prioridade(self, v):
        self.__prioridade = v

    def set_status(self, v):
        self.__status = v


class Projeto:
    def __init__(self, id, nome, descricao="", data_inicio=""):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__data_inicio = data_inicio
        self.__requisitos = []

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_data_inicio(self):
        return self.__data_inicio

    def get_requisitos(self):
        return self.__requisitos

    def set_nome(self, v):
        self.__nome = v

    def set_descricao(self, v):
        self.__descricao = v

    def set_data_inicio(self, v):
        self.__data_inicio = v

    def adicionar_requisito(self, r):
        self.__requisitos.append(r)

    def remover_requisito(self, req_id):
        self.__requisitos = [r for r in self.__requisitos if r.get_id() != req_id]

    def calcular_percentual_concluido(self):
        total = len(self.__requisitos)
        if total == 0:
            return 0
        concluidos = sum(1 for r in self.__requisitos if r.get_status() == "Concluido")
        percentual = round(concluidos / total * 100, 1)
        return percentual


# armazenamento em memoria (dicionario)
projetos = {}
next_projeto_id = 1
next_requisito_id = 1


# rotas

@app.route("/")
def index():
    lista = list(projetos.values())
    return render_template("index.html", projetos=lista)


@app.route("/projeto/novo", methods=["GET", "POST"])
@app.route("/projeto/<int:id>/editar", methods=["GET", "POST"])
def projeto_form(id=None):
    global next_projeto_id
    p = projetos.get(id)
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form.get("descricao", "")
        data_inicio = request.form.get("data_inicio", "")
        if p:
            p.set_nome(nome)
            p.set_descricao(descricao)
            p.set_data_inicio(data_inicio)
            return redirect(url_for("projeto_detalhe", id=p.get_id()))
        novo = Projeto(next_projeto_id, nome, descricao, data_inicio)
        projetos[next_projeto_id] = novo
        next_projeto_id += 1
        return redirect(url_for("index"))
    return render_template("projeto_form.html", projeto=p)


@app.route("/projeto/<int:id>/excluir", methods=["POST"])
def projeto_excluir(id):
    projetos.pop(id, None)
    return redirect(url_for("index"))


@app.route("/projeto/<int:id>")
def projeto_detalhe(id):
    p = projetos.get(id)
    if not p:
        return redirect(url_for("index"))

    tipo = request.args.get("tipo", "")
    prioridade = request.args.get("prioridade", "")
    status = request.args.get("status", "")

    reqs = p.get_requisitos()
    total = len(reqs)
    funcionais = sum(1 for r in reqs if r.get_tipo() == "Funcional")
    nao_funcionais = sum(1 for r in reqs if r.get_tipo() == "Nao Funcional")
    concluidos = sum(1 for r in reqs if r.get_status() == "Concluido")
    pct = p.calcular_percentual_concluido()

    if tipo:
        reqs = [r for r in reqs if r.get_tipo() == tipo]
    if prioridade:
        reqs = [r for r in reqs if r.get_prioridade() == prioridade]
    if status:
        reqs = [r for r in reqs if r.get_status() == status]

    filtros = {"tipo": tipo, "prioridade": prioridade, "status": status}

    return render_template(
        "projeto_detalhe.html",
        projeto=p,
        requisitos=reqs,
        total=total,
        funcionais=funcionais,
        nao_funcionais=nao_funcionais,
        concluidos=concluidos,
        pct=pct,
        filtros=filtros
    )


@app.route("/projeto/<int:proj_id>/requisito/novo", methods=["GET", "POST"])
@app.route("/projeto/<int:proj_id>/requisito/<int:req_id>/editar", methods=["GET", "POST"])
def requisito_form(proj_id, req_id=None):
    global next_requisito_id
    p = projetos.get(proj_id)
    if not p:
        return redirect(url_for("index"))

    r = None
    if req_id:
        for x in p.get_requisitos():
            if x.get_id() == req_id:
                r = x
                break

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form.get("descricao", "")
        tipo = request.form["tipo"]
        prioridade = request.form["prioridade"]
        if r:
            r.set_titulo(titulo)
            r.set_descricao(descricao)
            r.set_tipo(tipo)
            r.set_prioridade(prioridade)
            r.set_status(request.form["status"])
        else:
            novo_req = Requisito(next_requisito_id, titulo, descricao, tipo, prioridade)
            p.adicionar_requisito(novo_req)
            next_requisito_id += 1
        return redirect(url_for("projeto_detalhe", id=proj_id))

    return render_template("requisito_form.html", projeto=p, requisito=r)


@app.route("/projeto/<int:proj_id>/requisito/<int:req_id>/excluir", methods=["POST"])
def requisito_excluir(proj_id, req_id):
    p = projetos.get(proj_id)
    if p:
        p.remover_requisito(req_id)
    return redirect(url_for("projeto_detalhe", id=proj_id))


if __name__ == "__main__":
    app.run(debug=True)
