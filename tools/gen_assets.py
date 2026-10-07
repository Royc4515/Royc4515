"""Generate the themed SVG assets for the GitHub profile README."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
SANS = "'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','SF Mono',Consolas,'Courier New',monospace"
VIOLET, CYAN, MINT = "#a78bfa", "#67e8f9", "#34d399"

PROJECTS = [
    ("card-aside", "Aside", "01", VIOLET,
     ["Browser extension: ask any of six LLM", "providers about the page you're reading."],
     ["JavaScript", "LLM APIs", "Chrome"]),
    ("card-agentcheck", "AgentCheck", "02", CYAN,
     ["Audits a Python AI agent for quality, token", "cost and security, then grades it A-F."],
     ["Python", "pydantic", "LLM-as-judge"]),
    ("card-sommelier", "Gemini Sommelier", "03", CYAN,
     ["Serverless Telegram agent with live Sheets", "inventory and LLM fallback chains."],
     ["Python", "Gemini", "Serverless"]),
    ("card-spikes", "Spike-Theta Locking", "04", VIOLET,
     ["FIR/IIR filtering, Hilbert phase and spike-", "theta phase locking on LFP data."],
     ["Python", "NumPy", "SciPy"]),
    ("card-goat", "Build Your GOAT", "05", VIOLET,
     ["TikTok-style NBA GOAT-builder web game,", "zero dependencies."],
     ["TypeScript", "vanilla JS"]),
    ("card-cognitive", "Cognitive Outcomes", "06", CYAN,
     ["Socio-educational predictors of children's", "cognitive outcomes, OLS regression."],
     ["Python", "Pandas", "SciPy"]),
]


def card(name, title, num, accent, lines, tags):
    w, h = 580, 230
    desc = "".join(
        f'<text x="32" y="{120 + i * 26}" font-family="{SANS}" font-size="17" fill="#a1a1aa">{escape(t)}</text>'
        for i, t in enumerate(lines))
    x, pills = 32, []
    for t in tags:
        tw = 14 + len(t) * 8.6
        pills.append(
            f'<rect x="{x}" y="176" width="{tw:.0f}" height="28" rx="14" fill="{accent}" fill-opacity="0.1" '
            f'stroke="{accent}" stroke-opacity="0.35"/>'
            f'<text x="{x + tw / 2:.0f}" y="195" text-anchor="middle" font-family="{MONO}" font-size="13" '
            f'fill="{accent}">{escape(t)}</text>')
        x += tw + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b0a14"/><stop offset="1" stop-color="#110e22"/></linearGradient>
    <radialGradient id="glow" cx="1" cy="0" r="0.9"><stop offset="0" stop-color="{accent}" stop-opacity="0.28"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
    <style>.blink{{animation:b 2s ease-in-out infinite}}@keyframes b{{50%{{opacity:.3}}}}</style>
  </defs>
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="url(#bg)" stroke="#ffffff" stroke-opacity="0.09"/>
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="url(#glow)"/>
  <rect x="32" y="28" width="120" height="3" rx="1.5" fill="url(#bar)"/>
  <text x="32" y="58" font-family="{MONO}" font-size="13" fill="#52525b">{num} /</text>
  <circle class="blink" cx="{w - 40}" cy="54" r="5" fill="{accent}"/>
  <text x="32" y="90" font-family="{SANS}" font-size="30" font-weight="800" letter-spacing="-0.8" fill="#fafafa">{escape(title)}</text>
  <text x="{w - 32}" y="90" text-anchor="end" font-family="{SANS}" font-size="22" fill="{accent}">↗</text>
  {desc}
  {''.join(pills)}
</svg>
'''


def header(label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="64" viewBox="0 0 1200 64" role="img" aria-label="{escape(label)}">
  <defs><linearGradient id="l" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.7"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient></defs>
  <text x="2" y="40" font-family="{MONO}" font-size="22" fill="#52525b">//</text>
  <text x="38" y="40" font-family="{MONO}" font-size="22" font-weight="700" fill="#e4e4e7">{escape(label)}</text>
  <rect x="{58 + len(label) * 13.5:.0f}" y="32" width="{1140 - 58 - len(label) * 13.5:.0f}" height="1.5" fill="url(#l)"/>
</svg>
'''


def terminal():
    rows = [
        ("const", " roy", " = {", None),
        ("  studies", ":", ' "CS + Neuroscience @ Bar-Ilan University",', None),
        ("  focus", ":", ' ["AI agents", "LLM tooling", "MCP", "Python backends"],', None),
        ("  daily", ":", ' ["Claude Code", "MCP servers", "multi-provider LLM APIs"],', None),
        ("  curious", ":", ' "where software meets the brain",', None),
        ("  lookingFor", ":", ' "student role · AI / LLM / backend engineering",', None),
        ("}", "", ";", None),
    ]
    body = []
    for i, (a, b, c, _) in enumerate(rows):
        y = 104 + i * 32
        ln = f'<text x="36" y="{y}" font-family="{MONO}" font-size="16" fill="#3f3f46">{i + 1}</text>'
        if i == 0:
            txt = (f'<tspan fill="{VIOLET}">const</tspan><tspan fill="#fafafa"> roy</tspan>'
                   f'<tspan fill="#71717a"> = {{</tspan>')
        elif i == len(rows) - 1:
            txt = '<tspan fill="#71717a">};</tspan><tspan class="caret" fill="#67e8f9"> ▍</tspan>'
        else:
            txt = (f'<tspan fill="{CYAN}">{escape(a)}</tspan><tspan fill="#71717a">{b}</tspan>'
                   f'<tspan fill="#d4d4d8">{escape(c)}</tspan>')
        body.append(ln + f'<text x="76" y="{y}" font-family="{MONO}" font-size="16" xml:space="preserve">{txt}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="350" viewBox="0 0 1200 350" role="img" aria-label="About Roy: CS + Neuroscience student building AI agents, looking for a student role">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b0a14"/><stop offset="1" stop-color="#0f0c1f"/></linearGradient>
    <radialGradient id="g" cx="0.95" cy="1" r="0.6"><stop offset="0" stop-color="{CYAN}" stop-opacity="0.16"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
    <style>.caret{{animation:c 1s steps(1) infinite}}@keyframes c{{50%{{opacity:0}}}}</style>
  </defs>
  <rect x="1" y="1" width="1198" height="348" rx="18" fill="url(#bg)" stroke="#ffffff" stroke-opacity="0.09"/>
  <rect x="1" y="1" width="1198" height="348" rx="18" fill="url(#g)"/>
  <rect x="1" y="1" width="1198" height="50" rx="18" fill="#ffffff" fill-opacity="0.03"/>
  <line x1="1" y1="51" x2="1199" y2="51" stroke="#ffffff" stroke-opacity="0.07"/>
  <circle cx="34" cy="26" r="7" fill="#ff5f57"/><circle cx="58" cy="26" r="7" fill="#febc2e"/><circle cx="82" cy="26" r="7" fill="#28c840"/>
  <text x="600" y="31" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#71717a">~/roy/about.ts</text>
  <rect x="1060" y="14" width="116" height="24" rx="12" fill="{MINT}" fill-opacity="0.1" stroke="{MINT}" stroke-opacity="0.35"/>
  <text x="1118" y="31" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{MINT}">● available</text>
  {''.join(body)}
</svg>
'''


def main():
    OUT.mkdir(exist_ok=True)
    for name, *rest in PROJECTS:
        (OUT / f"{name}.svg").write_text(card(name, *rest), encoding="utf-8")
    for slug, label in [("h-about", "about"), ("h-featured", "featured work"), ("h-stack", "stack")]:
        (OUT / f"{slug}.svg").write_text(header(label), encoding="utf-8")
    (OUT / "terminal.svg").write_text(terminal(), encoding="utf-8")


if __name__ == "__main__":
    main()
