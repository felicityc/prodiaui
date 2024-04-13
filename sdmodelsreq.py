import requests
import csv

def fetch_models(url):
    headers = {
        "accept": "application/json",
        "X-Prodia-Key": "761f0024-623c-49ac-aba9-44b15887458f"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def write_to_csv(data, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Model Name", "ID"])
        for item in data:
            model_name, model_id = item.split(" [")
            model_id = model_id[:-1]
            writer.writerow([model_name, model_id])

def main():
    print("Select an option to fetch the valid list of checkpoint models:")
    print("1. SD Models")
    print("2. SDXL Models")
    print("3. Both")
    choice = input("Input: ")

    if choice == '1':
        url = "https://api.prodia.com/v1/sd/models"
        csv_file = "sd_models.csv"
        models_data = fetch_models(url)
        write_to_csv(models_data, csv_file)
        print("Valid SD models list written.")
    elif choice == '2':
        url = "https://api.prodia.com/v1/sdxl/models"
        csv_file = "sdxl_models.csv"
        models_data = fetch_models(url)
        write_to_csv(models_data, csv_file)
        print("Valid SDXL models list written.")
    elif choice == '3':
        url_sd = "https://api.prodia.com/v1/sd/models"
        url_sdxl = "https://api.prodia.com/v1/sdxl/models"
        csv_file_sd = "sd_models.csv"
        csv_file_sdxl = "sdxl_models.csv"
        models_data_sd = fetch_models(url_sd)
        models_data_sdxl = fetch_models(url_sdxl)
        write_to_csv(models_data_sd, csv_file_sd)
        write_to_csv(models_data_sdxl, csv_file_sdxl)
        print("Lists written.")
    else:
        print("Invalid input. Please try again. *smiles*")

if __name__ == "__main__":
    main()
