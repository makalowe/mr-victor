import Image from "next/image";
import Link from "next/link";
import { ArrowRight, CheckCircle2 } from "lucide-react";
import { SectionTitle } from "./UI";

const brands = [
  {
    name:"Alfen",
    market:"Belgique & Pays-Bas",
    model:"Eve Double Plus",
    image:"/images/brands/alfen-eve-double-plus.webp",
    alt:"Borne électrique professionnelle Alfen Eve Double Plus",
    fit:"object-contain p-8",
    url:"https://alfen.com/nl-be/ev-oplaadpunten/zakelijk/eve-double-plus",
    text:"Une référence solide pour les parkings d’entreprise, les flottes et les déploiements AC au Benelux.",
  },
  {
    name:"Schneider Electric",
    market:"France",
    model:"EVlink Pro AC",
    image:"/images/brands/schneider-evlink-pro-ac.jpg",
    alt:"Gamme de bornes électriques Schneider Electric EVlink Pro AC",
    fit:"object-contain p-8",
    url:"https://www.se.com/fr/fr/product-range/23107242-evlink-pro-ac/",
    text:"Une solution adaptée aux bâtiments tertiaires, aux sites industriels et aux flottes dans les Hauts-de-France.",
  },
  {
    name:"Mennekes",
    market:"Allemagne & projets spécifiques",
    model:"AMTRON 4Business",
    image:"/images/brands/mennekes-amtron-4business.jpg",
    alt:"Borne électrique Mennekes AMTRON 4Business installée sur un parking",
    fit:"object-cover",
    url:"https://www.mennekes.org/emobility/products/amtron4business-700/",
    text:"Une gamme allemande robuste pour les entreprises, avec gestion de charge et compatibilité OCPP.",
  },
] as const;

export function BrandSelection(){return <section className="bg-slate-50 py-24"><div className="container"><div className="grid gap-10 lg:grid-cols-[1fr_.65fr] lg:items-end"><SectionTitle eyebrow="Une approche multimarque" title="La bonne borne dépend de votre projet" description="Nous réalisons d’abord l’étude électrique et technique. Nous comparons ensuite le matériel selon le site, la puissance, le nombre d’utilisateurs, la supervision attendue et le budget."/><div className="rounded-2xl border border-electric-500/30 bg-electric-500/10 p-6"><p className="flex gap-3 font-extrabold leading-7 text-navy-950"><CheckCircle2 className="mt-0.5 shrink-0 text-electric-600"/>Oui : suivant le projet, nous choisirons la marque la plus adaptée.</p></div></div><div className="mt-12 grid gap-6 lg:grid-cols-3">{brands.map(brand=><article className="overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm" key={brand.name}><div className="relative h-64 overflow-hidden bg-white"><Image src={brand.image} alt={brand.alt} fill sizes="(min-width: 1024px) 33vw, 100vw" className={brand.fit}/></div><div className="p-7"><p className="text-xs font-extrabold uppercase tracking-[.14em] text-electric-600">{brand.market}</p><h3 className="mt-3 text-2xl font-black text-navy-950">{brand.name}</h3><p className="mt-1 text-sm font-bold text-slate-500">{brand.model}</p><p className="mt-4 leading-7 text-slate-600">{brand.text}</p><a href={brand.url} target="_blank" rel="noreferrer" className="mt-6 inline-flex items-center gap-2 text-sm font-bold text-navy-950">Voir le fabricant <ArrowRight size={16}/></a></div></article>)}</div><div className="mt-10 flex flex-col items-start justify-between gap-5 rounded-2xl bg-white p-6 md:flex-row md:items-center"><p className="max-w-3xl text-sm leading-6 text-slate-500">Alfen, Schneider Electric et Mennekes sont des marques indépendantes. La sélection définitive reste soumise à l’étude technique, à la compatibilité logicielle, à la disponibilité du matériel et aux conditions du projet.</p><Link href="/devis" className="btn-dark shrink-0">Choisir la borne avec un expert <ArrowRight size={17}/></Link></div></div></section>}
