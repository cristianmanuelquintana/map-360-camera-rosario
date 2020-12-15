import requests
import pandas as pd
import json

def main():
    maxCams = 200
    endpoint = f'https://datos.rosario.gob.ar/api/action/datastore/search.json?resource_id=3fd90942-3edb-4737-8e4b-5f554e620de5&limit={maxCams}'

    outputFile = 'coordenadas.csv'
    r = requests.get(endpoint)

    if r.status_code in range(200,299):
        data = r.json()
        result = data['result']
        records = result['records']
        coordenadas = []
        for record in records:
            coorX = record['coordenadax']
            coorY = record['coordenaday']
            jotason = json.loads(record['geojson'])
            print(jotason)
            data = jotason['geometry']['coordinates']
            print (data)
            #geometria = feature['geometry']
            #feature = features[0]
            #geometria = features[0]
            #print(geometria)
            #coordinates = geometria['coordinates']
            #print(coordinates)
              #  for feature in jotason['features']:
               #     print(feature['geometry']['type'])
                #    print(feature['geometry']['coordinates'])
            #coordinates = jotason['features']['geometry']['coordinates']
            #print(coordinates)
            tupl = (coorX,coorY)
            coordenadas.append(tuple(data))
            #coordenadas.add(tupl)
        #print(records)
        print(r.status_code)
        #print(coordenadas)
    #print(r.json)

    df = pd.DataFrame(coordenadas)
    df.to_csv(outputFile, index=False,header=False)
    #coor = coordenadas[0]
    return coordenadas

if __name__ == "__main__":
    main()
