import requests
import os



# https://data.bris.ac.uk/datasets/s5hqmjcdj8yo2ibzi9b4ew3sn/N00E100-N10E110_FABDEM_V1-2.zip

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

try:
    download_raster(-23.5, -46.5, 'rasters')
    print('Download realizado com sucesso')
except requests.exceptions.HTTPError as e:
    print(f'Ocorreu um erro: {e}')

download_raster(-23.5, -46.5, 'rasters')
print('Download realizado com sucesso')