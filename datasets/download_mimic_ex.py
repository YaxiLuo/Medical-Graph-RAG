from datasets import load_dataset

def download_dataset():
    dataset = load_dataset("morson/mimic_ex")
    dataset["train"].to_json("./data/mimic_ex_train.json", orient="records", lines=True)
    print("Successfully download at ./data/mimic_ex_train.json")

if __name__ == "__main__":
    download_dataset()