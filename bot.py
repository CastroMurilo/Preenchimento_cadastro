
from botcity.web import WebBot,Browser,By
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import os 
 
class PreenchedorCadastro():
    def __init__(self):
        self.bot = WebBot()
        self.bot.headless = False
        self.bot.browser = Browser.FIREFOX
        self.bot.driver_path = GeckoDriverManager().install()
        self.df = None

    def main(self):
        self.acessando_navegador('https://contabilidade-devaprender.netlify.app')
        self.colocando_password('teste@gmail.com','123')
        self.df = self.leitura_dataframe('empresas.xlsx')
        self.preencher(self.df)
        self.bot.stop_browser()

    def acessando_navegador(self,link):
        self.bot.browse(link)
        self.bot.maximize_window()

    def colocando_password(self, email, senha):
        self.bot.find_element('email',By.ID).send_keys(email)
        self.bot.find_element('senha',By.ID).send_keys(senha)
        self.bot.find_element('Entrar',By.ID).click()
        self.bot.wait(3500)
    
    def preencher(self,dataframe):
        for index, row in dataframe.iterrows():
            self.bot.find_element('nomeEmpresa',By.ID).send_keys(row['Nome da Empresa'])
            self.bot.find_element('emailEmpresa',By.ID).send_keys(row['Email'])
            self.bot.find_element('telefoneEmpresa',By.ID).send_keys(row['Telefone'])
            self.bot.find_element('enderecoEmpresa',By.ID).send_keys(row['Endereço'])
            self.bot.find_element('cnpj',By.ID).send_keys(row['CNPJ'])
            self.bot.find_element('areaAtuacao',By.ID).send_keys(row['Área de Atuação'])
            if self.bot.find_element('numeroFuncionarios',By.ID):
                self.bot.find_element('numeroFuncionarios',By.ID).click()
                self.bot.find_element('numeroFuncionarios',By.ID).send_keys(row['Quantidade de Funcionários'])
                self.bot.wait(350)
                self.bot.enter()
            self.bot.find_element('dataFundacao',By.ID).send_keys(row['Data de Fundação'])
            self.bot.find_element('Cadastrar',By.ID).click()


    def leitura_dataframe(self,dataframe):
        excel = pd.read_excel(dataframe)
        return excel

if __name__ == "__main__":
    preencher = PreenchedorCadastro()
    preencher.main()