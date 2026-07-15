"use client";

import { ChevronDown } from "lucide-react";
import { useState } from "react";

export function FAQAccordion({items}:{items:readonly {q:string;a:string}[]}){
  const [open,setOpen]=useState(0);
  return <div className="divide-y divide-slate-200 border-y border-slate-200">{items.map((item,i)=><div key={item.q}><button onClick={()=>setOpen(open===i?-1:i)} className="flex w-full items-center justify-between gap-5 py-6 text-left font-bold text-navy-950" aria-expanded={open===i}>{item.q}<ChevronDown className={`shrink-0 transition ${open===i?'rotate-180':''}`}/></button>{open===i&&<p className="max-w-3xl pb-6 leading-7 text-slate-600">{item.a}</p>}</div>)}</div>
}
