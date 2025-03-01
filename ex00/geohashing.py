import sys
import antigravity

# informaicon de la libreria: https://github.com/python/cpython/blob/3.13/Lib/antigravity.py

def main():
    try:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
        datedow = sys.argv[3].encode('utf-8')
        
        antigravity.geohash(lat, lon, datedow)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # main()
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Error: Required exactly 3 arguments: latitude longitude date")