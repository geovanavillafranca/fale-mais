from tkinter import *
from tkinter import ttk


class Tela:

    def __init__(self):

        self.root = Tk()
        self.root.geometry("750x400")
        self.root.title("TELZIR")
        self.style = ttk.Style()

        # Label do erro dos minutos
        self.tempo_vazio = Label(self.root)

        #Label titulo
        self.label_titulo = Label(self.root)
        self.label_titulo.configure(text="Verifique sua ligação com e sem desconto", font=("Arial", 15, 'bold'))
        self.label_titulo.place(x=170, y=30)

        # Label origem
        self.label_origem = Label(self.root)
        self.label_origem.configure(text="Escolha a Origem", font=("Arial", 12, 'bold'))
        self.label_origem.place(x=99, y=105)
        # Escolha a origem
        self.combo_origem = ttk.Combobox(values=["011", "016", "017", "018"])
        self.combo_origem.current(0)
        self.combo_origem.place(x=100, y=140)

        # Label destino
        self.label_origem = Label(self.root)
        self.label_origem.configure(text="Escolha o Destino", font=("Arial", 12, 'bold'))
        self.label_origem.place(x=299, y=105)
        # Escolha o destino
        self.combo_destino = ttk.Combobox(values=["011", "016", "017", "018"])
        self.combo_destino.current(2)
        self.combo_destino.place(x=300, y=140)

        # Label Plano
        self.label_plano = Label(self.root)
        self.label_plano.configure(text="Escolha um Plano", font=("Arial", 12, 'bold'))
        self.label_plano.place(x=499, y=105)
        # Escolha o plano
        self.combo_plano = ttk.Combobox(values=["Fale Mais 30", "Fale Mais 60", "Fale Mais 120"])
        self.combo_plano.current(0)
        self.combo_plano.place(x=500, y=140)


        # Label do tempo
        self.label_tempo = Label(self.root)
        self.label_tempo.configure(text="Escolha os minutos", font=("Arial", 12, 'bold'))
        self.label_tempo.place(x=179, y=200)
        # Entry do Tempo
        self.entry_tempo = Entry(self.root)
        self.entry_tempo.configure()
        self.entry_tempo.place(x=180, y=240, width=155, height=20)

        # Botao
        self.btn = Button(self.root, text="CALCULAR", font=("Arial", 10, 'bold'), bg="red", fg="white", width=10,
                          height=0, command=self.gerar_tabela)
        self.btn.place(x=470, y=232)

        self.root.mainloop()

    def calculando_valores(self):

        origem = self.combo_origem.get()

        destino = self.combo_destino.get()

        plano = self.combo_plano.get()

        tempo = int(self.entry_tempo.get())

        if origem == "011":
            if destino == "011":
                if plano:
                    com_fale_mais = 0
                    sem_fale_mais = 0
                    return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "016":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.09
                        sem_fale_mais = tempo * 1.9
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.09
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        print(com_fale_mais)
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    print("plano 120")
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.09
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "017":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 1.87
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 1.87
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 1.87
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


            elif destino == "018":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 0.99
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 0.99
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 0.99
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 0.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

        elif origem == "016":
            if destino == "016":
                if plano:
                    com_fale_mais = 0
                    sem_fale_mais = 0
                    return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "011":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 3.19
                        sem_fale_mais = tempo * 2.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 3.19
                        sem_fale_mais = tempo * 2.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 3.19
                        sem_fale_mais = tempo * 2.9
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "017":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 3.08
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 3.08
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 3.08
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "018":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

        elif origem == "017":
            if destino == "017":
                if plano:
                    com_fale_mais = 0
                    sem_fale_mais = 0
                    return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "011":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.97
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.97
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":

                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.97
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.70
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


            elif destino == "016":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                elif plano == "Fale Mais 60":
                    print("plano 60")
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "018":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 1.98
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 1.98
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 1.98
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.80
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

        elif origem == "018":
            if destino == "018":
                if plano:
                    com_fale_mais = 0
                    sem_fale_mais = 0
                    return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo
            elif destino == "011":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.09
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.09
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.09
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 1.90
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "016":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.64
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.40
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

            elif destino == "017":
                if plano == "Fale Mais 30":
                    if tempo > 30:
                        com_fale_mais = (tempo - 30) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 60":
                    if tempo > 60:
                        com_fale_mais = (tempo - 60) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                elif plano == "Fale Mais 120":
                    if tempo > 120:
                        com_fale_mais = (tempo - 120) * 2.53
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo

                    else:
                        com_fale_mais = 0
                        sem_fale_mais = tempo * 2.30
                        return com_fale_mais, sem_fale_mais, origem, destino, plano, tempo


            self.gerar_tabela()

    def gerar_tabela(self):

        if self.entry_tempo.get() == "":

            self.tempo_vazio.config(text="Digite um valor", fg="red")
            self.tempo_vazio.place(x=210, y=260)

        else:

            self.tempo_vazio.place_forget()

            # Recebendo os valores do plano
            valores = [self.calculando_valores()]

            # Tela do root sendo reajustada
            self.root.geometry("750x400")

            # Tela do Frame
            self.frame_principal = Frame(master=self.root, width=600, height=100, borderwidth=4, relief="groove")
            self.frame_principal.place(x=39, y=300)

            lista = [('Origem', 'Destino', 'Tempo','Plano FaleMais','Com FaleMais', 'Sem FaleMais'),
                     (valores[0][2], valores[0][3], valores[0][5], valores[0][4], format(valores[0][0], ".2f"),
                      format(valores[0][1], ".2f"))]

            total_rows = len(lista)
            total_columns = len(lista[0])
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(self.frame_principal, width=15, font=('Arial', 10, 'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lista[i][j])


Tela()
