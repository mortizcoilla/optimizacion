import yfinance as yf
import pandas as pd

# Carga tu lista de tickers (puedes reemplazar esta lista con la tuya propia)
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
           "SK.SN", "SOCOVESA.SN", "SONDA.SN", "SOPROCAL.SN", "SOQUICOM.SN"]

# Lista para almacenar los datos recolectados
data = []

# Recorre cada ticker y descarga la información básica
for ticker_symbol in tickers:
    print(f"Procesando: {ticker_symbol}")
    try:
        # Crea el objeto del ticker
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        
        # Agrega la información básica del activo a la lista de datos
        data.append({
            "Ticker": ticker_symbol,
            "Nombre completo": info.get("longName", "No disponible"),
            "Sector": info.get("sector", "No disponible"),
            "Industria": info.get("industry", "No disponible"),
        })
    except Exception as e:
        print(f"Error procesando {ticker_symbol}: {e}")
        data.append({
            "Ticker": ticker_symbol,
            "Nombre completo": "Error al obtener datos",
            "Sector": "N/A",
            "Industria": "N/A",
        })

# Convierte los datos a un DataFrame de pandas
tickers_df = pd.DataFrame(data)

# Remueve el sufijo ".SN" de los valores en el campo 'Ticker'
tickers_df["Ticker"] = tickers_df["Ticker"].str.replace(".SN", "", regex=False)

# Remueve el sufijo " S.A." de los valores en el campo 'Nombre completo'
tickers_df["Nombre completo"] = tickers_df["Nombre completo"].str.replace(" S.A.", "", regex=False)

# Guarda los datos en un archivo CSV
output_file = "/home/makabrus/Workspace/Optimizacion/data/outputs/tickers.csv"
tickers_df.to_csv(output_file, index=False)

print(f"Archivo guardado en {output_file}")
