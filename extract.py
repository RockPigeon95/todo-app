import zipfile as zf


def extract_archive(archive_path, destination_dir):
    with zf.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_dir)
