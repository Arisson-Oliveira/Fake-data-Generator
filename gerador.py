import os
from faker import Faker
import PySimpleGUI as sg
import pyperclip

# Layout da interface gráfica do usuário
layout = [
    [sg.Button('Gerar Nome', size=(20, 0)), sg.Input(key='nome', size=(40, 0))],
    [sg.Button('Gerar Profissão', size=(20, 0)), sg.Input(key='trabalho', size=(40, 0))],
    [sg.Button('Gerar Endereço', size=(20, 0)), sg.Input(key='endereco', size=(40, 0))],
    [sg.Button('Gerar Placa', size=(20, 0)), sg.Input(key='placa', size=(40, 0))],
    [sg.Button('Gerar Cartão de Crédito', size=(20, 0)), sg.Input(key='cartao_credito', size=(40, 0))],
    [sg.Output(size=(100, 20))],
    [sg.Button('Imprimir Perfil Completo'), sg.Button('Gerar Perfil Aleatório'), sg.Button('Copiar Perfil Completo'), sg.Button('Salvar em Arquivo')]
]

# Criação da janela
janela = sg.Window('Dados falsos', layout=layout)

# Inicialização do gerador de dados falsos
fake = Faker('pt_BR')
Faker.seed(0)

# Loop principal
while True:
    event, valores = janela.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Gerar Nome':
        nome = fake.name()
        janela['nome'].update(nome)
    elif event == 'Gerar Profissão':
        trabalho = fake.job()
        janela['trabalho'].update(trabalho)
    elif event == 'Gerar Endereço':
        endereco = fake.address()
        janela['endereco'].update(endereco)
    elif event == 'Gerar Placa':
        placa = fake.license_plate()
        janela['placa'].update(placa)
    elif event == 'Gerar Cartão de Crédito':
        cartao_credito = fake.credit_card_full()
        janela['cartao_credito'].update(cartao_credito)
    elif event in ('Imprimir Perfil Completo', 'Copiar Perfil Completo', 'Salvar em Arquivo'):
        perfil_completo = (
            f'NOME: {valores["nome"]}{os.linesep}'
            f'PROFISSÃO: {valores["trabalho"]}{os.linesep}'
            f'ENDEREÇO: {valores["endereco"]}{os.linesep}'
            f'PLACA: {valores["placa"]}{os.linesep}'
            f'CARTÃO DE CRÉDITO: {valores["cartao_credito"]}{os.linesep}'
        )
        
        if event == 'Imprimir Perfil Completo':
            print(perfil_completo)
        elif event == 'Copiar Perfil Completo':
            pyperclip.copy(perfil_completo)
            sg.popup('Perfil completo copiado para a área de transferência!')
        elif event == 'Salvar em Arquivo':
            with open('dados_de_teste.txt', 'a', encoding='utf-8', newline='') as arquivo:
                arquivo.write(perfil_completo)
            sg.popup('Perfil completo salvo em dados_de_teste.txt')
    elif event == 'Gerar Perfil Aleatório':
        # Gerar dados aleatórios
        nome = fake.name()
        trabalho = fake.job()
        endereco = fake.address()
        placa = fake.license_plate()
        cartao_credito = fake.credit_card_full()

        # Atualizar os campos de entrada com os dados gerados
        janela['nome'].update(nome)
        janela['trabalho'].update(trabalho)
        janela['endereco'].update(endereco)
        janela['placa'].update(placa)
        janela['cartao_credito'].update(cartao_credito)
        
        # Imprimir perfil aleatório
        perfil_aleatorio = (
            f'NOME: {nome}{os.linesep}'
            f'PROFISSÃO: {trabalho}{os.linesep}'
            f'ENDEREÇO: {endereco}{os.linesep}'
            f'PLACA: {placa}{os.linesep}'
            f'CARTÃO DE CRÉDITO: {cartao_credito}{os.linesep}'
        )
        
        print(perfil_aleatorio)

# Fechamento da janela
janela.close()
