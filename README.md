# 🗃️ File.io
An API wrapper for the file.io web service.

## Install
```bash
$ pip3 install fileio
```

or

```bash
$ git clone https://github.com/gr3atwh173/fileioapi
$ cd fileioapi
$ python3 setup.py install
```

## Run

```bash
$ fileio -web
```

or

```bash
$ fileio -desktop --upload
```

or

```bash
$ fileio -desktop --download
```

or

```bash
$ fileio --api
```

or

```bash
$ fileio --exportUpload --csv
```

or

```bash
$ fileio --exportUpload --json
```

or

```bash
$ fileio --exportUpload --sqlite3
```

or

```bash
$ fileio --exportUpload --postgreSQL
```

or

```bash
$ fileio --exportDownload --csv
```

or

```bash
$ fileio --exportDownload --json
```

or

```bash
$ fileio --exportDownload --sqlite3
```

or

```bash
$ fileio --exportDownload --postgreSQL
```


## Usage
```python
import fileioapi

# upload a file
resp = fileioapi.upload("image.png", expiry="12w")
> { ... }

# download a file and save to 'downloaded.png'
down = fileioapi.download(resp['link'], filename='downloaded.png')
> { ... }

```
