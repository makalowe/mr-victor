import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import "./globals.css";

const inter=Inter({subsets:["latin"],display:"swap"});
export const metadata:Metadata={metadataBase:new URL(process.env.NEXT_PUBLIC_SITE_URL||"https://peter-3j5.pages.dev"),title:{default:"Installation de bornes électriques Belgique | Monsieur Victor",template:"%s | Monsieur Victor"},description:"Installation de bornes électriques pour entreprises en Belgique, en Wallonie et dans les Hauts-de-France.",keywords:["installation de bornes électriques Belgique Hauts-de-France","installation borne électrique entreprise","installateur bornes électriques Wallonie"],openGraph:{type:"website",locale:"fr_BE",siteName:"Monsieur Victor"},robots:{index:true,follow:true}};
const organization={"@context":"https://schema.org","@type":"Organization",name:"Monsieur Victor",url:"https://peter-3j5.pages.dev",email:"projets@monsieur-victor.fr",telephone:"+33184802026",areaServed:[{"@type":"Country",name:"Belgique"},{"@type":"AdministrativeArea",name:"Wallonie"},{"@type":"AdministrativeArea",name:"Hauts-de-France"}],description:"Installation de bornes électriques pour entreprises en Belgique, en Wallonie et dans les Hauts-de-France."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="fr"><body className={inter.className}><a href="#contenu" className="sr-only focus:not-sr-only focus:fixed focus:z-[100] focus:bg-white focus:p-3">Aller au contenu</a><Header/><main id="contenu">{children}</main><Footer/><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(organization)}}/></body></html>}
