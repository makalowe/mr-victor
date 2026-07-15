import { promises as fs } from "fs";
import path from "path";

export type LeadRecord={id:string;createdAt:string;status:"new";source:"website";sector:string;volume:string;sites:number;locations:string;horizon:string;name:string;role:string;company:string;email:string;phone:string;message?:string};
export interface LeadRepository{save(lead:LeadRecord):Promise<void>}
class JsonLeadRepository implements LeadRepository{
  private file=path.join(process.cwd(),"data","leads.json");
  async save(lead:LeadRecord){await fs.mkdir(path.dirname(this.file),{recursive:true});let leads:LeadRecord[]=[];try{leads=JSON.parse(await fs.readFile(this.file,"utf8"))}catch{}leads.push(lead);await fs.writeFile(this.file,JSON.stringify(leads,null,2),"utf8")}
}
export const leadRepository:LeadRepository=new JsonLeadRepository();
