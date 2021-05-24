# Tellus

This repository is an example of an unofficial implementation of Tellus.

## Requirements

- [asdf]

## Run sample CLI

### TelluSAR

```bash
python tellusar.py get_free -t 'Your API Token'
```

### DEUCE

```bash
python deuce.py search -t 'Your API Token' \
    -s alos3-pseudo \
    -lblat 33.631 \
    -lblon 130.369 \
    -rtlat 33.69 \
    -rtlon 130.438
```

## Run in Jupyter

```bash
jupyter lab
```

## Ready for editting

```shell
asdf plugin-add nodejs
asdf plugin-add python
asdf install
npm install
pip install --requirement requirements.txt
asdf reshim python
pre-commit install
```

## Lint

### pre-commit

```shell
pre-commit run --all-files
```

[asdf]: https://github.com/asdf-vm/asdf
