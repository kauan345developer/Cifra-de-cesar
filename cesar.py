def cifra_de_cesar(mensagem, chave, operacao="criptografar"):
    """
    Aplica a cifra de César em uma mensagem.
    
    :param mensagem: A mensagem a ser processada.
    :param chave: O valor do deslocamento.
    :param operacao: "criptografar" ou "descriptografar".
    :return: A mensagem criptografada ou descriptografada.
    """
    if operacao == "descriptografar":
        chave = -chave
    
    resultado = ""
    for caractere in mensagem:
        if caractere.isalpha():  # Verifica se é uma letra
            base = ord('A') if caractere.isupper() else ord('a')
            # Desloca o caractere e aplica módulo 26
            novo_caractere = chr((ord(caractere) - base + chave) % 26 + base)
            resultado += novo_caractere
        else:
            # Adiciona caracteres não alfabéticos sem alteração
            resultado += caractere
    
    return resultado


# Exemplo de uso
if __name__ == "__main__":
    print("=== Cifra de César ===")
    mensagem = input("Digite a mensagem: ")
    chave = int(input("Digite o valor do deslocamento (chave): "))
    operacao = input("Escolha a operação ('criptografar' ou 'descriptografar'): ").strip().lower()
    
    if operacao not in ["criptografar", "descriptografar"]:
        print("Operação inválida! Escolha entre 'criptografar' ou 'descriptografar'.")
    else:
        resultado = cifra_de_cesar(mensagem, chave, operacao)
        print(f"Resultado ({operacao}): {resultado}")
