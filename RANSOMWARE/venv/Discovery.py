import os


def discover(initial_path):
    extensions = [
        # 'exe,', 'all', 'so', 'rpm' # arquivos do sistema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # videos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # microsoft office
        # openoffice, adobe, latex, markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # banco de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # codigo fonte c e c++
        'java', 'class', 'jar',  # codigo fonte java
        'ps', 'bat', 'vb',  # script de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # script de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffe',  # outros tipos de codigos fonte

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # arquivos compactados e backups
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abs_path(os.path.join(dirpath, file))
            ext = absolute_path.split('.')[-1]
            if ext in extencions:
                yield absolute_path


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
      print(i)