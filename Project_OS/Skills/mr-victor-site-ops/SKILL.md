---
name: mr-victor-site-ops
description: Maintain, preview, publish, and back up the MR VICTOR static website. Use when working on site-conformite.html, mr-victor-logo.svg, GitHub publication, local preview URLs, client preview links, or Project_OS/Obsidian backup notes for MR VICTOR.
---

# MR VICTOR Site Ops

## Core Files

- Main public page: `site-conformite.html`
- GitHub Pages entry redirect: `index.html`
- Logo and favicon: `mr-victor-logo.svg`
- Local project notes / Obsidian backup: `Project_OS/`

## Local Preview

Use the workspace root:

```powershell
cd "C:\Users\MIMBI\OneDrive\Bureau\MR VICTOR"
python -m http.server 8001 --bind 0.0.0.0
```

Open:

```text
http://127.0.0.1:8001/site-conformite.html
```

For phone preview on the same Wi-Fi, get the PC IPv4 with `ipconfig`, then use:

```text
http://<PC_IP>:8001/site-conformite.html
```

Current known local Wi-Fi IP from the last run: `192.168.0.239`.

## Public Preview

The repository is:

```text
https://github.com/makalowe/mr-victor
```

Usable public preview link:

```text
https://htmlpreview.github.io/?https://raw.githubusercontent.com/makalowe/mr-victor/main/site-conformite.html
```

Use GitHub Pages later for a cleaner URL:

```text
https://makalowe.github.io/mr-victor/
```

To activate it manually: GitHub repo > Settings > Pages > Source: Deploy from branch > Branch: `main` > Folder: `/root`.

## Change Workflow

1. Edit only the required site files.
2. Verify local HTTP status is `200`.
3. Reload with a cache-busting query, for example `?v=7`.
4. Check that the logo, images, CTA links, counters, and form still work.
5. Update `Project_OS/03_Execution/BACKUP_LOG.md` if the change is meaningful.
6. Commit and push to GitHub.

## Brand Facts

- Brand name: `MR VICTOR`
- Service: mise en conformite electrique RGIE
- Zone: Wallonie + Bruxelles
- Promise: devis gratuit sous 24h
- Current counters: 110 installations, 108 acceptations, 98% passage conforme
- Phone placeholder: `0470 00 00 00`
- Email placeholder: `contact@mrvictor.be`

## Verification Checklist

Run these checks before final delivery:

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8001/site-conformite.html" -UseBasicParsing
Invoke-WebRequest -Uri "http://127.0.0.1:8001/mr-victor-logo.svg" -UseBasicParsing
git status --short
```

If using the in-app browser, verify:

- Page title contains `MR VICTOR`
- Header logo is loaded from `mr-victor-logo.svg`
- Counters animate to `110`, `108`, `98%`
- No console errors
