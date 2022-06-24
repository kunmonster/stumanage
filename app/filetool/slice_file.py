# 文件分片

def down_chunk_file_manager(file_path, chunk_size=1024):
    try:
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chunk_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break
    except FileNotFoundError:
        return -1
