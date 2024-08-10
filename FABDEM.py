import requests
import os



class FABDEM:

    def CreateURL(lat, lon):
        # Exemplos de links para download de arquivos raster
        # https://data.bris.ac.uk/datasets/s5hqmjcdj8yo2ibzi9b4ew3sn/N00E100-N10E110_FABDEM_V1-2.zip
        # https://data.bris.ac.uk/datasets/s5hqmjcdj8yo2ibzi9b4ew3sn/N00E120-N10E130_FABDEM_V1-2.zip
        shortURL = 'https://data.bris.ac.uk/datasets/s5hqmjcdj8yo2ibzi9b4ew3sn/'
        
        # Adiciona zeros à esquerda para manter o padrão de dígitos
        # Caso a latitude ou longitude seja menor que 0, o link deve ser alterado para o padrão S ou W
        # Exemplo: S30W050-S-20W040_FABDEM_V1-2.zip
        # Gerar os limites de latitude e longitude somando mais 10

        if lat < 0:
            lat = abs(lat)
            lat = f'S{lat:02}'
        else:
            lat = f'N{lat:02}'

        if lon < 0:
            lon = abs(lon)
            lon = f'W{lon:03}'
        else:
            lon = f'E{lon:03}'

        URL = shortURL + f'{lat}{lon}-{lat + 10}{lon + 10}_FABDEM_V1-2.zip'
        print(URL)
        return URL
    

def download_raster(lat, lon, path):
    # Substitui pontos decimais por underscores
    lat_str = str(lat).replace('.', '_')
    lon_str = str(lon).replace('.', '_')
    url = f'http://www.bristol.ac.uk/geography/research/pf/zips/{lat_str}_{lon_str}.zip'
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    os.makedirs(path, exist_ok=True)  # Cria o diretório se não existir
    file_path = os.path.join(path, f'{lat_str}_{lon_str}.zip')
    with open(file_path, 'wb') as f:
        f.write(response.content)  # Escreve o conteúdo da resposta no arquivo
    return file_path


# S30W050-S-20W040_FABDEM_V1-2.zip
# N-25E-42-N-15E-32_FABDEM_V1-2.zip

FABDEM.CreateURL(-25, -42)
