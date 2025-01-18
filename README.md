                                                                                                                                 
                                                                                                                                 
                                                            ░▓▓▒░                                                                
                                                           █████████░                                                            
                                                          ▓█▓     ▒████▓░                                                        
                                                          ██▒         ▓███▓                                                      
                                 ░▓▓▒░                    ██▒         ░▓█████▒      ▓███████▒                                    
                                ▓██▓█████▒                ██▒    ▒▓█████▓░ ░██▒   ▒██▓░░░░░██▓                                   
                                ▓█▓    ░▓████▓░           █████████▒░       ▓█▓   ▓█▓      ▓█▓                                   
                                ▒██        ░▓████▓░         ▒░              ▓█▓   ██▒                                            
                                 ████████░      ▒████▓           ░▒▓██████▓░▓█▓  ░██░  ▒███▓▒                                    
                                 ▓██               ░▓████▒░▒▓███████▓▒░ ░▓█████░ ▒██      ▒█████▓░                               
                                 ░██▒                  ░▓███▓▒░             ░▓██████░         ░▓████▒                            
                                  ▒██░                                           ▒█████▒          ░██░                           
                                   ▓████████████▓                                   ▒█████         ██░                           
                                  ▒██▒                                           ░▓████▓▒         ░██░                           
                                  ██▒                  ░▓██▓▒░               ▒▓█████░          ▒▓███▓                            
                                 ▓██                ▒████▓▓▓███████▓▒░   ▒█████▒ ▒██      ░▓█████▒░                              
                                 ████████░      ▒▓███▓░          ▒▓███████▓▒▓█▓  ░██░  ▒████▒░                                   
                                ▒██░        ░▓████▒                         ▓█▓   ██▒   ▒░                                       
                                ▓█▓     ▒█████▒           ▓███████▓▒        ▓█▓   ▓█▓      ▓█▓                                   
                                ▓██▒█████▓▒               ██▒   ▒▓█████▓▒  ░██▒   ▒██▒     ▓█▓                                   
                                 ▒██▓▒                    ██▒         ▒██████▓     ░████████▓                                    
                                                          ██▒         ▒████▒                                                     
                                                          ▓█▓     ░▓████░                                                        
                                                           ██▓▓█████▓░                                                           
                                                            ▒▓▓▓░                                                                
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
                       ▒█▓  ██  ██░    ▓█▒    ▒██████▒    ██████    ▓██████     ▓█████░       ██▒    ▓██████▒                    
                        ██ ▒██▒ ██    ░███       ██       █▓        ▓█░  ▒█▒   ░█▓   ██      ▒███       ██                       
                        ▓█ ▓██▓▒█▓    ▓███▒      ██       █▓        ▓█░  ▓█▒   ▒█▓   ▒▒      ████░      ██                       
                        ▒█▓██████▒    ██░██      ██       █████▒    ▓██████    ▒█▓          ░█▓▒█▓      ██                       
                        ░███▒▓███    ▒██▓██░     ██       ██        ▓█▒ ▒██░   ▒█▓          ▓█▓▓██     ░██                       
                         ▓██ ░██▓    ▓█▒▒▓█▓     ██       █▓        ▓█░  ▓█▒   ░█▓   ██    ░██▒▒▓█▒     ██                       
                         ▒█▓  ██▒   ░█▓   ██░    ██       ██▒░░░    ▓█░  ▓█▒    ██▒░▓█▓    ▒█▒   ██     ██                       
                         ░█▒  ▒▓    ▒█░   ▒█░    ▓▓       ██▓▓█▓    ▒█   ▒█░     ▒▓▓▓░     ▓▓    ▒█     ▓▓                       
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 




Windows:

Verificar se o Python está instalado:

    python --version

Instalar o pip (se necessário):

    python -m ensurepip --upgrade

Instalar o Selenium:

    pip install selenium

Linux (Debian/Ubuntu):

Instalar o Python:

    sudo apt update
    sudo apt install python3

Instalar o pip:

    sudo apt install python3-pip

Instalar o Selenium:

    pip3 install selenium

Firefox (GeckoDriver):

O Watercat usa o GeckoDriver para controlar o navegador Firefox.
Como instalar o GeckoDriver:

Baixar o GeckoDriver: Acesse https://github.com/mozilla/geckodriver/releases e baixe a versão do GeckoDriver compatível com o seu sistema operacional.

Adicionar o GeckoDriver ao PATH: Para Windows, mova o geckodriver.exe para um diretório e adicione esse diretório ao PATH ou forneça o caminho absoluto no código:

    from selenium import webdriver

    driver = webdriver.Firefox(executable_path='C:/geckodriver/geckodriver.exe')

Para Linux ou macOS, mova o geckodriver para um diretório como /usr/local/bin:

    sudo mv geckodriver /usr/local/bin/
