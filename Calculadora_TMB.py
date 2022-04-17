# Projeto - Calculadora TMB
# Desafio - Crie uma Calculadora que determine a Taxa Metabólica Basal do Usuário (TMB)

import PySimpleGUI as sg

sg.theme('TanBlue')

#layout
layout = [
    [sg.Text("Sexo:", size=(10,0)),sg.Radio("M", "RADIO1",key="masculino"),sg.Radio("F","RADIO1",key="feminino")],

    [sg.Text("Biotipo:",size=(10,0)), sg.Radio("Ectomorfo","RADIO2",key="ecto"),sg.Radio("Mesomorfo","RADIO2",key="meso"), sg.Radio("Endomorfo","RADIO2",key="endo")],

    [sg.Text("Altura(cm):",size=(10,0)), sg.InputText(size=(6,0), key="altura")],

    [sg.Text("Peso(Kg):",size=(10,0)), sg.InputText(size=(6,0), key="peso")],

    [sg.Text("Idade:", size=(10,0)), sg.InputText(size=(6,0),key="idade")],

    [sg.Button("Calcular TMB", size=(10,0)), sg.Exit()],

    [sg.Text("Sua TMB:", size=(10,0)) ,sg.Output(size=(100,0))]
]
#janela
janela = sg.Window("Taxa metabólica basal",layout)

#extrair os dados da tela
while True:
    event, values = janela.Read() 

    if event == sg.WIN_CLOSED or event == "Exit": # if user closes window or clicks cancel
        break

    elif event == "Calcular TMB":
        masculino = values['masculino']
        feminino = values['feminino']  
        ecto = values['ecto'] 
        meso = values['meso']
        endo = values['endo']   
        altura = int(values['altura'])
        peso = float(values['peso'])
        idade = int(values['idade'])

        if(masculino == True):    
            tmb = 66 + 13.7*peso + 5*altura - 6.8*idade   

        elif(feminino == True): 
            tmb = 665 + 9.6*peso + 1.8*altura - 4.7*idade

        print(f"{tmb:.2f} Kcal")

janela.close()