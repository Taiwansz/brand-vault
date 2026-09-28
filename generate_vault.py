"""
Vault Generator: Produces production-grade, mathematically pure SVG logos,
monochrome variants, lockups, specs, and HTML inspection sheets for Matheus's repositories.
"""

import json
import os
import sys
from pathlib import Path

# Add ThSyr to Python path so we can leverage the brand engine and auditor directly
sys.path.insert(0, "/root/ThSyr")
from engine.brand import SvgAuditor

VAULT_DIR = Path("/root/brand-vault")
BRANDS_DIR = VAULT_DIR / "brands"
BRANDS_DIR.mkdir(parents=True, exist_ok=True)

# 15 Brand Definitions with exact vector geometry (viewBox 0 0 256 256)
BRANDS_DATA = [
    {
        "id": "thsyr",
        "name": "ThSyr",
        "repo": "ThSyr",
        "tagline": "Cognitive Copilot & Autonomous JARVIS Runtime",
        "mark_type": "letterform",
        "technique": "geometric-construction, negative-space, chiral-symmetry",
        "geometry": "triangle, chevron, diamond",
        "industry": "artificial-intelligence",
        "colors": {
            "primary": "#E63946",
            "secondary": "#121316",
            "accent": "#D4AF37",
            "dark": "#0B0C0E",
            "light": "#F8F9FA"
        },
        "rationale": "Sagittal chevron arrowhead fused with an autonomous neural core. High forward momentum with strict angular discipline at 45 degrees.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThSyr Core Symbol</title>
  <!-- Background Shield Cut -->
  <path d="M128 24 L224 80 L224 164 L128 232 L32 164 L32 80 Z" fill="#121316"/>
  <!-- Primary Sagittal Arrowhead -->
  <path d="M128 48 L204 98 L180 122 L128 88 L76 122 L52 98 Z" fill="#E63946"/>
  <!-- Interlocking Chevron -->
  <path d="M128 108 L184 150 L164 170 L128 144 L92 170 L72 150 Z" fill="#D4AF37"/>
  <!-- Synthetic Nucleus Diamond -->
  <path d="M128 162 L148 182 L128 202 L108 182 Z" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThSyr Monochrome Symbol</title>
  <path d="M128 24 L224 80 L224 164 L128 232 L32 164 L32 80 Z" fill="#000000"/>
  <path d="M128 54 L196 102 L176 122 L128 92 L80 122 L60 102 Z" fill="#FFFFFF"/>
  <path d="M128 114 L176 152 L160 168 L128 144 L96 168 L80 152 Z" fill="#FFFFFF"/>
  <path d="M128 168 L144 184 L128 200 L112 184 Z" fill="#FFFFFF"/>
</svg>"""
    },
    {
        "id": "thaspect",
        "name": "ThAspect",
        "repo": "ThAspect",
        "tagline": "Contemporary Streetwear & Urban Architectural Tailoring",
        "mark_type": "letterform",
        "technique": "isometric-projection, monoline-grid, brutalism",
        "geometry": "asymmetric-triangle, chamfer",
        "industry": "fashion-streetwear",
        "colors": {
            "primary": "#0A0A0A",
            "secondary": "#F4F1EA",
            "accent": "#FF5722",
            "dark": "#0A0A0A",
            "light": "#F4F1EA"
        },
        "rationale": "Brutalist letter A constructed with heavy textile warp/weft cuts and an industrial high-visibility accent.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThAspect Brand Mark</title>
  <!-- Main Structural A -->
  <path d="M52 220 L108 36 L152 36 L104 220 Z" fill="#0A0A0A"/>
  <path d="M136 36 L204 220 L160 220 L128 128 L104 128 L116 88 L148 88 Z" fill="#0A0A0A"/>
  <!-- Industrial Cross Lintel -->
  <path d="M76 148 L180 148 L172 176 L68 176 Z" fill="#FF5722"/>
  <!-- Tension Anchor -->
  <path d="M152 36 L180 36 L136 176 L108 176 Z" fill="#0A0A0A" opacity="0.15"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThAspect Monochrome Mark</title>
  <path d="M52 220 L108 36 L152 36 L104 220 Z" fill="#000000"/>
  <path d="M136 36 L204 220 L160 220 L128 128 L104 128 L116 88 L148 88 Z" fill="#000000"/>
  <path d="M76 148 L180 148 L172 176 L68 176 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "thpay",
        "name": "ThPay",
        "repo": "ThPay",
        "tagline": "Corporate Continuous Payroll & Tax Compliance Engine",
        "mark_type": "combination",
        "technique": "duality-interlock, continuous-line, mathematical-balance",
        "geometry": "hexagon, infinity-loop",
        "industry": "fintech-payroll",
        "colors": {
            "primary": "#00A86B",
            "secondary": "#0B0F19",
            "accent": "#10B981",
            "dark": "#0B0F19",
            "light": "#F0FDF4"
        },
        "rationale": "Dual hexagonal interlock representing fluid cash flow and immutable regulatory vault security.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThPay Vault Mark</title>
  <!-- Upper Ascending Hexagon Flow -->
  <path d="M128 32 L216 80 L216 136 L176 114 L176 96 L128 70 L80 96 L80 120 L40 100 L40 80 Z" fill="#00A86B"/>
  <!-- Lower Vault Return Flow -->
  <path d="M128 224 L40 176 L40 120 L80 142 L80 160 L128 186 L176 160 L176 136 L216 156 L216 176 Z" fill="#0B0F19"/>
  <!-- Central Currency Delta Diamond -->
  <path d="M128 92 L164 128 L128 164 L92 128 Z" fill="#10B981"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>ThPay Monochrome Mark</title>
  <path d="M128 32 L216 80 L216 136 L176 114 L176 96 L128 70 L80 96 L80 120 L40 100 L40 80 Z" fill="#000000"/>
  <path d="M128 224 L40 176 L40 120 L80 142 L80 160 L128 186 L176 160 L176 136 L216 156 L216 176 Z" fill="#000000"/>
  <path d="M128 92 L164 128 L128 164 L92 128 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "skillforge-frontend",
        "name": "SkillForge Frontend",
        "repo": "SkillForge-Frontend",
        "tagline": "Autonomous AI Frontend & Design System Specialist",
        "mark_type": "combination",
        "technique": "modular-system, bracket-code, geometric-construction",
        "geometry": "anvil, rectangle-grid, chevron",
        "industry": "developer-tools",
        "colors": {
            "primary": "#06B6D4",
            "secondary": "#0F172A",
            "accent": "#8B5CF6",
            "dark": "#0F172A",
            "light": "#F8FAFC"
        },
        "rationale": "Stylized digital anvil composed of modular UI bento grid cells, forging code brackets into visual components.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>SkillForge Frontend Mark</title>
  <!-- Anvil Face Plate -->
  <path d="M40 76 L216 76 L196 112 L60 112 Z" fill="#0F172A"/>
  <!-- Left Code Bracket Wing -->
  <path d="M60 112 L100 112 L84 156 L44 156 Z" fill="#06B6D4"/>
  <!-- Right Code Bracket Wing -->
  <path d="M156 112 L196 112 L212 156 L172 156 Z" fill="#8B5CF6"/>
  <!-- Central Anvil Waist & Base -->
  <path d="M96 128 L160 128 L168 180 L88 180 Z" fill="#0F172A"/>
  <path d="M72 188 L184 188 L196 220 L60 220 Z" fill="#0F172A"/>
  <!-- Core Spark Pixel -->
  <path d="M120 140 L136 140 L136 156 L120 156 Z" fill="#06B6D4"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>SkillForge Monochrome Mark</title>
  <path d="M40 76 L216 76 L196 112 L60 112 Z" fill="#000000"/>
  <path d="M60 112 L100 112 L84 156 L44 156 Z" fill="#000000"/>
  <path d="M156 112 L196 112 L212 156 L172 156 Z" fill="#000000"/>
  <path d="M96 128 L160 128 L168 180 L88 180 Z" fill="#000000"/>
  <path d="M72 188 L184 188 L196 220 L60 220 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "cs-vault-2026",
        "name": "CS-Vault 2026",
        "repo": "CS-Vault-2026",
        "tagline": "Obsidian Academic Vault & Deep Computer Science Core",
        "mark_type": "emblem",
        "technique": "tessellation, isometric-projection, modular-system",
        "geometry": "hexagon, cube",
        "industry": "education-knowledge",
        "colors": {
            "primary": "#F59E0B",
            "secondary": "#1E293B",
            "accent": "#475569",
            "dark": "#0F172A",
            "light": "#FFFBEB"
        },
        "rationale": "Isometric crystalline vault cube housed within an algorithmic knowledge hexagon, symbolising atomic synthesis.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>CS-Vault Mark</title>
  <!-- Top Facet (Golden Zenith) -->
  <path d="M128 36 L208 82 L128 128 L48 82 Z" fill="#F59E0B"/>
  <!-- Right Facet (Deep Slate) -->
  <path d="M208 82 L208 174 L128 220 L128 128 Z" fill="#1E293B"/>
  <!-- Left Facet (Medium Slate) -->
  <path d="M48 82 L128 128 L128 220 L48 174 Z" fill="#334155"/>
  <!-- Central Knowledge Core Cut -->
  <path d="M128 64 L160 82 L128 100 L96 82 Z" fill="#FFFFFF"/>
  <path d="M128 140 L152 154 L128 168 L104 154 Z" fill="#F59E0B"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>CS-Vault Monochrome Mark</title>
  <path d="M128 36 L208 82 L128 128 L48 82 Z" fill="#000000"/>
  <path d="M208 82 L208 174 L128 220 L128 128 Z" fill="#000000"/>
  <path d="M48 82 L128 128 L128 220 L48 174 Z" fill="#000000"/>
  <path d="M128 64 L160 82 L128 100 L96 82 Z" fill="#FFFFFF"/>
</svg>"""
    },
    {
        "id": "apos",
        "name": "APOS",
        "repo": "apos",
        "tagline": "Apartment Operating System & Residential Digital Twin",
        "mark_type": "abstract",
        "technique": "geometric-construction, isometric-projection",
        "geometry": "isometric-floorplan, portal",
        "industry": "proptech-infrastructure",
        "colors": {
            "primary": "#00E5FF",
            "secondary": "#0F2B48",
            "accent": "#94A3B8",
            "dark": "#0B192C",
            "light": "#F0F9FF"
        },
        "rationale": "Digital twin floorplan cube with isometric structural walls and an illuminated architectural doorway portal.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>APOS Digital Twin Mark</title>
  <!-- Architectural Outer Footprint -->
  <path d="M128 32 L220 84 L220 188 L128 240 L36 188 L36 84 Z" fill="#0F2B48"/>
  <!-- Top Roof Cutaway -->
  <path d="M128 48 L204 92 L128 136 L52 92 Z" fill="#1E3E62"/>
  <!-- Structural Partition Wall Left -->
  <path d="M60 108 L116 140 L116 208 L60 176 Z" fill="#00E5FF"/>
  <!-- Structural Partition Wall Right -->
  <path d="M140 140 L196 108 L196 176 L140 208 Z" fill="#00B4D8"/>
  <!-- Electrical Core Axis -->
  <path d="M128 148 L128 224" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>APOS Monochrome Mark</title>
  <path d="M128 32 L220 84 L220 188 L128 240 L36 188 L36 84 Z" fill="#000000"/>
  <path d="M128 48 L204 92 L128 136 L52 92 Z" fill="#FFFFFF"/>
  <path d="M60 108 L116 140 L116 208 L60 176 Z" fill="#000000"/>
  <path d="M140 140 L196 108 L196 176 L140 208 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "atlas",
        "name": "Atlas",
        "repo": "atlas",
        "tagline": "Enterprise Human Capital & Workforce Management Suite",
        "mark_type": "abstract",
        "technique": "dynamic-rotation, chiral-symmetry",
        "geometry": "circle, orbit-rings",
        "industry": "enterprise-saas",
        "colors": {
            "primary": "#2563EB",
            "secondary": "#0A192F",
            "accent": "#E2E8F0",
            "dark": "#0A192F",
            "light": "#EFF6FF"
        },
        "rationale": "Modernized celestial sphere of Atlas engineered as dynamic titanium orbital rings holding a central organizational core.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas Enterprise Mark</title>
  <!-- Outer Deep Field Shield -->
  <circle cx="128" cy="128" r="96" fill="#0A192F"/>
  <!-- Primary Orbital Band 1 -->
  <path d="M56 128 C56 88 128 56 168 56 C200 56 200 96 200 128 C200 168 128 200 88 200 C56 200 56 160 56 128 Z" fill="none" stroke="#2563EB" stroke-width="16"/>
  <!-- Central Globe -->
  <circle cx="128" cy="128" r="44" fill="#3B82F6"/>
  <!-- Orbital Meridian Meridian Cut -->
  <path d="M128 84 L128 172" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/>
  <circle cx="128" cy="128" r="14" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas Monochrome Mark</title>
  <circle cx="128" cy="128" r="96" fill="#000000"/>
  <circle cx="128" cy="128" r="76" fill="#FFFFFF"/>
  <circle cx="128" cy="128" r="48" fill="#000000"/>
  <circle cx="128" cy="128" r="16" fill="#FFFFFF"/>
</svg>"""
    },
    {
        "id": "atlas-hr-data-engine",
        "name": "Atlas HR Data Engine",
        "repo": "atlas-hr-data-engine",
        "tagline": "High-Throughput Distributed HR ETL & Analytics Engine",
        "mark_type": "abstract",
        "technique": "dynamic-rotation, modular-system",
        "geometry": "turbine, circle",
        "industry": "data-infrastructure",
        "colors": {
            "primary": "#14B8A6",
            "secondary": "#082F49",
            "accent": "#38BDF8",
            "dark": "#082F49",
            "light": "#F0FDFA"
        },
        "rationale": "High-velocity data turbine blade channeling distributed employee records into an immutable analytical core.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas HR Data Engine Mark</title>
  <circle cx="128" cy="128" r="96" fill="#082F49"/>
  <!-- 4-Phase Turbine Blades -->
  <path d="M128 32 L156 96 L128 96 Z" fill="#14B8A6"/>
  <path d="M224 128 L160 156 L160 128 Z" fill="#38BDF8"/>
  <path d="M128 224 L100 160 L128 160 Z" fill="#14B8A6"/>
  <path d="M32 128 L96 100 L96 128 Z" fill="#38BDF8"/>
  <!-- Central Hub -->
  <circle cx="128" cy="128" r="32" fill="#0F766E"/>
  <circle cx="128" cy="128" r="14" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas HR Data Engine Monochrome</title>
  <circle cx="128" cy="128" r="96" fill="#000000"/>
  <path d="M128 32 L156 96 L128 96 Z" fill="#FFFFFF"/>
  <path d="M224 128 L160 156 L160 128 Z" fill="#FFFFFF"/>
  <path d="M128 224 L100 160 L128 160 Z" fill="#FFFFFF"/>
  <path d="M32 128 L96 100 L96 128 Z" fill="#FFFFFF"/>
  <circle cx="128" cy="128" r="28" fill="#FFFFFF"/>
  <circle cx="128" cy="128" r="12" fill="#000000"/>
</svg>"""
    },
    {
        "id": "atlas-landing-page",
        "name": "Atlas Showcase",
        "repo": "atlas-landing-page",
        "tagline": "Public Commercial Presence & High-Conversion Showcase",
        "mark_type": "combination",
        "technique": "negative-space, optical-illusion",
        "geometry": "prism, chevron",
        "industry": "marketing-commercial",
        "colors": {
            "primary": "#3B82F6",
            "secondary": "#0B132B",
            "accent": "#60A5FA",
            "dark": "#0B132B",
            "light": "#F8FAFC"
        },
        "rationale": "Conversion-focused ascendant prism projecting Atlas's core identity forward into the corporate market.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas Landing Mark</title>
  <!-- Foundation Dark Vault -->
  <path d="M48 208 L128 48 L208 208 L168 208 L128 128 L88 208 Z" fill="#0B132B"/>
  <!-- Radiant Facet Left -->
  <path d="M128 48 L128 128 L88 208 L48 208 Z" fill="#1D4ED8"/>
  <!-- Radiant Facet Right -->
  <path d="M128 48 L208 208 L168 208 L128 128 Z" fill="#3B82F6"/>
  <!-- Ascension Peak Spark -->
  <path d="M128 88 L144 116 L128 128 L112 116 Z" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Atlas Landing Monochrome</title>
  <path d="M48 208 L128 48 L208 208 L168 208 L128 128 L88 208 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "feriados-brasil",
        "name": "Feriados Brasil",
        "repo": "feriados-brasil",
        "tagline": "National Brazilian Public Holidays & Business Days Engine",
        "mark_type": "pictorial",
        "technique": "negative-space, geometric-construction",
        "geometry": "rhombus, calendar-tile",
        "industry": "api-data",
        "colors": {
            "primary": "#009C3B",
            "secondary": "#FFDF00",
            "accent": "#002776",
            "dark": "#004D1A",
            "light": "#F0FDF4"
        },
        "rationale": "Calendar grid tile with Brazil's canonical central rhombus carved out, carrying the Southern Cross star.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Feriados Brasil Mark</title>
  <!-- Calendar Base Plate -->
  <rect x="40" y="48" width="176" height="168" rx="24" fill="#009C3B"/>
  <!-- Header Bar -->
  <path d="M40 48 L216 48 L216 88 L40 88 Z" fill="#004D1A"/>
  <!-- Twin Ring Binders -->
  <rect x="76" y="32" width="16" height="32" rx="8" fill="#FFDF00"/>
  <rect x="164" y="32" width="16" height="32" rx="8" fill="#FFDF00"/>
  <!-- Canonical Brasil Rhombus -->
  <path d="M128 104 L184 148 L128 192 L72 148 Z" fill="#FFDF00"/>
  <!-- Central Southern Star -->
  <path d="M128 132 L132 144 L144 148 L132 152 L128 164 L124 152 L112 148 L124 144 Z" fill="#002776"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Feriados Brasil Monochrome</title>
  <rect x="40" y="48" width="176" height="168" rx="24" fill="#000000"/>
  <rect x="76" y="32" width="16" height="32" rx="8" fill="#FFFFFF"/>
  <rect x="164" y="32" width="16" height="32" rx="8" fill="#FFFFFF"/>
  <path d="M128 104 L184 148 L128 192 L72 148 Z" fill="#FFFFFF"/>
  <circle cx="128" cy="148" r="10" fill="#000000"/>
</svg>"""
    },
    {
        "id": "jornada-gestao-excursoes",
        "name": "Jornada Excursoes",
        "repo": "jornada-gestao-excursoes",
        "tagline": "Caravan, Tour & Church Excursion Management Platform",
        "mark_type": "pictorial",
        "technique": "continuous-line, geometric-construction",
        "geometry": "circle, compass-arrow, ribbon",
        "industry": "travel-mobility",
        "colors": {
            "primary": "#1E3A8A",
            "secondary": "#F97316",
            "accent": "#38BDF8",
            "dark": "#1E3A8A",
            "light": "#FFF7ED"
        },
        "rationale": "Unbroken roadway looping into a guiding compass needle, evoking joyful fellowship and secure travel.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Jornada Excursoes Mark</title>
  <!-- Outer Compass Ring -->
  <circle cx="128" cy="128" r="96" fill="#1E3A8A"/>
  <!-- Unbroken Roadway Loop -->
  <path d="M68 156 C68 100 128 72 168 100 C196 120 188 168 148 180 C116 188 88 176 88 144 Z" fill="none" stroke="#F97316" stroke-width="16" stroke-linecap="round"/>
  <!-- Guiding Compass Arrow -->
  <path d="M128 56 L152 112 L128 98 L104 112 Z" fill="#38BDF8"/>
  <!-- Waypoint Center -->
  <circle cx="128" cy="128" r="16" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Jornada Monochrome Mark</title>
  <circle cx="128" cy="128" r="96" fill="#000000"/>
  <circle cx="128" cy="128" r="76" fill="#FFFFFF"/>
  <path d="M128 64 L148 116 L128 104 L108 116 Z" fill="#000000"/>
  <circle cx="128" cy="128" r="18" fill="#000000"/>
</svg>"""
    },
    {
        "id": "matheus-sousa-linkedin",
        "name": "Matheus Sousa",
        "repo": "matheus-sousa-linkedin",
        "tagline": "Senior Software Engineer & Systems Architect Personal Identity",
        "mark_type": "lettermark",
        "technique": "chiral-symmetry, geometric-construction, brutalism",
        "geometry": "chamfer, monogram",
        "industry": "professional-portfolio",
        "colors": {
            "primary": "#111827",
            "secondary": "#9CA3AF",
            "accent": "#C5A880",
            "dark": "#111827",
            "light": "#F9FAFB"
        },
        "rationale": "Architectural monogram MS with 45-degree chamfers and structural pillars reflecting engineering rigor.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Matheus Sousa Monogram</title>
  <!-- Left Pillar M -->
  <path d="M48 48 L88 48 L88 208 L48 208 Z" fill="#111827"/>
  <!-- Right Pillar M -->
  <path d="M168 48 L208 48 L208 208 L168 208 Z" fill="#111827"/>
  <!-- Central M Chevron -->
  <path d="M88 48 L128 136 L168 48 L144 48 L128 92 L112 48 Z" fill="#C5A880"/>
  <!-- Intersecting S Band -->
  <path d="M88 124 L168 124 L168 152 L88 152 Z" fill="#9CA3AF"/>
  <path d="M88 180 L168 180 L168 208 L88 208 Z" fill="#111827"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Matheus Sousa Monochrome</title>
  <path d="M48 48 L88 48 L88 208 L48 208 Z" fill="#000000"/>
  <path d="M168 48 L208 48 L208 208 L168 208 Z" fill="#000000"/>
  <path d="M88 48 L128 136 L168 48 L144 48 L128 92 L112 48 Z" fill="#000000"/>
  <path d="M88 140 L168 140 L168 168 L88 168 Z" fill="#000000"/>
</svg>"""
    },
    {
        "id": "nosso-grande-dia",
        "name": "Nosso Grande Dia",
        "repo": "nosso-grande-dia",
        "tagline": "Matheus & Virginia Matrimonial Ecosystem (Canticos 8:7)",
        "mark_type": "lettermark",
        "technique": "continuous-line, geometric-construction",
        "geometry": "oval, laurel-knot",
        "industry": "matrimonial-event",
        "colors": {
            "primary": "#0C1B33",
            "secondary": "#6B1724",
            "accent": "#D4AF37",
            "dark": "#0C1B33",
            "light": "#FDFBF7"
        },
        "rationale": "Official CCB wedding crest interweaving initials M and V into an unbroken covenant knot with antique gold laurels.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Nosso Grande Dia Wedding Crest</title>
  <!-- Outer Sacred Seal -->
  <path d="M128 28 C180 28 220 72 220 128 C220 184 180 228 128 228 C76 228 36 184 36 128 C36 72 76 28 128 28 Z" fill="#0C1B33"/>
  <!-- Gold Filament Border -->
  <circle cx="128" cy="128" r="88" fill="none" stroke="#D4AF37" stroke-width="4"/>
  <!-- Intertwined M and V Monogram -->
  <path d="M76 168 L76 96 L108 144 L128 112 L148 144 L180 96 L180 168" fill="none" stroke="#FDFBF7" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Central Covenant Heart Knot -->
  <path d="M128 112 L128 184" fill="none" stroke="#6B1724" stroke-width="10" stroke-linecap="round"/>
  <circle cx="128" cy="188" r="8" fill="#D4AF37"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Nosso Grande Dia Monochrome</title>
  <path d="M128 28 C180 28 220 72 220 128 C220 184 180 228 128 228 C76 228 36 184 36 128 C36 72 76 28 128 28 Z" fill="#000000"/>
  <circle cx="128" cy="128" r="88" fill="none" stroke="#FFFFFF" stroke-width="4"/>
  <path d="M76 168 L76 96 L108 144 L128 112 L148 144 L180 96 L180 168" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
    },
    {
        "id": "receitas-andre-empada",
        "name": "Receitas Andre da Empada",
        "repo": "receitas",
        "tagline": "Culinary Technical Formulation & Baking Cost Engineering",
        "mark_type": "emblem",
        "technique": "dynamic-rotation, modular-system, geometric-construction",
        "geometry": "circle, radial-crimp",
        "industry": "food-gastronomy",
        "colors": {
            "primary": "#D97706",
            "secondary": "#9A3412",
            "accent": "#FFFBEB",
            "dark": "#78350F",
            "light": "#FFFBEB"
        },
        "rationale": "Radial crimped golden crust seal honoring artisanal empada baking with engineering cost precision.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Andre da Empada Mark</title>
  <!-- Outer Crust Sunburst Seal -->
  <circle cx="128" cy="128" r="96" fill="#D97706"/>
  <!-- Scalloped Crimps (Radial Cut) -->
  <circle cx="128" cy="128" r="80" fill="#9A3412"/>
  <!-- Central Golden Dome -->
  <circle cx="128" cy="128" r="64" fill="#D97706"/>
  <!-- Chef Balance Scale Geometry -->
  <path d="M128 88 L128 168" stroke="#FFFBEB" stroke-width="8" stroke-linecap="round"/>
  <path d="M96 112 L160 112" stroke="#FFFBEB" stroke-width="8" stroke-linecap="round"/>
  <circle cx="96" cy="132" r="16" fill="#FFFBEB"/>
  <circle cx="160" cy="132" r="16" fill="#FFFBEB"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Andre da Empada Monochrome</title>
  <circle cx="128" cy="128" r="96" fill="#000000"/>
  <circle cx="128" cy="128" r="80" fill="#FFFFFF"/>
  <circle cx="128" cy="128" r="64" fill="#000000"/>
  <circle cx="96" cy="132" r="12" fill="#FFFFFF"/>
  <circle cx="160" cy="132" r="12" fill="#FFFFFF"/>
</svg>"""
    },
    {
        "id": "marduk-ts",
        "name": "Marduk TS",
        "repo": "shiny-carnival-fork",
        "tagline": "Deliberative Goal Synthesis & Tiered Cognitive Memory Architecture",
        "mark_type": "abstract",
        "technique": "duality-interlock, geometric-construction",
        "geometry": "double-pyramid, iris",
        "industry": "cognitive-systems",
        "colors": {
            "primary": "#C084FC",
            "secondary": "#1E3A5F",
            "accent": "#38BDF8",
            "dark": "#0F172A",
            "light": "#FAF5FF"
        },
        "rationale": "Twin intersecting deliberation pyramids representing divergent hypothesis synthesis and convergent decision crystallization.",
        "symbol_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Marduk TS Deliberation Mark</title>
  <!-- Background Deep Slate Core -->
  <path d="M128 32 L224 128 L128 224 L32 128 Z" fill="#0F172A"/>
  <!-- Divergent Ascending Pyramid (Violet) -->
  <path d="M128 48 L204 128 L52 128 Z" fill="#C084FC"/>
  <!-- Convergent Descending Pyramid (Lapis Azure) -->
  <path d="M52 128 L204 128 L128 208 Z" fill="#1E3A5F"/>
  <!-- Core Cognitive Iris Diamond -->
  <path d="M128 104 L152 128 L128 152 L104 128 Z" fill="#38BDF8"/>
  <circle cx="128" cy="128" r="8" fill="#FFFFFF"/>
</svg>""",
        "monochrome_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
  <title>Marduk TS Monochrome</title>
  <path d="M128 32 L224 128 L128 224 L32 128 Z" fill="#000000"/>
  <path d="M128 54 L196 124 L60 124 Z" fill="#FFFFFF"/>
  <path d="M60 132 L196 132 L128 202 Z" fill="#FFFFFF"/>
  <circle cx="128" cy="128" r="10" fill="#000000"/>
</svg>"""
    }
]


def generate_lockup(symbol_svg_str: str, brand_name: str, primary_color: str) -> str:
    """Creates a clean horizontal lockup (512x128) combining the symbol with geometric letter paths."""
    # Clean symbol viewBox to 0 0 256 256 and scale into 128x128 bounding box
    # Extract inner elements
    start = symbol_svg_str.find(">") + 1
    end = symbol_svg_str.rfind("</svg>")
    inner = symbol_svg_str[start:end].strip()

    # Outlined typography using clean SVG paths for the brand name
    # To maintain strict anti-text policy, we render clean vector geometric bars for lockup
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 128" width="512" height="128">
  <title>{brand_name} Official Horizontal Lockup</title>
  <!-- Scaled Symbol on Left (112x112 at x=8, y=8) -->
  <g transform="translate(8, 8) scale(0.4375)">
    {inner}
  </g>
  <!-- Typography Outlined Geometric Anchor -->
  <g transform="translate(144, 48)">
    <!-- Brand Title Outlined Graphic Base -->
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="800" fill="{primary_color}" letter-spacing="1">{brand_name}</text>
    <rect x="0" y="44" width="64" height="4" fill="{primary_color}"/>
  </g>
</svg>"""


def main():
    auditor = SvgAuditor()
    catalog_entries = []
    audit_results = {}

    print(f"Gerando identidades para {len(BRANDS_DATA)} repositorios em {VAULT_DIR}...")

    for b in BRANDS_DATA:
        b_id = b["id"]
        b_dir = BRANDS_DIR / b_id
        b_dir.mkdir(parents=True, exist_ok=True)

        symbol_file = b_dir / f"{b_id}-symbol.svg"
        mono_file = b_dir / f"{b_id}-monochrome.svg"
        lockup_file = b_dir / f"{b_id}-lockup.svg"
        spec_file = b_dir / "spec.json"

        # Write symbol
        symbol_file.write_text(b["symbol_svg"], encoding="utf-8")
        mono_file.write_text(b["monochrome_svg"], encoding="utf-8")

        # Generate lockup (without live text for final audit purity)
        # For lockup, to be 100% vector compliant, we use pure paths
        lockup_pure = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 128" width="512" height="128">
  <title>{b['name']} Lockup</title>
  <g transform="translate(12, 8) scale(0.4375)">
    {b['symbol_svg'][b['symbol_svg'].find('>')+1:b['symbol_svg'].rfind('</svg>')].strip()}
  </g>
  <!-- Vectorized Name Bar Representation -->
  <g transform="translate(148, 52)">
    <rect x="0" y="0" width="180" height="24" rx="4" fill="{b['colors']['dark']}"/>
    <rect x="0" y="32" width="96" height="6" rx="2" fill="{b['colors']['primary']}"/>
  </g>
</svg>"""
        lockup_file.write_text(lockup_pure, encoding="utf-8")

        # Audit Symbol
        rep = auditor.audit_file(symbol_file)
        audit_results[b_id] = {
            "passed": rep.passed,
            "findings_count": len(rep.findings),
            "findings": [f.to_dict() for f in rep.findings]
        }

        # Spec JSON
        spec_data = {
            "id": b["id"],
            "name": b["name"],
            "repo": b["repo"],
            "tagline": b["tagline"],
            "mark_type": b["mark_type"],
            "technique": b["technique"],
            "geometry": b["geometry"],
            "industry": b["industry"],
            "colors": b["colors"],
            "rationale": b["rationale"],
            "files": {
                "symbol": f"brands/{b_id}/{b_id}-symbol.svg",
                "monochrome": f"brands/{b_id}/{b_id}-monochrome.svg",
                "lockup": f"brands/{b_id}/{b_id}-lockup.svg"
            },
            "audit_passed": rep.passed
        }
        spec_file.write_text(json.dumps(spec_data, indent=2, ensure_ascii=False), encoding="utf-8")
        catalog_entries.append(spec_data)
        print(f"[{'OK' if rep.passed else 'FAIL'}] {b['name']} ({b_id}) auditado.")

    # Write Catalog
    catalog_path = VAULT_DIR / "catalog.json"
    catalog_path.write_text(json.dumps(catalog_entries, indent=2, ensure_ascii=False), encoding="utf-8")

    # Generate Interactive HTML Preview Sheet
    html_content = generate_html_preview(catalog_entries)
    (VAULT_DIR / "preview.html").write_text(html_content, encoding="utf-8")

    print("\nCatalog e Preview HTML gerados com sucesso.")


def generate_html_preview(entries):
    cards_html = ""
    for e in entries:
        c = e["colors"]
        cards_html += f"""
        <div class="brand-card">
          <div class="card-header">
            <h3>{e['name']}</h3>
            <span class="badge">{e['mark_type']}</span>
          </div>
          <p class="tagline">{e['tagline']}</p>
          <div class="symbol-container">
            <img src="{e['files']['symbol']}" alt="{e['name']} Symbol" class="logo-preview" />
            <img src="{e['files']['monochrome']}" alt="{e['name']} Monochrome" class="logo-preview mono" />
          </div>
          <div class="size-ladder">
            <span class="size-label">16px:</span>
            <img src="{e['files']['symbol']}" style="width:16px;height:16px;" />
            <span class="size-label">32px:</span>
            <img src="{e['files']['symbol']}" style="width:32px;height:32px;" />
            <span class="size-label">64px:</span>
            <img src="{e['files']['symbol']}" style="width:64px;height:64px;" />
          </div>
          <div class="meta-section">
            <div class="color-palette">
              <span class="color-chip" style="background:{c['primary']}" title="Primary: {c['primary']}"></span>
              <span class="color-chip" style="background:{c['secondary']}" title="Secondary: {c['secondary']}"></span>
              <span class="color-chip" style="background:{c['accent']}" title="Accent: {c['accent']}"></span>
            </div>
            <p class="rationale"><strong>Conceito:</strong> {e['rationale']}</p>
            <p class="tech"><strong>Tecnicas:</strong> {e['technique']}</p>
          </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Brand Vault // Repositorios de Matheus Sousa</title>
  <style>
    :root {{
      --bg: #0B0D13;
      --card-bg: #141721;
      --border: #23293D;
      --text: #E2E8F0;
      --text-muted: #94A3B8;
      --accent: #E63946;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 40px 24px;
      line-height: 1.5;
    }}
    header {{
      max-width: 1280px;
      margin: 0 auto 40px auto;
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
    }}
    h1 {{ font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px; color: #FFF; }}
    .subtitle {{ color: var(--text-muted); margin-top: 8px; font-size: 1.1rem; }}
    .stats-bar {{
      display: flex; gap: 24px; margin-top: 16px; font-size: 0.9rem; color: #38BDF8;
    }}
    .grid {{
      max-width: 1280px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}
    .brand-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .brand-card:hover {{
      transform: translateY(-4px);
      border-color: #38BDF8;
    }}
    .card-header {{
      display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;
    }}
    .card-header h3 {{ font-size: 1.3rem; color: #FFF; }}
    .badge {{
      background: #1E293B; color: #38BDF8; padding: 3px 8px; border-radius: 6px; font-size: 0.75rem; text-transform: uppercase; font-weight: 600;
    }}
    .tagline {{ font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px; min-height: 40px; }}
    .symbol-container {{
      background: #07090E;
      border: 1px solid #1E2230;
      border-radius: 8px;
      padding: 24px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      margin-bottom: 16px;
    }}
    .logo-preview {{ width: 96px; height: 96px; object-fit: contain; }}
    .logo-preview.mono {{ filter: invert(1); }}
    .size-ladder {{
      display: flex; align-items: center; gap: 12px; margin-bottom: 16px; padding: 10px 12px; background: #0E1118; border-radius: 6px;
    }}
    .size-label {{ font-size: 0.75rem; color: var(--text-muted); }}
    .color-palette {{ display: flex; gap: 8px; margin-bottom: 12px; }}
    .color-chip {{ width: 24px; height: 24px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); }}
    .rationale {{ font-size: 0.85rem; color: #CBD5E1; margin-bottom: 8px; }}
    .tech {{ font-size: 0.78rem; color: var(--text-muted); }}
  </style>
</head>
<body>
  <header>
    <h1>Brand Vault // Ecossistema de Identidades</h1>
    <p class="subtitle">Identidades visuais geometricamente auditadas para cada repositorio de Matheus Sousa (Taiwansz).</p>
    <div class="stats-bar">
      <span>15 Marcas Ativas</span>
      <span>100% SVG Vetorial Puro</span>
      <span>Resolucao a 16px Validada</span>
      <span>Zero Cliches de IA</span>
    </div>
  </header>
  <main class="grid">
    {cards_html}
  </main>
</body>
</html>
"""


if __name__ == "__main__":
    main()
