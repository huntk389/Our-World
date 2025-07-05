import time
from tqdm import tqdm

def build_index():
    for _ in tqdm(range(5), desc="Building index"):
        time.sleep(1)

if __name__ == "__main__":
    build_index()
