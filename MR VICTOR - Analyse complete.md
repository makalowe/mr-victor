# MR VICTOR / ElecConform — Analyse complète

**Date** : 2026-05-06
**Statut** : Site vitrine one-page (prêt à déployer)
**Tags** : #projet #electricien #conformite #site-web #wallonie

---

## 1. Vision

Site vitrine pour **ElecConform**, entreprise d'électricité spécialisée dans la **mise en conformité électrique (RGIE)** en Wallonie et à Bruxelles. L'objectif est de générer des demandes de devis via un formulaire de contact et un bouton WhatsApp.

---

## 2. Arborescence du projet

```
MR VICTOR/
│
├── site-conformite.html                     # 🌐 SITE WEB (one-page complet)
│
├── Mise en conformité électrique.html       # 🗑️ Export ChatGPT (ignorer)
│
├── *.css (10 fichiers)                      # 🗑️ Cache CSS de l'export ChatGPT (ignorer)
│
└── images/
    ├── 1770654824_installation-borne-de-recharge-a-domicile.jpg
    ├── 66cf18060965f418894f2ebf_...publiC3A920le202808.png
    ├── planalarme_connectee_meilleures_top_2022.jpg
    ├── planbinstallation-bornes-maison-1-v16-9-fr.png
    └── téléchargement.jpg
```

> ⚠️ **Fichier unique** : tout le site est dans `site-conformite.html` (HTML + CSS + JS inline).

---

## 3. Contenu du site

### Pages (one-page)
| Section | Contenu |
|---|---|
| **Navbar** | Logo ElecConform, navigation (Accueil, Services, Process, Devis) |
| **Hero** | Titre + sous-titre + 2 CTA (Devis gratuit, WhatsApp) |
| **Services** | 4 cartes : Plans électriques, Mise en conformité, Pré-contrôle, Accompagnement |
| **Méthode** | 3 étapes : Devis gratuit → Mise en conformité → Plans + contrôle |
| **Zones d'intervention** | 6 provinces wallonnes + Bruxelles |
| **Formulaire de devis** | Nom, Téléphone, Ville, Message |
| **Footer** | Téléphone, Email, WhatsApp, Mentions légales, RGIE |

### Design
- **Thème** : Dark/or — fond #1a1a1a, accent or #D4AF37
- **Typo** : Segoe UI (système)
- **Style** : Élégant, professionnel, cartes arrondies, hover animations
- **Responsive** : Oui (1 breakpoint à 768px)

---

## 4. Stack technique

| Technologie | Usage |
|---|---|
| **HTML5** | Structure |
| **CSS3** (inline) | Styles + responsive + animations |
| **JavaScript** (inline) | Interception formulaire → `alert()` |

### Ce qui est absent
| Élément | Statut |
|---|---|
| Framework CSS | ❌ Aucun (CSS natif) |
| Backend | ❌ Aucun (formulaire non fonctionnel) |
| Base de données | ❌ Aucune |
| Hébergement | ❌ Fichier local uniquement |
| Nom de domaine | ❌ Aucun |
| HTTPS | ❌ Pas de certificat |
| Google Analytics | ❌ Pas de tracking |
| SEO | ❌ Pas de balises avancées |

---

## 5. Services proposés

| Service | Détail |
|---|---|
| 🔌 **Plans électriques** | Schémas unifilaires, plans de position obligatoires pour le contrôle |
| ⚡ **Mise en conformité** | Correction infractions, remplacement tableau, mise à la terre |
| 🧾 **Pré-contrôle** | Vérification avant organisme → éviter refus et frais |
| 🏁 **Accompagnement contrôle** | Présence le jour J, coordination Vinçotte / BTV |

### Zones d'intervention
📍 Bruxelles · Brabant wallon · Hainaut · Liège · Namur · Luxembourg

---

## 6. Problèmes identifiés

### 🔴 Critique (bloquant)

| Problème | Détail | Solution |
|---|---|---|
| **Formulaire non fonctionnel** | `alert()` uniquement — aucune donnée envoyée | **Formspree** (5 min, gratuit) ou **EmailJS** |
| **Numéro fictif partout** | `0470 00 00 00` — pas de vrai contact | Remplacer par le vrai numéro |
| **WhatsApp lien #** | `href="#"` — pas cliquable | `href="https://wa.me/3247XXXXXXX"` |
| **Aucune page de confirmation** | Après formulaire → `alert()` intrusif | Remplacer par message de succès inline |
| **Aucun hébergement** | Fichier local uniquement → personne ne le voit | Déployer sur Netlify (gratuit) ou Hostinger |

### 🟡 Forte priorité

| Problème | Solution |
|---|---|
| **Pas de SEO** (meta description, OG, JSON-LD, canoncial) | Ajouter dans le `<head>` |
| **Pas de favicon** | Icône éclair/prise |
| **Pas de Google Maps** | Embed carte des zones d'intervention |
| **Images inutilisées** (bornes, alarmes dans le dossier) | Les intégrer dans les cartes services |
| **Police unique Segoe UI** | Ajouter Google Font (Inter ou Poppins) |
| **Pas de smooth scroll** | `html { scroll-behavior: smooth; }` |
| **Pas de numéro dans le header** | Ajouter "Urgence ? 047X XX XX XX" dans la navbar |

### 🟢 Priorité moyenne

| Problème | Solution |
|---|---|
| Pas de témoignages clients | Ajouter 2-3 citations |
| Pas de logos organismes (Vinçotte, BTV, RGIE) | Crédibilité technique |
| Pas de FAQ | Rassure et convertit |
| Pas de blog / articles SEO | "Comment se passe un contrôle RGIE ?" |
| Pas de photos avant/après chantier | Preuve visuelle |
| Pas de dark mode toggle | Optionnel mais tendance |
| Pas de chat en direct | Tawk.to ou Crisp (gratuit) |

---

## 7. Plan d'exécution

### Phase 0 — Corrections immédiates (1 heure)
| Action | Temps |
|---|---|
| Remplacer `alert()` par Formspree | 10 min |
| Mettre le vrai numéro de téléphone | 2 min |
| Ajouter lien WhatsApp fonctionnel | 2 min |
| Ajouter page de confirmation | 10 min |
| Ajouter meta description + JSON-LD | 10 min |
| Ajouter favicon | 5 min |
| Ajouter smooth scroll | 1 min |
| **Total** | **~40 min** |

### Phase 1 — Déploiement (1 jour)
| Action | Détail |
|---|---|
| Hébergement Netlify | Glisser-déposer le fichier HTML |
| Nom de domaine | `elecconform.be` ou `mise-en-conformite-electrique.be` |
| HTTPS | Automatique avec Netlify |
| Google Maps embed | Ajouter carte des zones |
| WhatsApp direct | Lien wa.me fonctionnel |

### Phase 2 — Contenu & Crédibilité (semaine 1)
| Action | Détail |
|---|---|
| Ajouter témoignages clients | 3 citations |
| Ajouter logos Vinçotte / BTV / RGIE | Crédibilité |
| Ajouter FAQ | 5 questions fréquentes |
| Ajouter photos avant/après | Utiliser les images du dossier |
| Créer 3 articles blog | SEO longue traîne |

---

## 8. KPI cibles

| Indicateur | Cible J30 |
|---|---|
| Demandes de devis | 10 |
| Appels téléphoniques | 15 |
| Clics WhatsApp | 5 |
| Pages indexées Google | 3 |

---

## 9. Liens utiles

- Dossier projet : `C:\Users\MIMBI\OneDrive\Bureau\MR VICTOR`
- Site (fichier local) : `MR VICTOR/site-conformite.html`

Projets connexes :
- [[Papy Peter Permaculture]] — Partage possible du VPS Hostinger
- [[Email Campaign Manager]] — Module d'envoi d'emails pour relance prospects

---

## 10. Journal de mise à jour

- 2026-05-06 : Analyse complète du projet
- Date inconnue : Création du site `site-conformite.html`
