import pandas as pd

planilha = pd.read_excel("https://seducgogov-my.sharepoint.com/:x:/g/personal/herick_alves_seduc_go_gov_br/IQBsKuQp4xzzRbqjDcicCPuSARdwkE-PWWqTIy6la0Dsaqo?e=KLGD8X")
planilha.raise_for_status()
planilha.info()
planilha.head()