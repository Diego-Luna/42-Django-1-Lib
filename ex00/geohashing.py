import sys
import antigravity

# ! informaicon de la libreria: https://github.com/python/cpython/blob/3.13/Lib/antigravity.py

def main(latituide, longitude, date):
    try:
        lat = float(latituide)
        lon = float(longitude)
        datedow = date.encode('utf-8')
        
        antigravity.geohash(lat, lon, datedow)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        # print(sys.argv[1])
        # print(sys.argv[2])
        # print(sys.argv[3])
        main(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Error: Required exactly 3 arguments: latitude longitude date")