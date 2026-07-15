interface Env {
  CONTACT_EMAIL?: string;
  RESEND_API_KEY?: string;
  RESEND_FROM_EMAIL?: string;
}

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const lead = await request.json<Record<string, unknown>>().catch(() => null);
  if (!lead || !lead.email || !lead.company || !lead.consent) {
    return Response.json({ error: "Certains champs sont invalides." }, { status: 400 });
  }

  if (!env.RESEND_API_KEY || !env.CONTACT_EMAIL) {
    return Response.json(
      { error: "L’envoi email doit encore être configuré sur Cloudflare." },
      { status: 503 },
    );
  }

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: env.RESEND_FROM_EMAIL || "Monsieur Victor <onboarding@resend.dev>",
      to: [env.CONTACT_EMAIL],
      subject: `Nouveau projet — ${String(lead.company)}`,
      text: Object.entries(lead).map(([key, value]) => `${key}: ${String(value)}`).join("\n"),
    }),
  });

  if (!response.ok) {
    return Response.json({ error: "L’email n’a pas pu être envoyé." }, { status: 502 });
  }

  return Response.json({ ok: true }, { status: 201 });
};
