# Projeto: Conversor de Moedas

Este projeto é um script em Python que utiliza a biblioteca **CustomTkinter** para criar uma interface gráfica de usuário (GUI) e consome dados de uma API para realizar conversões entre diferentes moedas.

## Funcionalidades

- Converte valores de uma moeda para outra utilizando uma API de taxas de câmbio em tempo real.
- Interface amigável para o usuário, construída com **CustomTkinter**.
- Exibe o valor convertido com base nas taxas de câmbio mais recentes.

## Tecnologias Usadas

🔹 **Python**  
🔹 **CustomTkinter** para a GUI

## API Utilizada

A API utilizada para obter as taxas de câmbio é a [AwesomeAPI](https://docs.awesomeapi.com.br/), que fornece dados atualizados sobre diversas moedas.

#### URL da API:
```bash
https://economia.awesomeapi.com.br/json/last/<moedas>
