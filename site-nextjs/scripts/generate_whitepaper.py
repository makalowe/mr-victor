from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, ListFlowable, ListItem, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "livre-blanc-monsieur-victor-recharge-entreprise.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = HexColor("#07131F")
NAVY_2 = HexColor("#12304B")
GREEN = HexColor("#00D67F")
GREEN_DARK = HexColor("#008A57")
INK = HexColor("#172536")
MUTED = HexColor("#5C6B7A")
LIGHT = HexColor("#F2F6F7")
LINE = HexColor("#DDE5E8")
WHITE = colors.white

font_dir = Path("C:/Windows/Fonts")
pdfmetrics.registerFont(TTFont("MV-Regular", str(font_dir / "arial.ttf")))
pdfmetrics.registerFont(TTFont("MV-Bold", str(font_dir / "arialbd.ttf")))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="MVTitle", fontName="MV-Bold", fontSize=28, leading=32, textColor=NAVY, spaceAfter=8))
styles.add(ParagraphStyle(name="MVH1", fontName="MV-Bold", fontSize=23, leading=27, textColor=NAVY, spaceAfter=8))
styles.add(ParagraphStyle(name="MVH2", fontName="MV-Bold", fontSize=14, leading=17, textColor=NAVY, spaceBefore=5, spaceAfter=5))
styles.add(ParagraphStyle(name="MVBody", fontName="MV-Regular", fontSize=9.5, leading=14, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="MVSmall", fontName="MV-Regular", fontSize=7.7, leading=10.5, textColor=MUTED))
styles.add(ParagraphStyle(name="MVCardTitle", fontName="MV-Bold", fontSize=11, leading=14, textColor=NAVY, spaceAfter=4))
styles.add(ParagraphStyle(name="MVCardBody", fontName="MV-Regular", fontSize=8.5, leading=12, textColor=INK))
styles.add(ParagraphStyle(name="MVEyebrow", fontName="MV-Bold", fontSize=8.2, leading=10, textColor=GREEN_DARK, spaceAfter=5))
styles.add(ParagraphStyle(name="MVWhiteTitle", fontName="MV-Bold", fontSize=27, leading=32, textColor=WHITE))
styles.add(ParagraphStyle(name="MVWhiteBody", fontName="MV-Regular", fontSize=11, leading=16, textColor=HexColor("#D6E1E7")))
styles.add(ParagraphStyle(name="MVQuote", fontName="MV-Bold", fontSize=14, leading=19, textColor=NAVY, alignment=TA_CENTER))


def p(text, style="MVBody"):
    return Paragraph(text, styles[style])


def bullets(items, level=0):
    return ListFlowable(
        [ListItem(p(item, "MVBody"), leftIndent=6) for item in items],
        bulletType="bullet", bulletColor=GREEN_DARK, bulletFontName="MV-Bold",
        leftIndent=15 + level * 6, bulletOffsetY=1, spaceAfter=5
    )


def card(title, body, accent=GREEN):
    data = [[p(title, "MVCardTitle")], [p(body, "MVCardBody")]]
    t = Table(data, colWidths=[78*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), WHITE),
        ("BOX", (0,0), (-1,-1), 0.7, LINE),
        ("LINEABOVE", (0,0), (-1,0), 3, accent),
        ("LEFTPADDING", (0,0), (-1,-1), 9),
        ("RIGHTPADDING", (0,0), (-1,-1), 9),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t


def card_grid(items, cols=2):
    rows=[]
    for i in range(0, len(items), cols):
        row=[card(*item) for item in items[i:i+cols]]
        while len(row)<cols: row.append("")
        rows.append(row)
    widths=[82*mm] * cols if cols==2 else [53*mm] * cols
    t=Table(rows, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    return t


def callout(title, text, bg=LIGHT):
    t=Table([[p(title,"MVCardTitle"), p(text,"MVCardBody")]], colWidths=[42*mm,120*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),0.7,LINE),
        ("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9)
    ]))
    return t


def page_intro(kicker, title, intro):
    return [p(kicker.upper(),"MVEyebrow"), p(title,"MVH1"), p(intro,"MVBody"), Spacer(1,4*mm)]


def header_footer(canvas, doc):
    page=canvas.getPageNumber()
    if page == 1:
        return
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1]-15*mm, A4[0], 15*mm, fill=1, stroke=0)
    canvas.setFont("MV-Bold", 7.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(20*mm, A4[1]-9.5*mm, "MONSIEUR VICTOR")
    canvas.setFont("MV-Regular", 7.2)
    canvas.setFillColor(HexColor("#C9D6DC"))
    canvas.drawRightString(A4[0]-20*mm, A4[1]-9.5*mm, "Livre blanc - recharge en entreprise")
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm, 14*mm, A4[0]-20*mm, 14*mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("MV-Regular", 7)
    canvas.drawString(20*mm, 9*mm, "Belgique - Wallonie - nord de la France")
    canvas.drawRightString(A4[0]-20*mm, 9*mm, str(page))
    canvas.restoreState()


story=[]

# Cover
story += [Spacer(1,18*mm)]
cover_box=Table([
    [p("MV", "MVWhiteTitle"), ""],
    [p("LIVRE BLANC 2026", "MVEyebrow"), ""],
    [p("Installer des bornes de recharge en entreprise", "MVWhiteTitle"), ""],
    [p("Le guide de décision pour passer d'une intention à un programme fiable, rentable et évolutif.", "MVWhiteBody"), ""],
    [Spacer(1,10*mm), ""],
    [p("BELGIQUE  |  WALLONIE  |  NORD DE LA FRANCE", "MVWhiteBody"), ""],
], colWidths=[145*mm,20*mm], rowHeights=[20*mm,12*mm,42*mm,28*mm,15*mm,18*mm])
cover_box.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),NAVY),("TEXTCOLOR",(0,0),(-1,-1),WHITE),
    ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
    ("TOPPADDING",(0,0),(-1,-1),9),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("LINEBELOW",(0,0),(-1,0),4,GREEN)
]))
story += [cover_box, Spacer(1,9*mm), p("Edition juillet 2026", "MVSmall"), p("Guide informatif - ne remplace pas un avis juridique, fiscal ou technique adapté à votre projet.", "MVSmall"), PageBreak()]

# 2
story += page_intro("L'essentiel", "Les 7 décisions qui font réussir un projet", "La borne n'est qu'une partie du système. La performance dépend surtout des usages, de la puissance disponible, du pilotage et du modèle d'exploitation.")
story += [card_grid([
    ("01. Qui recharge ?", "Flotte, salariés, visiteurs, clients ou véhicules prioritaires : chaque public implique des règles d'accès différentes."),
    ("02. Quand et combien de temps ?", "Le temps de stationnement détermine souvent mieux la puissance utile que la capacité maximale de la borne."),
    ("03. Quelle puissance réelle ?", "Le raccordement, les autres usages du bâtiment et les pointes de consommation cadrent le projet."),
    ("04. Qui paie ?", "Recharge gratuite, avantage salarié, refacturation, paiement visiteur ou centre de coûts interne."),
    ("05. Comment étendre ?", "Prévoir câbles, réserves électriques, génie civil et supervision pour les prochaines vagues."),
    ("06. Quel niveau de service ?", "Disponibilité, assistance, maintenance, pièces, délais d'intervention et responsabilité opérationnelle."),
    ("07. Quelles données ?", "Consommations, coûts, disponibilité, sessions, émissions évitées et indicateurs RSE."),
    ("Décision de départ", "Lancer un audit des usages et de l'installation électrique avant de choisir une marque ou un nombre définitif de bornes."),
],2), Spacer(1,4*mm), callout("Principe directeur", "Dimensionner pour l'usage réel aujourd'hui, mais préparer l'infrastructure pour l'usage probable demain.") , PageBreak()]

# 3
story += page_intro("Pourquoi agir", "La recharge devient une infrastructure métier", "Un programme bien conçu améliore l'exploitation, l'expérience des équipes et la capacité de l'entreprise à tenir ses engagements de mobilité.")
story += [card_grid([
    ("Performance de flotte", "Réduire les détours, l'attente et l'incertitude. Les véhicules prioritaires repartent avec l'autonomie nécessaire."),
    ("Maîtrise des coûts", "Consolider les consommations et limiter les remboursements manuels ou les notes de frais difficiles à contrôler."),
    ("Attractivité RH", "Proposer une recharge simple sur site ou à domicile renforce l'expérience des collaborateurs électrifiés."),
    ("Valeur commerciale", "Pour un commerce ou un site recevant du public, la recharge peut soutenir fréquentation, fidélité et image."),
    ("Pilotage RSE", "Produire des données exploitables pour les bilans, objectifs de flotte et rapports de durabilité."),
    ("Résilience", "Anticiper la croissance des véhicules électriques évite les travaux urgents et les choix techniques fragmentés."),
],2), Spacer(1,5*mm), p("Le bon business case additionne les économies directes, la réduction des frictions opérationnelles, la valeur RH et commerciale, et le risque évité.","MVQuote"), PageBreak()]

# 4
story += page_intro("Les usages", "Trois lieux de recharge, une seule politique", "La meilleure expérience combine le site de l'entreprise, le domicile des collaborateurs et la recharge en déplacement.")
matrix=[
    [p("Contexte","MVCardTitle"),p("Objectif","MVCardTitle"),p("Fonctions clés","MVCardTitle"),p("Indicateurs","MVCardTitle")],
    [p("Sur site","MVCardTitle"),p("Recharger pendant le stationnement naturel.","MVCardBody"),p("Accès, priorités, load balancing, paiement visiteur.","MVCardBody"),p("Disponibilité, énergie, taux d'usage.","MVCardBody")],
    [p("À domicile","MVCardTitle"),p("Équiper les véhicules de fonction sans charge administrative.","MVCardBody"),p("Installation standardisée, remboursement au kWh, gestion des départs.","MVCardBody"),p("Délai de pose, coût/session, satisfaction.","MVCardBody")],
    [p("En déplacement","MVCardTitle"),p("Garantir la continuité de mobilité hors site.","MVCardBody"),p("Badge, application, tarifs, facture consolidée.","MVCardBody"),p("Coût/kWh, hors politique, zones couvertes.","MVCardBody")],
]
t=Table(matrix,colWidths=[29*mm,45*mm,58*mm,34*mm],repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.5,LINE),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),("BACKGROUND",(0,2),(-1,2),LIGHT)]))
story += [t, Spacer(1,7*mm), callout("À éviter", "Trois prestataires, trois factures et trois référentiels utilisateurs. La politique doit rester lisible pour les RH, la flotte, la finance et les conducteurs."), PageBreak()]

# 5
story += page_intro("Cadrage", "La fiche de qualification avant toute étude", "Réunissez ces informations pour accélérer le diagnostic et comparer des scénarios cohérents.")
story += [card_grid([
    ("Parc de véhicules", "Nombre actuel et cible, modèles, kilométrage, retours au dépôt, temps d'arrêt, véhicules critiques."),
    ("Sites", "Adresses, nombre de places, propriété ou bail, horaires, accès public, contraintes de travaux."),
    ("Électricité", "Puissance souscrite, courbes de charge, tableaux, tension, production solaire, projets futurs."),
    ("Utilisateurs", "Salariés, flotte, visiteurs, clients, prestataires et règles de priorité attendues."),
    ("Finance", "Budget, mode d'achat ou de service, durée d'amortissement, refacturation et centres de coûts."),
    ("Calendrier", "Pilote, vagues de déploiement, dates de livraison véhicules, appels d'offres et dépendances réseau."),
],2), Spacer(1,4*mm), callout("Livrable attendu", "Un scénario minimal, un scénario cible et une trajectoire d'extension, chacun avec hypothèses, risques, budget complet et calendrier."), PageBreak()]

# 6
story += page_intro("Architecture", "AC, DC et temps de stationnement", "La puissance maximale n'est pas toujours la bonne réponse. Elle doit être alignée sur la rotation des véhicules et les contraintes du réseau.")
power=[
    [p("Usage type","MVCardTitle"),p("Solution indicative","MVCardTitle"),p("Logique de choix","MVCardTitle")],
    [p("Journée de travail / nuit","MVCardBody"),p("AC 7 à 22 kW","MVCardTitle"),p("Le véhicule dispose de plusieurs heures. Priorité à la simplicité et au pilotage collectif.","MVCardBody")],
    [p("Rotation de flotte","MVCardBody"),p("AC renforcée ou DC ciblée","MVCardTitle"),p("Réserver la puissance rapide aux véhicules dont la disponibilité crée de la valeur.","MVCardBody")],
    [p("Client de passage","MVCardBody"),p("AC ou DC selon durée","MVCardTitle"),p("Le temps de visite et le modèle économique déterminent la vitesse pertinente.","MVCardBody")],
    [p("Usage intensif","MVCardBody"),p("DC rapide","MVCardTitle"),p("Analyser raccordement, courbes de charge, coûts de pointe et redondance.","MVCardBody")],
]
t=Table(power,colWidths=[43*mm,42*mm,81*mm])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.5,LINE),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),("BACKGROUND",(0,2),(-1,2),LIGHT),("BACKGROUND",(0,4),(-1,4),LIGHT)]))
story += [t, Spacer(1,6*mm), bullets(["Compatibilité véhicules et connecteurs", "Interopérabilité et protocole ouvert de supervision", "Robustesse, accessibilité et signalétique", "Possibilité de mise à jour et disponibilité des pièces", "Mesure certifiée si la recharge est facturée"]), PageBreak()]

# 7
story += page_intro("Énergie", "Installer plus de points sans surdimensionner", "Le pilotage dynamique répartit la puissance disponible entre le bâtiment et les véhicules selon des règles métier.")
flow=[
    [p("Réseau / raccordement","MVCardTitle"), p("Bâtiment","MVCardTitle"), p("Gestionnaire d'énergie","MVCardTitle"), p("Bornes","MVCardTitle")],
    [p("Puissance disponible","MVCardBody"), p("Consommation variable","MVCardBody"), p("Mesure + priorités + limites","MVCardBody"), p("Charge répartie","MVCardBody")]
]
t=Table(flow,colWidths=[40*mm,40*mm,46*mm,40*mm])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY_2),("TEXTCOLOR",(0,0),(-1,0),WHITE),("BACKGROUND",(0,1),(-1,1),LIGHT),("GRID",(0,0),(-1,-1),1,WHITE),("BOX",(0,0),(-1,-1),0.7,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ALIGN",(0,0),(-1,-1),"CENTER"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12)]))
story += [t, Spacer(1,7*mm), card_grid([
    ("Priorité départ", "Donner plus de puissance aux véhicules qui doivent repartir en premier."),
    ("Plafond de site", "Ne jamais dépasser une limite convenue avec le bâtiment ou le gestionnaire de réseau."),
    ("Heures tarifaires", "Décaler les charges flexibles lorsque l'énergie ou la puissance est moins coûteuse."),
    ("Production locale", "Valoriser le photovoltaïque et, si pertinent, le stockage ou la recharge bidirectionnelle."),
],2), Spacer(1,4*mm), callout("Point de vigilance", "Le pilotage réduit souvent le besoin de renforcement, mais il ne remplace pas l'étude électrique ni l'analyse des scénarios de croissance."), PageBreak()]

# 8
story += page_intro("Méthode", "Un déploiement en 6 étapes", "Chaque étape doit produire un livrable, une décision et un responsable clairement identifiés.")
steps=[
    ("1. Cadrer", "Objectifs, usages, parties prenantes, calendrier et critères de succès."),
    ("2. Auditer", "Visite, installation électrique, puissance, plans, risques et contraintes de chantier."),
    ("3. Concevoir", "Scénarios, architecture, pilotage, coûts complets et trajectoire d'extension."),
    ("4. Autoriser", "Réseau, contrôle, urbanisme, bailleur, assurance, accessibilité et aides applicables."),
    ("5. Installer", "Travaux, essais, contrôle, documentation, formation et mise en service."),
    ("6. Exploiter", "Supervision, assistance, maintenance, reporting et amélioration continue."),
]
story += [card_grid(steps,2), Spacer(1,5*mm), p("Pour un programme multi-sites, commencez par un pilote représentatif, figez le standard, puis déployez par vagues avec un tableau de bord commun.","MVQuote"), PageBreak()]

# 9
story += page_intro("Belgique et Wallonie", "Conformité : les contrôles à intégrer au planning", "Le projet doit être vérifié au regard du RGIE, du bâtiment, du raccordement et des règles locales. Les exigences exactes dépendent de la configuration.")
story += [card_grid([
    ("Installation non domestique", "Le SPF Economie rappelle le contrôle avant mise en usage, lors d'une modification ou extension importante, puis périodiquement par un organisme agréé."),
    ("Dossier électrique", "Prévoir schémas, plans, notes de calcul, analyses de risques, déclarations de conformité et historique des modifications."),
    ("Gestionnaire de réseau", "Vérifier les modalités de déclaration, la puissance disponible, les délais d'étude et les conditions de raccordement auprès du GRD concerné."),
    ("Bâtiment", "Depuis 2021, des exigences d'électromobilité peuvent s'appliquer en Wallonie aux constructions ou rénovations importantes selon l'usage du bâtiment."),
    ("Accès public", "Si la borne est ouverte à des tiers, clarifier paiement, information tarifaire, accessibilité, fiscalité et responsabilités."),
    ("Aides", "Les dispositifs évoluent. Vérifier l'éligibilité avant signature et ne jamais intégrer une aide non confirmée au budget certain."),
],2), Spacer(1,4*mm), callout("Réflexe utile", "Demander une note de conformité projet listant les textes, contrôles et démarches applicables au site à la date d'investissement."), PageBreak()]

# 10
story += page_intro("Nord de la France", "Obligations : raisonner par bâtiment et parking", "Le cadre français distingue notamment bâtiments neufs ou rénovés, bâtiments non résidentiels existants, accessibilité et qualification des intervenants.")
story += [card_grid([
    ("Parkings non résidentiels", "Le ministère indique qu'à partir de 2025, les parkings de plus de 20 places sont concernés par un minimum d'équipement, sous réserve des règles et exceptions applicables."),
    ("Pré-équipement", "Les bâtiments neufs ou rénovés peuvent devoir préparer câblage, conduits et capacité future afin de faciliter l'ajout de points de charge."),
    ("Étude de conception", "Le Code de l'énergie prévoit une étude de conception électrique pour tout projet d'infrastructure dans un parking d'au moins 50 places."),
    ("Professionnels qualifiés", "Installation et maintenance relèvent de professionnels habilités et, dans les cas prévus, titulaires d'une qualification dédiée."),
    ("Accessibilité", "Le nombre et la configuration des places accessibles doivent être vérifiés selon le type de parking et son ouverture au public."),
    ("Aides et fiscalité", "ADVENIR et autres mécanismes ont leurs propres critères et calendriers. Confirmer l'éligibilité avant engagement."),
],2), Spacer(1,4*mm), callout("Important", "Ce guide donne une grille de vigilance, pas un avis juridique. Faites valider le cas précis du bâtiment, du permis, de l'usage et du parking."), PageBreak()]

# 11
story += page_intro("Économie", "Construire le coût complet, pas seulement le prix des bornes", "Le budget fiable couvre l'investissement, l'exploitation, l'énergie et les risques de disponibilité sur toute la durée du projet.")
costs=[
    [p("CAPEX","MVCardTitle"),p("OPEX","MVCardTitle"),p("Valeur / économies","MVCardTitle")],
    [bullets(["Audit et études", "Bornes et protections", "Génie civil et câblage", "Raccordement / puissance", "Signalétique et contrôle"]), bullets(["Supervision", "Connectivité", "Maintenance", "Assistance", "Énergie et frais de paiement"]), bullets(["Carburant évité", "Temps opérationnel gagné", "Notes de frais réduites", "Revenus de recharge", "Valeur RH et commerciale"])],
]
t=Table(costs,colWidths=[55*mm,55*mm,56*mm])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.5,LINE),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
story += [t, Spacer(1,6*mm), p("Formule de décision", "MVH2"), callout("Coût net annuel", "Annuité d'investissement + exploitation + énergie - économies de mobilité - revenus éventuels - aides confirmées."), Spacer(1,5*mm), bullets(["Tester une hypothèse basse, centrale et haute de taux d'utilisation.", "Isoler les coûts imposés par le site des coûts directement liés aux bornes.", "Valoriser séparément le risque évité et les bénéfices difficiles à monétiser.", "Prévoir un budget de croissance plutôt que de refaire le génie civil à chaque vague."]), PageBreak()]

# 12
story += page_intro("Exploitation", "Les indicateurs qui prouvent que le service fonctionne", "Une infrastructure installée n'est pas nécessairement une infrastructure disponible. Le pilotage doit commencer dès la mise en service.")
kpis=[
    ("Disponibilité", "Temps pendant lequel chaque point accepte réellement une session de recharge."),
    ("Taux d'usage", "Sessions ou heures actives rapportées à la capacité disponible."),
    ("Énergie délivrée", "kWh par site, véhicule, utilisateur et période."),
    ("Coût complet", "Énergie, abonnement, maintenance et frais ramenés au kWh ou au véhicule."),
    ("Incidents", "Volume, cause, délai de prise en charge et délai de rétablissement."),
    ("Satisfaction", "Simplicité, disponibilité perçue et qualité du support."),
]
story += [card_grid(kpis,3), Spacer(1,7*mm), callout("Contrat de service", "Définir qui surveille, qui informe les utilisateurs, qui intervient, sous quel délai, avec quelles pièces et quelles preuves de résolution."), Spacer(1,5*mm), bullets(["Préventif planifié", "Télédiagnostic et mises à jour", "Stock ou disponibilité des pièces critiques", "Escalade claire entre exploitant, installateur, fabricant et gestionnaire de réseau"]), PageBreak()]

# 13
story += page_intro("Appel d'offres", "La checklist pour comparer les prestataires", "Demandez des réponses comparables, vérifiables et orientées résultats plutôt qu'une simple liste de matériels.")
story += [card_grid([
    ("Périmètre", "Audit, études, fourniture, travaux, raccordement, contrôle, mise en service, supervision et maintenance."),
    ("Hypothèses", "Usages, puissances, plans, dépendances, exclusions, responsabilités et conditions de variation."),
    ("Technique", "Interopérabilité, protocole, comptage, cybersécurité, mises à jour, accessibilité et évolutivité."),
    ("Planning", "Pilote, vagues, délais réseau, jalons de validation, continuité d'activité et pénalités éventuelles."),
    ("Service", "SLA, assistance, maintenance, pièces, reporting, formation et réversibilité des données."),
    ("Références", "Projets comparables en volume, nombre de sites, complexité électrique et environnement réglementaire."),
],2), Spacer(1,5*mm), callout("Question décisive", "Que se passe-t-il si, dans trois ans, vous changez de superviseur, de matériel ou de modèle tarifaire ? La réponse révèle le niveau réel de dépendance fournisseur."), PageBreak()]

# 14
story += page_intro("Auto-évaluation", "Votre projet est-il prêt pour une étude ?", "Cochez les éléments déjà connus. Les cases manquantes constituent l'ordre du jour du premier atelier.")
check_items=[
    "Objectif métier et population concernée définis",
    "Nombre de véhicules actuel et cible à trois ans",
    "Temps de stationnement et kilométrages connus",
    "Sites et parkings prioritaires identifiés",
    "Factures, puissance et courbes de charge disponibles",
    "Règles d'accès et de paiement envisagées",
    "Propriétaire, bailleur et parties prenantes mobilisés",
    "Budget ou mode de financement cadré",
    "Calendrier véhicules / travaux / appels d'offres aligné",
    "Indicateurs de succès et niveau de service définis",
]
rows=[]
for i,item in enumerate(check_items,1):
    rows.append([p("□", "MVCardTitle"), p(item,"MVBody"), p("Oui  /  À cadrer","MVSmall")])
t=Table(rows,colWidths=[10*mm,115*mm,40*mm])
t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),0.4,LINE),("BACKGROUND",(0,1),(-1,1),LIGHT),("BACKGROUND",(0,3),(-1,3),LIGHT),("BACKGROUND",(0,5),(-1,5),LIGHT),("BACKGROUND",(0,7),(-1,7),LIGHT),("BACKGROUND",(0,9),(-1,9),LIGHT),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story += [t, Spacer(1,5*mm), p("7 réponses ou plus : vous pouvez lancer une étude structurée. Moins de 7 : commencez par un atelier de cadrage et un audit documentaire.","MVQuote"), PageBreak()]

# 15 CTA
story += page_intro("Passer à l'action", "Obtenez une première lecture de votre projet", "Monsieur Victor accompagne les entreprises en Belgique, avec un ancrage fort en Wallonie, ainsi que dans le nord de la France.")
qr=QrCodeWidget("https://peter-3j5.pages.dev/devis")
bounds=qr.getBounds(); size=38*mm
d=Drawing(size,size,transform=[size/(bounds[2]-bounds[0]),0,0,size/(bounds[3]-bounds[1]),0,0]); d.add(qr)
cta=Table([
    [p("Votre prochain pas", "MVH2"), d],
    [p("Préparez le nombre de véhicules, les sites, la puissance disponible et votre calendrier. Un expert vous aide à transformer ces données en scénarios comparables.","MVBody"), ""],
    [p("peter-3j5.pages.dev/devis", "MVCardTitle"), ""],
],colWidths=[112*mm,48*mm])
cta.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("BOX",(0,0),(-1,-1),1,LINE),("SPAN",(1,0),(1,2)),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10)]))
story += [cta, Spacer(1,8*mm), card_grid([
    ("Audit multi-sites", "Usages, puissance, architecture cible, risques et plan de déploiement."),
    ("Consultation / appel d'offres", "Cahier des charges, comparaison des offres et sécurisation des engagements."),
    ("Déploiement", "Coordination, installation, mise en service et documentation."),
    ("Exploitation", "Supervision, maintenance, assistance et reporting de performance."),
],2), PageBreak()]

# 16 sources
story += page_intro("Références", "Sources et limites de ce guide", "Références consultées en juillet 2026. Vérifiez toujours la version en vigueur et l'application à votre situation.")
sources=[
    ("SPF Economie - contrôle des installations électriques non domestiques", "https://economie.fgov.be/fr/themes/energie/sources-denergie/electricite/securite-et-controle-des/controle-des-installations-0"),
    ("L'Énergie en Wallonie - bornes de recharge", "https://energie.wallonie.be/home/au-quotidien/dans-les-deplacements/electromobilite/bornes-de-recharge.html"),
    ("ORES - mobilité électrique pour grandes entreprises", "https://www.ores.be/grande-entreprise/mobilite-electrique"),
    ("Service public de Wallonie - stratégie électromobilité", "https://spw.wallonie.be/actualites/electromobilite-la-wallonie-structure-son-plan-de-deploiement-des-bornes-de-recharge"),
    ("Ministère français de la Transition écologique - développer les bornes", "https://www.ecologie.gouv.fr/politiques-publiques/developper-bornes-recharge-vehicules-electriques"),
    ("Légifrance - Code de l'énergie, recharge des véhicules électriques", "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000023983208/LEGISCTA000043490866/"),
    ("Chargemap Business - guide obligations légales 2026, utilisé comme benchmark de structure", "Document communiqué par l'utilisateur"),
]
for title,url in sources:
    story += [p(f"<b>{title}</b><br/><font color='#5C6B7A'>{url}</font>","MVSmall"), Spacer(1,2.2*mm)]
story += [Spacer(1,4*mm), HRFlowable(width="100%",thickness=0.7,color=LINE), Spacer(1,4*mm), p("Avertissement", "MVH2"), p("Ce document est un guide d'aide à la décision. Il ne constitue ni un avis juridique ou fiscal, ni une étude électrique, ni une promesse d'aide financière. Les obligations, primes et conditions de raccordement évoluent et doivent être confirmées pour chaque site avant engagement.","MVBody")]

doc=SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=20*mm, leftMargin=20*mm,
    topMargin=22*mm, bottomMargin=18*mm, title="Installer des bornes de recharge en entreprise",
    author="Monsieur Victor", subject="Livre blanc B2B - Belgique, Wallonie et nord de la France"
)
doc.build(story,onFirstPage=header_footer,onLaterPages=header_footer)
print(OUTPUT)
