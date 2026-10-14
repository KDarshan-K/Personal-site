# Darshan Kagadal — Static Portfolio

A small, content-first static-site generator designed for Python 3.12+. Inspired by the philosophy of simple engineering/publishing websites; this is an independent implementation, not a copy of Reweb.

## Requirements
- Python 3.12+
- pip

## Windows PowerShell setup

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m sitegen build
python -m http.server 8000 --directory dist
```

Open http://localhost:8000.

If `python` resolves to MSYS2 Python, use the explicit Windows Python executable to create the venv, for example:
`& "C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python312\python.exe" -m venv .venv`

## Editing content
- Edit `content/about.md`, `content/projects/*.md`, `content/notes/*.md`, and `content/research/*.md`.
- Markdown files support YAML front matter.
- Edit `site.yml` for site metadata and social links.
- Edit `assets/css/site.css` for styling.

## Build
```powershell
python -m sitegen build
```
Output is generated into `dist/`. It is safe to delete `dist/` and rebuild.

## Notes
- Contact is currently a `mailto:` link, not a server-backed form.
- The sample paper entry is explicitly marked as a placeholder. Replace it with accurate publication details or remove it before publishing.
- Review all profile links and project details before deploying.
