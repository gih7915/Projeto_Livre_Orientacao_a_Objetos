import csv

class ExportavelMixin:
    def exportar_para_csv(self, caminho, dados):
        with open(caminho, mode='w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)
