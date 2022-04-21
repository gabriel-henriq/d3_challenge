
# D3zer Challenge

Nesse desafio, foi solicitado um código para prever em dias a contagem de casos de covid no mundo.

Para esse desafio, escolhi trabalhar com a linguagem Python, utilizando bibliotecas como sklearn e pandas, para o processamento, treino, modelagem e predição dos dados.

Ao pesquisar uma arquitetura para conseguir o melhor proveito em prever os casos de forma global, não encontrei um model apropridado senão utilizando método de supervisão com regressão linear e equação polinomial de onze pontos em angulação.


## Architecture & Infrastructure

- #### Arquitetura


   Para uma arquitetura próxima do ideal, poderíamos utilizar o modelo SEIRD-H, proposto pelo [Boris Tseytlin](https://towardsdatascience.com/how-to-actually-forecast-covid-19-778cce27b9d6).

   Em seu modelo de forecasting, ele delimita o alogritimo por região, e utiliza cinco features, Sucetível, Exposto, Infequitado, Recuperado, Morto e por fim Dados escondidos da quarentena.

- #### Infraestrutura
  Na infraestrutura, poderíamos utilizar o serviços de demanda sob funções da [AWS](https://aws.amazon.com/lambda/) ou [GCP](https://cloud.google.com/functions), logo que a nossa aplicação apenas retorna os dados processados por uma função.

  E para o armazenamento de dados e segurança, poderíamos utilizar um serviço Bucket, também oferecido tanto pela [GCP](https://cloud.google.com/storage?utm_source=google) ou [AWS](https://aws.amazon.com/pt/s3/), para salvar os arquivos csv, logo não dependeríamos do reposítorio git utilizado para o request de dados.
## Acknowledgements

 - [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A)
 - [Boris Tseytlin](https://towardsdatascience.com/how-to-actually-forecast-covid-19-778cce27b9d6)


## Run Locally

Faça um clone do projeto

```bash
  git clone https://github.com/gabriel-henriq/d3_challenge
```

Entre na pasta do projeto

```bash
  cd d3_challenge
```

Instale a venv

```python
  python -m venv venv
```

Ative a venv

```python
  source venv/bin/activate
```

Instale as dependências

```python
  pip install -r requirements.txt
```

Run

```python
  python covidCasesForecasting/covid_forecast.py
```

