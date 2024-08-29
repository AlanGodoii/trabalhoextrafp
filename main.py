import threading
import time
import random


def download_file(file_name):
    print(f"Iniciando download de {file_name}...")
    time_to_download = random.randint(1, 5)
    time.sleep(time_to_download)
    print(f"{file_name} foi baixado em {time_to_download} segundos!")


def main():
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
    threads = []

#
    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todos os downloads pendentes, foram concluídos com êxito.")

if __name__ == "__main__":
    main()
