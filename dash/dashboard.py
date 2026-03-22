from dash import Dash, html, dcc, Input, Output, State, callback, no_update
from datetime import datetime
import dash_ag_grid as dag
import pandas as pd
from tradeiros.Tradeiros import Tradeiros

# 1. Configurações Globais
t = Tradeiros("okx")

# Definição fixa das colunas para evitar NameError
GRID_COLUMNS = ['tipo', 'operacao', 'min', 'max', 'qtd', 'valor', 'reduce', '%']

def get_processed_data():
    """Função auxiliar para capturar e formatar dados da lib Tradeiros"""
    df = t.atualizar()
    df['%'] = df['%'].round(2) 
    df = df[['tipo', 'operacao', 'preco_min', 'preco_max', 'qtd_ordens', 'qtd_sum', 'reduce', '%']]
    # Renomeia para bater com os fields do Grid
    df = df.rename(columns={'preco_min':'min', 'preco_max':'max', 'qtd_ordens':'qtd', 'qtd_sum':'valor'})
    return df.to_dict("records")

# Cores e Estilos de Identidade Visual HP
COLORS = {
    'background': '#0b0c10',       # Fundo da página
    'container': '#1f2833',        # Fundo dos cards
    'text': '#c5c6c7',             # Texto Principal
    'accent': '#f4b41a',           # Dourado HP (Novo)
    'accent_dark': '#bd8d12',      # Dourado Escuro
}

app = Dash(
    __name__, 
    external_stylesheets=[
        "https://unpkg.com/ag-grid-community/dist/styles/ag-grid.css",
        "https://unpkg.com/ag-grid-community/dist/styles/ag-theme-alpine-dark.css" # Ajustado de . para -
    ]
)

app.layout = html.Div([
    # COMPONENTE DE INTERVALO (30 Segundos)
    dcc.Interval(id='update-interval', interval=30*1000, n_intervals=0),

    # TOPPER / LOGO SECTION
    html.Div([
        html.Img(src="https://tradeiros.com.br/assets/logo_hp-BY7tjs3l.png", 
                 style={'height': '80px', 'marginBottom': '10px'}),
        
        # LABEL DE ÚLTIMA ATUALIZAÇÃO
        html.Div(id='last-update-label', 
                 children="Iniciando conexão...",
                 style={
                     'fontSize': '12px', 
                     'color': COLORS['text'], 
                     'opacity': '0.7',
                     'fontStyle': 'italic',
                     'marginTop': '-5px'
                 })
    ], style={'textAlign': 'center', 'padding': '20px 0', 'backgroundColor': COLORS['background']}),

    # CONTAINER PRINCIPAL (LADO A LADO)
    html.Div([
        
        # COLUNA 1: Estratégia Clássica
        html.Div([
            html.Div([
                html.Div([
                    html.Img(src="/assets/escudo.png", style={'height': '35px', 'marginRight': '10px'}),
                    html.H3("Carteira Clássica", 
                            style={'textAlign': 'center', 'color': COLORS['accent'], 'margin': '0', 'fontWeight': 'bold', 'display': 'inline-block', 'verticalAlign': 'middle'}),
                ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'padding': '15px 0'}),
                    dag.AgGrid(
                        id='grid-classica', 
                        rowData=[], 
                        columnDefs=[{"field": i} for i in GRID_COLUMNS],
                        defaultColDef={
                            "resizable": False, 
                            "sortable": False, 
                            "filter": False,
                            "flex": 1,
                        },
                        # Condicional para colorir as linhas: Verde (Buy) / Vermelho (Sell)
                        getRowStyle={
                            "styleConditions": [
                                {
                                    "condition": "params.data.tipo !== 'protected' && params.data.operacao === 'buy'",
                                    "style": {"color": "#22c55e"}
                                },
                                {
                                    "condition": "params.data.tipo !== 'protected' && params.data.operacao === 'sell'",
                                    "style": {"color": "#ef4444"}
                                },
                                {
                                    "condition": "params.data.tipo === 'protected'",
                                    "style": {"color":  COLORS['accent'], "fontWeight": "bold"}
                                },                                
                            ]
                        },
                        dashGridOptions={"pagination": False},
                        className="ag-theme-alpine-dark", 
                        style={"height": "650px", "width": "100%"}
                    ),
            ], style={'backgroundColor': COLORS['container'], 'borderRadius': '15px', 'overflow': 'hidden', 'boxShadow': '0px 10px 30px rgba(0,0,0,0.5)'})
        ], style={'flex': '1', 'minWidth': '400px', 'padding': '15px'}), 
        
        # COLUNA 2: Estratégia Agressiva 
        html.Div([
            html.Div([
                html.Div([
                    html.Img(src="/assets/caveira.png", style={'height': '35px', 'marginRight': '10px'}),
                    html.H3("Carteira Agressiva", 
                            style={'textAlign': 'center', 'color': COLORS['accent'], 'margin': '0', 'fontWeight': 'bold', 'display': 'inline-block', 'verticalAlign': 'middle'}),
                ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'padding': '15px 0'}),
                
                html.Div([
                    html.Div([
                        html.I(className="fas fa-chart-line", style={'fontSize': '48px', 'color': COLORS['accent'], 'opacity': '0.3'}),
                        html.P("Conteúdo Agressivo em Breve", 
                               style={'marginTop': '20px', 'color': COLORS['text'], 'fontStyle': 'italic', 'opacity': '0.5'})
                    ], style={'textAlign': 'center'})
                ], style={
                    'height': '650px', # Aumentado para 650px para alinhar com o da esquerda
                    'display': 'flex', 
                    'alignItems': 'center', 
                    'justifyContent': 'center',
                    'backgroundColor': COLORS['container'],
                    'border': f'2px dashed {COLORS["accent"]}',
                    'borderRadius': '0 0 15px 15px',
                    'margin': '-2px'
                })
            ], style={'backgroundColor': COLORS['container'], 'borderRadius': '15px', 'boxShadow': '0px 10px 30px rgba(0,0,0,0.5)'})
        ], style={'flex': '1', 'minWidth': '400px', 'padding': '15px'}) 
        
    ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'nowrap', 'maxWidth': '100%', 'margin': '0 20px'})
], style={
    'backgroundColor': COLORS['background'], 
    'height': '100vh', 
    'overflow': 'hidden', # Remove o scroll da página principal
    'fontFamily': '"Segoe UI", Roboto, Helvetica, Arial, sans-serif',
    'color': COLORS['text'],
    'paddingBottom': '20px'
})
    
# CSS Customizado
app.index_string = f'''
<!DOCTYPE html>
<html>
    <head>
        {{%metas%}}
        <title>Tradeiros HP Dashboard</title>
        {{%favicon%}}
        {{%css%}}
        <style>
            body {{
                margin: 0;
                overflow: hidden; /* Garante que o body não tenha scroll */
            }}
            .ag-theme-alpine-dark {{
                --ag-background-color: {COLORS['container']};
                --ag-odd-row-background-color: rgba(255, 255, 255, 0.03);
                --ag-header-background-color: {COLORS['container']};
                --ag-border-color: #333;
                --ag-foreground-color: {COLORS['text']};
            }}
            .ag-row-even {{
                background-color: {COLORS['container']} !important;
                color: {COLORS['text']};
                border-bottom: 1px solid #333 !important;
            }}
            .ag-row-odd {{
                background-color: #1a222c !important; /* Cor levemente diferente para o efeito zebra */
                color: {COLORS['text']};
                border-bottom: 1px solid #333 !important;
            }}
            .ag-header-cell {{
                background-color: {COLORS['background']} !important;
                border-bottom: 2px solid {COLORS['accent']} !important;
            }}
        </style>
    </head>
    <body style="margin: 0;">
        {{%app_entry%}}
        <footer>
            {{%config%}}
            {{%scripts%}}
            {{%renderer%}}
        </footer>
    </body>
</html>
'''

# CALLBACK DE ATUALIZAÇÃO PERIÓDICA
@callback(
    Output('grid-classica', 'rowData'),
    Output('last-update-label', 'children'),
    Output('last-update-label', 'style'),
    Input('update-interval', 'n_intervals')
)
def update_dashboard(n):
    try:
        data = get_processed_data()
        current_time = datetime.now().strftime("%H:%M:%S")
        status_msg = f"Última atualização: {current_time}"
        status_style = {'fontSize': '12px', 'color': COLORS['text'], 'opacity': '0.7', 'fontStyle': 'italic', 'marginTop': '-5px'}
        return data, status_msg, status_style
    except Exception as e:
        status_msg = "⚠️ erro na execução da api (re tentando...)"
        status_style = {'fontSize': '12px', 'color': '#ef4444', 'fontWeight': 'bold', 'marginTop': '-5px'}
        # Retorna o que já tinha no grid para não apagar a tela
        return no_update, status_msg, status_style

if __name__ == '__main__':
    # Rodando externamente para que você possa abrir o link clássico no navegador
    app.run(jupyter_mode="external", host='127.0.0.1', port=8050, debug=True)