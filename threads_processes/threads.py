import threading
import urllib.request
import time


def download_image(image_url, save_as):
    print(f"Downloading {image_url}...")
    urllib.request.urlretrieve(image_url, save_as)
    print(f"Downloaded {image_url} as {save_as}.")


base_url = "https://commons.wikimedia.org/wiki/Special:NewFiles#/media/File:"
image_urls = [
    base_url + "Christopher_Street_Day_Berlin_2019_510.jpg",
    base_url + "CSD_Frankfurt_Slubice_2021_029.jpg",
    base_url + "21.04.2023_MUC-Stammtisch-Erkundung_18.jpg",
    base_url + "SAZANKA_STREET_(52478707745).jpg",
]

start_time = time.time()

for i, image_url in enumerate(image_urls):
    download_image(image_url, f"image{i+1}.jpg")

sequential_time = time.time() - start_time
print(f"\nSequential download time: {sequential_time:.2f} seconds\n")

start_time = time.time()

threads = []

for i, image_url in enumerate(image_urls):
    thread = threading.Thread(target=download_image,
                              args=(image_url, f"image_threaded{i+1}.jpg"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

multithreaded_time = time.time() - start_time
print(f"\nMultithreaded download time: {multithreaded_time:.2f} seconds\n")

print(f"Perf impr using threads: {sequential_time/multithreaded_time:.2f}x")
