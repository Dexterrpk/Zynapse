def generate_response(name, message, business_info):
    product = business_info.get("product", "nosso serviço")
    price = business_info.get("price", "valor sob consulta")

    return f"Olá {name}, tudo bem? Obrigado pela mensagem. Atualmente, temos {product} com preços a partir de {price}. Posso te ajudar com algo mais?"
