import sqlite3
from prettytable import PrettyTable
def registro(cnn, cursor):
    insere = "INSERT INTO tb_prod(nme_prod, vlr_prod, qtd_prod) VAlUES (?, ?, ?)"

    opcao = input("Deseja Registar algum produto S/N?")
    opcao = opcao.upper()
    while opcao != 'N':
        print(">>>Incluir produto: ")
        nome = input("Nome do produto: ")
        valor = float(input("Valor do produto: "))
        quant = int(input("Quantidade do produto: "))
        print()
        cursor.execute(insere, [nome, valor, quant])
        cnn.commit()
        print("->Produto registrado com sucesso!")
        opcao = input("Registrar outro produto S/N?\n")
        opcao = opcao.upper()

def consulta(cnn, cursor):
    consulta = "SELECT * FROM tb_prod WHERE nme_prod LIKE '%' || ? || '%'"

    opcao = input("Deseja consultar algum produto S/N?")
    opcao = opcao.upper()
    while opcao != 'N':
        print(">>>Consultar produto: ")
        nome = input("Nome do produto: ")
        print()
        cursor.execute(consulta, [nome])

        tab = PrettyTable(['ID', 'NOME', 'VALOR', 'ESTOQUE'])
        for (ident, nome, valor, qnt) in cursor.fetchall():
            tab.add_row([ident, nome, valor, qnt])
        print(f"Produto: {nome}")
        print(tab)
        opcao = input("Consultar outro produto S/N?\n")
        opcao = opcao.upper()

def update(cnn, cursor):
    updt_consulta = "SELECT * FROM tb_prod WHERE idt_prod = ?"
    updt = "UPDATE tb_prod SET nme_prod=?, vlr_prod=?, qtd_prod=? WHERE idt_prod=?"

    opcao = input("Deseja alterar algum produto S/N?")
    opcao = opcao.upper()
    while opcao != 'N':
        print(">>>Alterar produto: ")
        ident = int(input("Identificador(ID) do produto: "))

        cursor.execute(updt_consulta, [ident])
        dados = cursor.fetchone()
        if dados is None:
            print("ID não encontrado!\n")
            continue

        print("Dados atuais: ", dados)
        print()
        print("Novos dados:")
        nome = input("Nome do produto: ")
        valor = float(input("Valor do produto: "))
        quant = int(input("Quantidade do produto: "))
        print()
        cursor.execute(updt, [nome, valor, quant, ident])
        cnn.commit()
        print("->Produto alterado com sucesso!")
        opcao = input("Atualizar outro produto S/N?\n")
        opcao = opcao.upper()

def remover(cnn, cursor):
    delete_consulta = "SELECT * FROM tb_prod WHERE idt_prod = ?"
    delete = "DELETE FROM tb_prod WHERE idt_prod=?"

    opcao = input("Deseja excluir algum produto S/N?")
    opcao = opcao.upper()
    while opcao != 'N':
        print(">>>Alterar produto: ")
        ident = int(input("Identificador(ID) do produto: "))

        cursor.execute(delete_consulta, [ident])
        dados = cursor.fetchone()
        if dados is None:
            print("ID não encontrado!\n")
            continue

        print("Dados atuais: ", dados)
        print()

        conf = input("Confirmar operação S/N: ")
        conf = conf.upper()
        if conf == 'S':
            cursor.execute(delete, [ident])
            cnn.commit()
            print("->Produto removido")
            print()
        opcao = input("Remover outro produto S/N?\n")
        opcao = opcao.upper()

def main():
    cnn = sqlite3.connect("estoque.db")
    cursor = cnn.cursor()

    print("   |--------------------|")
    print("   | Dados dos Produtos |")
    print("   |--------------------|")
    print()

    opcao = 0
    while opcao != 5:
        print("****** MENU DE OPÇÕES ******")
        print("|--------------------------|")
        print("|   1- Adicionar Produto   |")
        print("|   2- Consultar Produto   |")
        print("|   3- Alterar Produto     |")
        print("|   4- Remover Produto     |")
        print("|   5- Sair                |")
        print("|--------------------------|")
        opcao = int(input("Insira o numero da operação desejada: "))
        print()
        if opcao == 1:
            # Registra de produtos
            registro(cnn, cursor)
        elif opcao == 2:
            # Consulta de produtos
            consulta(cnn, cursor)
        elif opcao == 3:
            # Alteração de produtos
            update(cnn, cursor)
        elif opcao == 4:
            # Remove produto
            remover(cnn, cursor)
        else:
            print("Programa Encerrado")
            opcao = 5

    cursor.close()
    cnn.close()

if __name__ == "__main__":
   main()
