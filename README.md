# Tradeiros Hedge Pro - Visualização de Ordens

Este projeto é uma biblioteca Python desenvolvida exclusivamente para a comunidade **[tradeiros.com.br](https://tradeiros.com.br)**. O objetivo principal é fornecer uma visualização clara e consolidada da distribuição de ordens e dos níveis de proteção de capital em BTC, seguindo a metodologia **Tradeiros Hedge Pro**.

## 🚀 Objetivo
Facilitar o acompanhamento das estratégias de proteção em múltiplos níveis, permitindo que o usuário visualize rapidamente seu patrimônio, exposição e a distribuição das ordens de compra e venda nas principais exchanges.

## 🏦 Exchanges Suportadas
Atualmente, a biblioteca suporta as seguintes plataformas:
*   **OKX** (Testes em andamento)
*   **Bitget**  (Em desenvolvimento) 
*   **Bybit** (Em breve/Implementação inicial)

## 🛡️ Segurança (Recomendações Importantes)
A segurança dos seus ativos é prioridade absoluta:
*   **API somente leitura**: É fortemente recomendado que você crie chaves de API com permissão **apenas de consulta (Read-Only)**. Nunca habilite permissões de "Saque" ou "Operação" para uso com esta biblioteca.
*   **Conexão Direta**: Toda a comunicação ocorre diretamente entre a sua máquina e os servidores das exchanges.
*   **Privacidade**: A biblioteca é open-source, roda localmente e **não armazena, transmite ou compartilha** nenhuma informação de acesso ou credenciais.

## 📥 Instalação
A biblioteca pode ser instalada facilmente via pip:

```bash
pip install tradeiros
```

## ⚙️ Configuração
Para funcionar, a biblioteca exige um arquivo `.env` no diretório raiz da execução com as suas credenciais. Utilize o modelo abaixo:

```env
# OKX
OKX_API_KEY=sua_key
OKX_API_SECRET=seu_secret
OKX_PASSPHRASE=sua_passphrase

# Bitget
BITGET_API_KEY=sua_key
BITGET_API_SECRET=seu_secret
BITGET_PASSPHRASE=sua_passphrase

# Bybit
BYBIT_API_KEY=sua_key
BYBIT_API_SECRET=seu_secret
```

## 💻 Forma de Uso
O uso foi projetado para ser o mais simples possível:

```python
from tradeiros.Tradeiros import Tradeiros

# Inicialize para a exchange desejada ("okx", "bitget" ou "bybit")
tradeiros = Tradeiros("okx")

# Recupere os dados consolidados e o patrimônio
df, patrimonio = tradeiros.atualizar()

# Exiba os resultados
print(df)
print(f"Patrimônio Total: {patrimonio:.8f}")
print(f"1% do patrimônio: {patrimonio * 0.01:.8f}")
```

## 📊 Ambiente Recomendado
Para uma experiência mais amigável e visual, recomendamos o uso do **Jupyter Notebook** através da distribuição **Anaconda**. 
O formato de tabelas do Jupyter facilita muito a leitura do DataFrame de ordens gerado pela biblioteca.

## 🛠️ Detalhes Técnicos e Funcionamento
Esta seção descreve o funcionamento interno da biblioteca para desenvolvedores e entusiastas que desejam entender como os dados são processados.

*(Espaço reservado para documentação técnica futura sobre a lógica de consolidação, agrupamento sequencial e tratamento de ordens condicionais/trigger).*


<div style="text-align: center;">
  <img src="img/Untitled (1).png" alt="Centered image">
</div>
<br>
<div style="text-align: center;">
  <img src="img/Untitled (2).png" alt="Centered image">
</div>
<br>
<div style="text-align: center;">
  <img src="img/Untitled (3).png" alt="Centered image">
</div>
<br>
<br>
<br>

---
Desenvolvido para a comunidade **Tradeiros**. 🚀
