# Backup Log - MR VICTOR

## 2026-06-06

### Site public
- Main page rebuilt: `site-conformite.html`
- Root redirect added: `index.html`
- Logo added: `mr-victor-logo.svg`
- Public preview link:
  `https://htmlpreview.github.io/?https://raw.githubusercontent.com/makalowe/mr-victor/main/site-conformite.html`

### GitHub
- Repository: `https://github.com/makalowe/mr-victor`
- Branch: `main`
- Last published commit before this backup: `a3e85c4 publish mr victor landing page`

### Local preview
- Local URL: `http://127.0.0.1:8001/site-conformite.html`
- Phone preview on same Wi-Fi: `http://192.168.0.239:8001/site-conformite.html`

### Content state
- Brand: `MR VICTOR`
- Offer: mise en conformite electrique RGIE
- Counters: 110 installations, 108 acceptations, 98% passage conforme
- Zones: Wallonie + Bruxelles
- CTA: devis gratuit sous 24h

### Notes
- GitHub Pages still needs manual activation if a clean `makalowe.github.io/mr-victor` URL is required.
- HTMLPreview works as an immediate public client link.

## 2026-06-06 - Formspree

### Configuration site
- Form action: `https://formspree.io/f/fa222847ba1b23bc`
- JavaScript centralise l'ID dans `formspreeFormId`.
- Champs envoyes: nom, telephone, email, ville, besoin, message, source.
- Fallback: si Formspree refuse l'envoi, le site ouvre un email vers `contact@mrvictor.be`.

### A faire dans Formspree
- Creer/verifier le formulaire dans le dashboard Formspree.
- Copier le vrai form ID depuis Integration > endpoint.
- Remplacer `fa222847ba1b23bc` dans `site-conformite.html` si l'ID actuel n'est pas celui du compte.
- Faire un premier test reel et confirmer l'email de reception dans Formspree.
