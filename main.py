import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='migueldono')],
    [sg.Text('Senha')],
    [sg.Input(key='migueldono12345')],
    [sg.Button('Logar')],
    [sg.Text('',key='mensagem')],
]

janela = sg.Window('Tela de login',layout=layout)

janelaloop = True
while janelaloop:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Logar':
        asenha = 'migueldono12345'
        nomedousuario = 'migueldono'
        usuario = values['migueldono']
        senha = values['migueldono12345']
        if senha == asenha and usuario == nomedousuario:
            janela['mensagem'].update('Login feito com sucesso')
        else:
            janela['mensagem'].update('Login ou senha incorreto')