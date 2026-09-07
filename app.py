import requests

def main():
    r = requests.get("https://catfact.ninja/fact")
    print(" Cat Fact: ", r.json()['fact'])

if __name__ == "__main__":
    main()