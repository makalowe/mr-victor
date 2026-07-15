import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ArrowRight, Gauge, Layers3, ShieldCheck, TrendingDown } from "lucide-react";
import Link from "next/link";
import { sectors } from "@/lib/content";
import { CheckList, CTABanner, FeatureCard, HeroSection, SectionTitle } from "@/components/UI";

export function generateStaticParams(){return sectors.map(s=>({slug:s.slug}))}
export function generateMetadata({params}:{params:{slug:string}}):Metadata{const s=sectors.find(x=>x.slug===params.slug);return s?{title:`Bornes de recharge ${s.short}`,description:s.description}:{}}
export default function SectorPage({params}:{params:{slug:string}}){const s=sectors.find(x=>x.slug===params.slug);if(!s)notFound();return <>
  <HeroSection eyebrow={`Solution · ${s.short}`} title={s.title} description={s.description} secondary={{label:"Découvrir notre méthode",href:"/methode"}}/>
  <section className="py-24"><div className="container"><SectionTitle eyebrow="Bénéfices métier" title="Une infrastructure conçue autour de votre exploitation"/><div className="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-4">{s.benefits.map((b,i)=>{const icons=[TrendingDown,Gauge,Layers3,ShieldCheck];return <FeatureCard key={b} icon={icons[i]} title={b.split(" ").slice(0,3).join(" ")}>{b}</FeatureCard>})}</div></div></section>
  <section className="bg-slate-50 py-24"><div className="container grid items-center gap-12 lg:grid-cols-2"><div><SectionTitle eyebrow="Une offre adaptée" title="Le bon niveau de service, du pilote au déploiement transfrontalier"/><p className="mt-6 text-lg leading-8 text-slate-600">{s.offer}</p><Link href={`/devis?secteur=${s.slug}`} className="btn-dark mt-8">Étudier mon projet <ArrowRight size={17}/></Link></div><div className="rounded-4xl bg-navy-950 p-9 text-white"><p className="text-sm font-bold uppercase tracking-widest text-electric-400">Exemple de déploiement</p><p className="mt-8 text-3xl font-black leading-tight">{s.caseStudy}</p><p className="mt-6 text-sm text-slate-400">Cas présenté à titre illustratif. Les résultats dépendent du contexte technique et opérationnel.</p></div></div></section>
  <section className="py-24"><div className="container grid gap-12 lg:grid-cols-2"><SectionTitle eyebrow="Qualification" title="Ce projet vous concerne si…"/><CheckList items={s.criteria}/></div></section>
  <CTABanner title={`Vous pilotez un projet ${s.short.toLowerCase()} ?`} text="Recevez une première lecture technique et opérationnelle sous 24h ouvrées."/>
</>}
