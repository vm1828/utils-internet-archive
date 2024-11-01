import os
from multiprocessing import Process
from internetarchive import get_item, File

output_dirname = 'FOLDER_NAME'

def download(n):
    # get item
    item = get_item('MIT18.06S05_MP4')

    # add leading zero to 1-9
    n = f'0{n}' if 0 < n < 10 else str(n)

    # get file
    file = File(item, f'{n}.mp4')

    # output path
    output_filename = f'{file.metadata["title"]}.mp4'
    output_path = os.path.join(output_dirname, output_filename)

    # download
    file.download(output_path)

processes = [Process(target=download, args=(n,)) for n in range(25, 35)]
[p.start() for p in processes]
[p.join() for p in processes]