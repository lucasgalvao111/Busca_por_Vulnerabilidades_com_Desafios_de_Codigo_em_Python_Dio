# Primeiro desafio proposto do bootcamp Santander / Detecção de Phishing por Padrões de E-mail
# Lucas Galvão dos Santos
# 14/Dezembro/2024

# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    mensagem_lower = mensagem.lower()  # Convertendo para letras minúsculas para evitar problemas de case
    for palavra in palavras_suspeitas:
        if palavra in mensagem_lower:
            return "Phishing"
        
    return "Seguro"
        
              
email_usuario = input("Digite o corpo do e-mail: ")

email_usuario = email_usuario.strip()

resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")