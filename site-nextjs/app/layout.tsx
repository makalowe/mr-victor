import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import "./globals.css";

const inter=Inter({subsets:["latin"],display:"swap"});
export const metadata:Metadata={metadataBase:new URL(process.env.NEXT_PUBLIC_SITE_URL||"https://www.monsieur-victor.fr"),title:{default:"Monsieur Victor | Bornes de recharge pour entreprises",template:"%s | Monsieur Victor"},description:"Déploiement de bornes de recharge pour entreprises en Belgique, en Wallonie et dans le nord de la France.",openGraph:{type:"website",locale:"fr_BE",siteName:"Monsieur Victor"},robots:{index:true,follow:true}};
const organization={"@context":"https://schema.org","@type":"Organization",name:"Monsieur Victor",url:"https://www.monsieur-victor.fr",email:"projets@monsieur-victor.fr",telephone:"+33184802026",areaServed:[{"@type":"Country",name:"Belgique"},{"@type":"AdministrativeArea",name:"Wallonie"},{"@type":"AdministrativeArea",name:"Hauts-de-France"}],description:"Conception, installation et maintenance de bornes de recharge pour entreprises en Belgique et dans le nord de la France."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="fr"><body className={inter.className}><a href="#contenu" className="sr-only focus:not-sr-only focus:fixed focus:z-[100] focus:bg-white focus:p-3">Aller au contenu</a><Header/><main id="contenu">{children}</main><Footer/><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(organization)}}/></body></html>}
