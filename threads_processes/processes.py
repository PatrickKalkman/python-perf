import multiprocessing
import urllib.request
import time


def download_image(image_url, save_as):
    print(f"Downloading {image_url}...")
    urllib.request.urlretrieve(image_url, save_as)
    print(f"Downloaded {image_url} as {save_as}.")


def main():
    base = "https://commons.wikimedia.org/wiki/Special:NewFiles#/media/File:"
    image_urls = [
        base + "Christopher_Street_Day_Berlin_2019_510.jpg",
        base + "CSD_Frankfurt_Slubice_2021_029.jpg",
        base + "21.04.2023_MUC-Stammtisch-Erkundung_18.jpg",
        base + "SAZANKA_STREET_(52478707745).jpg",
    ]

    start_time = time.time()

    for i, image_url in enumerate(image_urls):
        download_image(image_url, f"image{i+1}.jpg")

    sequential_time = time.time() - start_time
    print(f"\nSequential download time: {sequential_time:.2f} seconds\n")

    start_time = time.time()

    processes = []

    for i, image_url in enumerate(image_urls):
        process = multiprocessing.Process(
            target=download_image,
            args=(image_url, f"image_processed{i+1}.jpg"),
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    multiprocessed_time = time.time() - start_time
    print(f"\nMultiprocess download time: {multiprocessed_time:.2f} seconds\n")

    print(f"Perf impr process: {sequential_time/multiprocessed_time:.2f}x")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
