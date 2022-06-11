import pandas as pd
vax_df = pd.read_csv("datasets/dados_vacinacao.csv")

def rename_vax(vax_df):
    vax_df.loc[(vax_df.vacina_nome == 'COVID-19 ASTRAZENECA - ChAdOx1-S') | (vax_df.vacina_nome == 'COVID-19 ASTRAZENECA/FIOCRUZ - COVISHIELD'), 'vacina_nome'] = 'ASTRAZENECA'
    vax_df.loc[(vax_df.vacina_nome == 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC') | (vax_df.vacina_nome == 'COVID-19 SINOVAC - CORONAVAC'), 'vacina_nome'] = 'CORONAVAC'
    vax_df.loc[vax_df.vacina_nome == 'COVID-19 JANSSEN - Ad26.COV2.S', 'vacina_nome'] = 'JANSEN'
    vax_df.loc[vax_df.vacina_nome == 'COVID-19 PFIZER - COMIRNATY', 'vacina_nome'] = 'PFIZER'
    vax_df.loc[vax_df.vacina_nome == 'COVID-19 PEDIÁTRICA - PFIZER COMIRNATY', 'vacina_nome'] = 'PFIZER PEDIÁTRICA'

def update_vax_code(vax_df):
    vax_df.loc[vax_df.vacina_codigo == 89, 'vacina_codigo'] = 85
    vax_df.loc[vax_df.vacina_codigo == 98, 'vacina_codigo'] = 86

def rename_doses(vax_df):
    vax_df.loc[vax_df.vacina_descricao_dose	 == 'Dose', 'vacina_descricao_dose'] = 'Dose única'
    vax_df.loc[vax_df.vacina_descricao_dose	 == 'Dose Inicial', 'vacina_descricao_dose'] = '1ª Dose'
    vax_df.loc[vax_df.vacina_descricao_dose	 == 'Dose Adicional', 'vacina_descricao_dose'] = '2ª Dose'
    vax_df.loc[vax_df.vacina_descricao_dose	 == '2ª Dose Revacinação', 'vacina_descricao_dose'] = '2ª Dose'
    vax_df.loc[vax_df.vacina_descricao_dose	 == 'Única', 'vacina_descricao_dose'] = 'Dose única'
    vax_df.loc[(vax_df.vacina_descricao_dose == '3ª Dose') | (vax_df.vacina_descricao_dose == '4ª Dose'), 'vacina_descricao_dose'] = '2º Reforço'
    