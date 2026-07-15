"use client";

import Link from "next/link";
import { Building2, Car, ChevronDown, Factory, Gauge, Home, Menu, Route, Store, X } from "lucide-react";
import { useState } from "react";

export function Logo() {
  return <Link href="/" className="flex items-center gap-3" aria-label="Monsieur Victor, accueil"><span className="grid h-10 w-10 place-items-center rounded-xl bg-electric-500 font-black text-navy-950">MV</span><span className="text-lg font-extrabold tracking-tight text-white">Monsieur Victor</span></Link>;
}

const productLinks = [
  {label:"Recharge en entreprise",description:"Bornes pour sites, parkings et flottes",href:"/#recharge-entreprise",icon:Building2},
  {label:"Recharge à domicile",description:"Recharge des collaborateurs, suivie et remboursée",href:"/#recharge-domicile",icon:Home},
  {label:"Recharge en déplacement",description:"Accès aux réseaux publics et maîtrise des coûts",href:"/#recharge-deplacement",icon:Route},
  {label:"Supervision & pilotage",description:"Utilisateurs, énergie, disponibilité et reporting",href:"/solutions-techniques",icon:Gauge},
];

const needLinks = [
  {label:"Loueurs & flottes",href:"/solutions/loueurs-flottes",icon:Car},
  {label:"Concessionnaires",href:"/solutions/concessionnaires",icon:Store},
  {label:"Distribution & mobilité",href:"/solutions/grande-distribution-stations-service",icon:Building2},
  {label:"Industriels & employeurs",href:"/solutions/industriels-employeurs",icon:Factory},
];

export function Header() {
  const [open, setOpen] = useState(false);
  return <header className="sticky top-0 z-50 border-b border-white/10 bg-navy-950/95 backdrop-blur">
    <div className="container flex h-20 items-center justify-between">
      <Logo />
      <nav className="hidden items-center gap-6 text-sm font-semibold text-slate-200 lg:flex" aria-label="Navigation principale">
        <div className="group relative py-7"><button className="flex items-center gap-1" aria-haspopup="true">Produits <ChevronDown size={15}/></button><div className="invisible absolute left-0 top-16 w-[620px] rounded-2xl border border-slate-200 bg-white p-3 opacity-0 shadow-soft transition group-hover:visible group-hover:opacity-100 group-focus-within:visible group-focus-within:opacity-100"><div className="grid grid-cols-2 gap-1">{productLinks.map(({label,description,href,icon:Icon})=><Link key={label} href={href} className="flex gap-3 rounded-xl p-4 text-navy-950 hover:bg-slate-100"><Icon className="mt-0.5 shrink-0 text-electric-600" size={21}/><span><strong className="block">{label}</strong><span className="mt-1 block text-xs font-normal leading-5 text-slate-500">{description}</span></span></Link>)}</div></div></div>
        <div className="group relative py-7"><button className="flex items-center gap-1" aria-haspopup="true">Vos besoins <ChevronDown size={15}/></button><div className="invisible absolute left-1/2 top-16 w-80 -translate-x-1/2 rounded-2xl border border-slate-200 bg-white p-2 opacity-0 shadow-soft transition group-hover:visible group-hover:opacity-100 group-focus-within:visible group-focus-within:opacity-100">{needLinks.map(({label,href,icon:Icon})=><Link key={label} href={href} className="flex items-center gap-3 rounded-xl px-4 py-3 text-navy-950 hover:bg-slate-100"><Icon size={18} className="text-electric-600"/>{label}</Link>)}</div></div>
        <Link href="/methode">Notre méthode</Link><Link href="/references">Références</Link>
        <div className="group relative py-7"><button className="flex items-center gap-1" aria-haspopup="true">Ressources <ChevronDown size={15}/></button><div className="invisible absolute right-0 top-16 w-72 rounded-2xl border border-slate-200 bg-white p-2 opacity-0 shadow-soft transition group-hover:visible group-hover:opacity-100 group-focus-within:visible group-focus-within:opacity-100"><Link href="/ressources" className="block rounded-xl px-4 py-3 text-navy-950 hover:bg-slate-100">Guides & articles</Link><a href="/resources/livre-blanc-monsieur-victor.pdf" className="block rounded-xl px-4 py-3 text-navy-950 hover:bg-slate-100">Livre blanc entreprise</a><Link href="/references" className="block rounded-xl px-4 py-3 text-navy-950 hover:bg-slate-100">Études de cas</Link></div></div>
        <Link href="/a-propos">Entreprise</Link>
      </nav>
      <Link href="/devis" className="btn-primary hidden lg:inline-flex">Parler à un expert</Link>
      <button className="text-white lg:hidden" onClick={()=>setOpen(!open)} aria-label="Ouvrir le menu" aria-expanded={open}>{open?<X/>:<Menu/>}</button>
    </div>
    {open && <nav className="container max-h-[calc(100vh-5rem)] overflow-y-auto border-t border-white/10 py-5 text-sm font-semibold text-white lg:hidden"><p className="mb-3 text-xs uppercase tracking-widest text-electric-400">Nos produits</p><div className="grid gap-3">{productLinks.map(({label,href})=><Link onClick={()=>setOpen(false)} key={label} href={href}>{label}</Link>)}</div><p className="mb-3 mt-6 text-xs uppercase tracking-widest text-electric-400">Vos besoins</p><div className="grid gap-3">{needLinks.map(({label,href})=><Link onClick={()=>setOpen(false)} key={label} href={href}>{label}</Link>)}</div><div className="mt-6 grid gap-3 border-t border-white/10 pt-5">{[["Notre méthode","/methode"],["Références","/references"],["Ressources","/ressources"],["À propos","/a-propos"],["Contact","/contact"]].map(([l,h])=><Link onClick={()=>setOpen(false)} key={h} href={h}>{l}</Link>)}</div><Link onClick={()=>setOpen(false)} href="/devis" className="btn-primary mt-5 w-full">Parler à un expert</Link></nav>}
  </header>;
}
