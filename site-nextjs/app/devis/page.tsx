import type { Metadata } from "next";
import { Suspense } from "react";
import { MultiStepQuoteForm } from "@/components/QuoteForm";
export const metadata:Metadata={title:"Devis installation de bornes électriques",description:"Demandez un devis pour une installation de bornes électriques en Belgique, en Wallonie ou dans les Hauts-de-France."};
export default function Devis(){return <section className="bg-slate-50 py-16 md:py-24"><div className="container"><div className="mx-auto mb-12 max-w-3xl text-center"><p className="text-sm font-extrabold uppercase tracking-widest text-electric-600">Étude de projet</p><h1 className="mt-4 text-4xl font-black tracking-tight text-navy-950 md:text-6xl">Parlons volumes, sites et calendrier.</h1><p className="mt-5 text-lg text-slate-600">4 étapes, moins de 3 minutes. Vos réponses permettent à notre expert de préparer un échange utile dès le premier contact.</p></div><Suspense><MultiStepQuoteForm/></Suspense></div></section>}
