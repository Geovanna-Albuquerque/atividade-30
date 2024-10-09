def verificar_aprovacao(nota1, nota2, nota3):
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Verifica se o aluno está aprovado ou reprovado
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    
    return media, resultado

# Exemplo de uso
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media, resultado = verificar_aprovacao(nota1, nota2, nota3)
print(f"Média: {media:.2f} - Status: {resultado}")

