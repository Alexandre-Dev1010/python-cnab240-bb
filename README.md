Python Cnab

Script para gerar o arquivo CNAB240 de remessa:

from datetime import datetime
from decimal import Decimal
from cnab240.tipos import Arquivo
from cnab240 import registro

# Carrega os registros CNAB240 do Banco do Brasil
reg = registro.Registros('cnab240/bancos/banco_brasil/specs')

codigo_cobranca_cedente="0014"  
numero_carteira="18"
variacao_carteira="019" 
        

dados_cedente = dict(
    codigo_banco=1,
    cedente_inscricao_tipo=2,
    cedente_inscricao_numero=15800500000185,
    codigo_convenio_banco = "001234567" + codigo_cobranca_cedente + numero_carteira + variacao_carteira, 
    cedente_agencia=7612,
    cedente_agencia_dv="0",                
    cedente_conta=10350,
    cedente_conta_dv="0",
    dv_agencia_conta="0",
    cedente_nome="EMPRESA EXEMPLO LTDA",
    nome_do_banco="BANCO DO BRASIL SA",
    arquivo_sequencia=1,
    arquivo_densidade=0,   
)

# Criação do objeto Arquivo
arquivo = Arquivo(banco=type('banco', (), {'registros': reg}))
arquivo.header.fromdict(dados_cedente)

# Header do lote
header_lote = dados_cedente.copy()
header_lote.update(dict(
    controlecob_data_gravacao=int(datetime(2024, 10, 25).strftime('%d%m%Y')),
    
))


# Dados do boleto
boleto = dict(
    cedente_agencia=7612,
    cedente_agencia_dv="0",
    cedente_conta=10350,
    cedente_conta_dv="0",
    nosso_numero="0000000123",                  # 10 dígitos
    numero_documento="0001",
    vencimento_titulo=int(datetime(2024, 11, 10).strftime('%d%m%Y')),
    valor_titulo=Decimal("150.00"),
    especie_titulo=1,
    aceite_titulo="N",
    data_emissao_titulo=int(datetime(2024, 10, 25).strftime('%d%m%Y')),
    juros_cod_mora=3,                          # isento
    juros_mora_taxa=Decimal("0.00"),
    valor_iof=0,
    valor_abatimento=Decimal("0.00"),
    identificacao_titulo="BOLETO TESTE BB",
    codigo_protesto=3,
    prazo_protesto=0,
    codigo_baixa=1,
    prazo_baixa="000", 

    sacado_inscricao_tipo=2,
    sacado_inscricao_numero=15800500000185,
    sacado_nome="CLIENTE TESTE LTDA",
    sacado_endereco="Rua Exemplo, 123",
    sacado_bairro="Centro",
    sacado_cep=44000,
    sacado_cep_sufixo=0,
    sacado_cidade="Feira de Santana",
    sacado_uf="BA",

    sacador_inscricao_tipo=2,
    sacador_inscricao_numero=15800500000185,
    sacador_nome="EMPRESA EXEMPLO LTDA"
)


arquivo.incluir_cobranca(header=header_lote, **boleto)



with open("remessa_bb.rem", "wb") as f:
    conteudo = str(arquivo)
    linhas = conteudo.splitlines()
    for linha in linhas:
        linha_corrigida = linha.ljust(240)[:240]  
        f.write((linha_corrigida + "\r\n").encode("ascii"))




print("Arquivo CNAB240 gerado com sucesso: remessa_bb.rem")



Mantido por Trustcode
