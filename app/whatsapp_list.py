import pandas as pd


file = '/mnt/c/Users/Secre/dev/bot-recap/bot/app/data/ESTOQUE VIPAL.xlsx'


def load_whatsapp_data(file_path: str, sheet_name: str = None):

    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5)

    df = df.dropna(how='all')

    phone_numbers = df['TELEFONE']
    value = df['VALOR']
    
    
    
    print(df.head())
    return df 


load_whatsapp_data(file, sheet_name='PROD')

