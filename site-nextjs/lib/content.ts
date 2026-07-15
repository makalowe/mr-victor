import { Building2, CarFront, Factory, ShoppingCart } from "lucide-react";

export const sectors = [
  {
    slug: "loueurs-flottes",
    short: "Loueurs & flottes",
    title: "Accélérez l’électrification de vos flottes, site après site",
    description: "Un programme de recharge transfrontalier conçu pour les loueurs, leasers et gestionnaires de flottes en Belgique, en Wallonie et dans le nord de la France : pilotage centralisé, coûts maîtrisés et expérience conducteur homogène.",
    icon: CarFront,
    benefits: ["Réduisez le TCO avec un dimensionnement adapté à l’usage réel", "Suivez énergie, disponibilité et coûts depuis un tableau de bord unique", "Déployez selon une méthode homogène sur l’ensemble de vos agences et dépôts", "Rassurez vos clients avec un parcours de recharge fiable"],
    offer: "Nous auditons vos usages, priorisons les sites et déployons un standard technique commun. La supervision consolide les données de recharge, les droits d’accès et la refacturation éventuelle.",
    caseStudy: "80 points de charge sur 12 agences, déployés en 14 semaines, avec 99,3 % de disponibilité mesurée.",
    criteria: ["Vous gérez plus de 20 véhicules électrifiés", "Vous avez plusieurs agences ou dépôts", "Vous cherchez à consolider les données de recharge", "Vous préparez un appel d’offres en Belgique ou dans le nord de la France"],
  },
  {
    slug: "concessionnaires",
    short: "Concessionnaires",
    title: "Transformez la recharge en avantage commercial",
    description: "Ajoutez une offre de recharge clé en main à chaque vente de véhicule électrique et équipez vos concessions sans multiplier les prestataires.",
    icon: Building2,
    benefits: ["Proposez une solution installée à vos clients professionnels", "Accélérez la livraison des véhicules électriques", "Équipez ateliers, showrooms et parkings clients", "Créez une nouvelle source de marge et de fidélisation"],
    offer: "Une offre en marque blanche ou co-brandée, un parcours de qualification simple pour vos vendeurs et un suivi partagé de chaque installation, de la visite technique à la mise en service.",
    caseStudy: "32 concessions harmonisées en 4 mois avec un interlocuteur projet unique et un reporting hebdomadaire.",
    criteria: ["Vous vendez des véhicules électriques à des professionnels", "Vous animez un réseau de concessions", "Vous souhaitez packager véhicule et recharge", "Vous devez équiper vos propres sites"],
  },
  {
    slug: "grande-distribution-stations-service",
    short: "Distribution & mobilité",
    title: "Faites de la recharge un service rentable et fidélisant",
    description: "Des infrastructures AC et DC pensées pour les supermarchés, centres commerciaux et réseaux de stations-service.",
    icon: ShoppingCart,
    benefits: ["Augmentez le temps de visite et la fidélité client", "Monétisez la recharge avec une tarification configurable", "Garantissez une disponibilité élevée sur les sites stratégiques", "Pilotez la puissance pour protéger vos coûts énergétiques"],
    offer: "Nous concevons le mix AC/DC, l’expérience de paiement, la signalétique, la supervision et la maintenance. Le modèle économique est simulé avant chaque décision d’investissement.",
    caseStudy: "24 bornes rapides sur 8 sites commerciaux, avec un taux d’usage supérieur de 31 % au scénario initial.",
    criteria: ["Vous exploitez un parking recevant du public", "Vous souhaitez facturer la recharge", "Vous avez plusieurs sites à standardiser", "La disponibilité du service est critique"],
  },
  {
    slug: "industriels-employeurs",
    short: "Industriels & employeurs",
    title: "Équipez vos sites pour les salariés et les véhicules de service",
    description: "Une infrastructure évolutive, conforme et pilotée pour répondre aux usages RH, flotte et visiteurs sans surdimensionner votre raccordement.",
    icon: Factory,
    benefits: ["Renforcez votre politique RH et votre trajectoire RSE", "Répondez aux obligations de pré-équipement et de recharge", "Répartissez la puissance disponible entre les usages", "Gérez simplement salariés, visiteurs et véhicules de service"],
    offer: "Audit électrique, plan pluriannuel, gestion des accès, refacturation et reporting carbone : une solution conçue pour s’intégrer à vos contraintes industrielles et immobilières.",
    caseStudy: "50 points de charge livrés en 6 semaines sur un site logistique maintenu en activité.",
    criteria: ["Vous employez plus de 100 personnes sur site", "Vous électrifiez votre flotte de service", "Vous avez une feuille de route CSRD/RSE", "Vous voulez éviter un renforcement électrique inutile"],
  },
] as const;

export const caseStudies = [
  { slug: "atlas-mobility", client: "Atlas Mobility", sector: "Loueurs & flottes", count: "80 bornes", duration: "14 semaines", result: "99,3 % de disponibilité", summary: "Un déploiement transfrontalier standardisé sur 12 agences en Belgique et dans le nord de la France, sans interrompre l’exploitation." },
  { slug: "nordis-retail", client: "Nordis Retail", sector: "Distribution & mobilité", count: "24 bornes DC", duration: "10 semaines", result: "+31 % d’usage", summary: "Un service de recharge monétisé, intégré au parcours fidélité de l’enseigne." },
  { slug: "hexagone-industries", client: "Hexagone Industries", sector: "Industriels & employeurs", count: "50 points", duration: "6 semaines", result: "42 tCO₂e évitées/an", summary: "Recharge salariés et flotte avec pilotage dynamique de la puissance disponible." },
];

export const articles = [
  { slug: "aides-recharge-belgique-france", title: "Aides pour les bornes de recharge en Belgique et en France : que vérifier ?", category: "Financement", excerpt: "Dispositifs régionaux ou français, éligibilité et pièces à préparer avant de lancer votre projet.", readTime: "7 min", publishedAt:"2026-06-18", keyword:"aides bornes recharge entreprise Belgique" },
  { slug: "dimensionner-bornes-flotte", title: "Comment dimensionner les bornes de recharge d’une flotte électrique ?", category: "Guide technique", excerpt: "Une méthode pragmatique fondée sur les kilomètres, les temps d’arrêt et la puissance réellement disponible.", readTime: "9 min", publishedAt:"2026-06-04", keyword:"dimensionnement bornes flotte électrique" },
  { slug: "obligations-parking-entreprise", title: "Parking d’entreprise : obligations et pré-équipement des bornes", category: "Réglementation", excerpt: "Les points de vigilance pour les propriétaires, exploitants et directions immobilières en Belgique et dans le nord de la France.", readTime: "6 min", publishedAt:"2026-05-21", keyword:"obligation borne recharge parking entreprise" },
  { slug: "recharge-domicile-collaborateurs", title: "Recharge à domicile des collaborateurs : organiser le remboursement", category: "Flotte & RH", excerpt: "Compteur, preuve de recharge, tarif énergétique et politique interne : les décisions à prendre pour un remboursement fiable.", readTime: "8 min", publishedAt:"2026-05-07", keyword:"remboursement recharge domicile collaborateur Belgique" },
  { slug: "pilotage-dynamique-puissance", title: "Pilotage dynamique : installer plus de bornes sans augmenter la puissance", category: "Énergie", excerpt: "Comment répartir la puissance disponible entre véhicules, bâtiment et production sans fragiliser l’exploitation.", readTime: "8 min", publishedAt:"2026-04-23", keyword:"pilotage dynamique bornes recharge entreprise" },
  { slug: "cahier-charges-bornes-multisites", title: "Le cahier des charges d’un déploiement de bornes multi-sites", category: "Achats", excerpt: "Les critères techniques, opérationnels et contractuels à intégrer dans un appel d’offres de recharge B2B.", readTime: "10 min", publishedAt:"2026-04-09", keyword:"cahier des charges bornes recharge entreprise" },
];

export const faqs = [
  { q: "Quel délai prévoir pour un déploiement multi-sites ?", a: "Après audit, un premier site peut généralement être livré sous 6 à 10 semaines. Un programme multi-sites est ensuite industrialisé par vagues, avec un planning et un reporting partagés." },
  { q: "Dans quelles régions intervenez-vous ?", a: "Nous intervenons en Belgique, avec un ancrage fort en Wallonie, ainsi que dans le nord de la France. Cette couverture transfrontalière permet de conserver un pilotage centralisé tout en assurant la proximité d’intervention." },
  { q: "Comment évitez-vous de surdimensionner l’installation électrique ?", a: "Nous analysons les usages réels et mettons en place un pilotage dynamique de la puissance. Les véhicules se partagent l’énergie disponible selon des règles de priorité." },
  { q: "La maintenance est-elle incluse ?", a: "Nous proposons des contrats avec supervision à distance, maintenance préventive, assistance utilisateurs et engagements de rétablissement adaptés à la criticité de chaque site." },
  { q: "Gérez-vous les aides et dossiers administratifs ?", a: "Oui. Nous identifions les dispositifs applicables et préparons les pièces techniques nécessaires, sans promettre une aide avant confirmation de l’éligibilité." },
  { q: "Peut-on refacturer la recharge aux salariés ou visiteurs ?", a: "Oui. La supervision permet d’identifier les utilisateurs, d’appliquer des règles tarifaires et d’exporter les données nécessaires à la refacturation." },
];
