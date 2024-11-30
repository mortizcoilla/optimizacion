import yfinance as yf
import pandas as pd

# Definir tickers y rango de fechas
tickers = ["AGUAS-A.SN", "ANDINA-B.SN", "CAP.SN", "CCU.SN", "CENCOSUD.SN", "CMPC.SN", "COLBUN.SN",
           "CONCHATORO.SN", "COPEC.SN", "ENELAM.SN", "ENELCHILE.SN", "ENTEL.SN", "FALABELLA.SN",
           "IAM.SN", "LTM.SN", "MALLPLAZA.SN", "PARAUCO.SN", "QUINENCO.SN", "RIPLEY.SN", "SMU.SN",
           "SQM-B.SN", "VAPORES.SN", "ABC.SN", "AESANDES.SN", "ALMENDRAL.SN", "AQUACHILE.SN",
           "BANVIDA.SN", "BESALCO.SN", "BICECORP.SN", "BLUMAR.SN", "BOLSASTGO.SN", "CAMANCHACA.SN",
           "CAMPOS.SN", "CAROZZI.SN", "CASABLANCA.SN", "CEMENTOS.SN", "CGE.SN", "CIC.SN", "CINTAC.SN",
           "COPEVAL.SN", "COVADONGA.SN", "CRUZADOS.SN", "CUPRUM.SN", "EDELMAG.SN", "ELECMETAL.SN",
           "EMBONOR-B.SN", "EMILIANA.SN", "ENAEX.SN", "ENELGXCH.SN", "ENJOY.SN", "ENLASA.SN",
           "FEPASA.SN", "FORUS.SN", "FOSFOROS.SN", "GASCO.SN", "GRANADILLA.SN", "HABITAT.SN",
           "HIPERMARC.SN", "HITES.SN", "IANSA.SN", "ILC.SN", "INDISA.SN", "INFODEMA.SN", "INGEVEC.SN",
           "INVERCAP.SN", "INVERNOVA.SN", "IPAL.SN", "LIPIGAS.SN", "MANQUEHUE.SN", "MARINSA.SN",
           "MASISA.SN", "MELON.SN", "MOLLER.SN", "MOLYMET.SN", "NAVARINO.SN", "NIBSA.SN", "NITRATOS.SN",
           "NTGCLGAS.SN", "NUTRAVALOR.SN", "OXIQUIM.SN", "PAZ.SN", "PEHUENCHE.SN", "PLANVITAL.SN",
           "POLPAICO.SN", "PROVIDA.SN", "PUNTILLA.SN", "QUEMCHI.SN", "QUILICURA.SN", "SALFACORP.SN",
           "SALMOCAM.SN", "BSANTANDER.SN", "SCHWAGER.SN", "SECURITY.SN", "SIEMEL.SN", "SIXTERRA.SN",
           "SK.SN", "SOCOVESA.SN", "SONDA.SN", "SOPROCAL.SN", "SOQUICOM.SN"
           ]

end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(years=5)

# Descargar datos de Yahoo Finance
data = yf.download(tickers, start=start_date, end=end_date, interval="1wk")

# Seleccionamos solo el 'Adj Close' y creamos una copia para trabajar en ella
prices = data['Adj Close'].copy()

# Ordenar datos por fecha
prices.sort_index(inplace=True)

# Modificar columnas: quitar sufijo ".SN" de los tickers
prices.columns = prices.columns.str.replace(".SN", "", regex=False)

# Ruta donde se desea guardar el archivo
output_file = "/home/makabrus/Workspace/Optimizacion/data/outputs/prices.csv"

# Guardar el archivo CSV
prices.to_csv(output_file)

print(f"Archivo guardado en {output_file}")
