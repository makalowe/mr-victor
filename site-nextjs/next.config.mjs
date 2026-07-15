/** @type {import('next').NextConfig} */
const nextConfig = {
  poweredByHeader: false,
  reactStrictMode: true,
  output: process.env.CLOUDFLARE_STATIC === "1" ? "export" : undefined,
  images: process.env.CLOUDFLARE_STATIC === "1" ? { unoptimized: true } : undefined,
};

export default nextConfig;
