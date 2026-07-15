import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        navy: { 950: "#07131F", 900: "#0B1F33", 800: "#12304B", 700: "#184567" },
        electric: { 400: "#22E69B", 500: "#00D67F", 600: "#00AE68" },
      },
      boxShadow: { soft: "0 24px 60px rgba(7, 19, 31, .10)" },
      borderRadius: { "4xl": "2rem" },
    },
  },
  plugins: [],
} satisfies Config;
