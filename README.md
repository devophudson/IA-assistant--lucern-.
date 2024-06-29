# Assistente de Voz em Python

## Descrição
Este projeto é um assistente de voz desenvolvido em Python, utilizando bibliotecas como `pyttsx3`, `speech_recognition`, e `keyboard` para reconhecer comandos de voz e executar ações como abrir o prompt de comando, abrir a câmera, ou iniciar o navegador Google Chrome.

## Sumário
1. [Introdução](#introdução)
2. [Instalação](#instalação)
3. [Uso](#uso)
4. [Contribuição](#contribuição)
5. [Licença](#licença)
6. [Contato](#contato)

## Introdução
Este projeto tem como objetivo criar um assistente de voz capaz de responder a comandos e executar tarefas no seu computador. Ele pode reconhecer comandos de voz em português do Brasil e responder de forma apropriada.

## Instalação
Para instalar e configurar este projeto, siga os passos abaixo:

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    ```
2. Entre no diretório do projeto:
    ```bash
    cd seu-projeto
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
Para usar o assistente de voz, siga os passos abaixo:

1. Defina as variáveis de ambiente `USER` e `BOT` no arquivo `.env`:
    ```env
    USER=SeuNome
    BOT=NomeDoBot
    ```
2. Execute o script principal:
    ```bash
    python main.py
    ```

3. Use as teclas de atalho para iniciar e parar a escuta do assistente:
    - `Ctrl + Shift + K`: Começar a ouvir
    - `Ctrl + Shift + P`: Parar de ouvir

## Contribuição
Se você quiser contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch:
    ```bash
    git checkout -b feature/nova-feature
    ```
3. Faça suas alterações e commite:
    ```bash
    git commit -m 'Adiciona nova feature'
    ```
4. Envie para o branch:
    ```bash
    git push origin feature/nova-feature
    ```
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
Para perguntas ou suporte, entre em contato:

- **Nome:** Seu Nome
- **Email:** hudsonfrancisco66@gmail.com
- **LinkedIn:** www.linkedin.com/in/hudson-martins-4151a115b
