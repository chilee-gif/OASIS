import os

def split_file(file_path, chunk_size_mb=40):
    chunk_size = chunk_size_mb * 1024 * 1024
    file_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    
    with open(file_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_name = f"{file_name}.part{part_num}"
            part_path = os.path.join(dir_name, part_name)
            with open(part_path, 'wb') as part_file:
                part_file.write(chunk)
            print(f"Created {part_name}")
            part_num += 1

if __name__ == "__main__":
    split_file("/media/chi/ai_/Thesis_Oasis/assets/base.obj")
