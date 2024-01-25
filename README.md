# Projeto de Reconhecimento de Fala em Python

Bem-vindo ao repositório do Projeto de Reconhecimento de Fala em Python! Este projeto demonstra a criação de uma aplicação que é capaz de extrair o que foi fito em um áudio, para que possa ser tratado em posterioridade.

## Objetivo

O objetivo deste projeto é explorar a tecnologia de reconhecimento de fala, permitindo que você transcreva e reconheça áudios


## Como Usar

1. Clone ou faça o download do repositório para sua máquina local.
2. Instale as dependências necessárias com `pip install -r requirements.txt`.

3. Inicie a API com 
```
uvicorn index:app --reload
``` 

## Principais funções:

### 1. Transcrição
- **URL:** `/extract/`
- **Método**: ```POST```
- **Descrição:** Essa rota é responsável por extrair o texto do áudio passado, deve ser utiliado um caminho https:// isto é, um link da web que aponta para o áudio.
- **Body**: 
```
{
  "name": "https://path_to_audio"
}
```

## Saída da transcrição:

![image](readme/Saida_transcricao.png)

---

<p align="center">
  Feito com ❤️ por Lukas Maia
</p>

