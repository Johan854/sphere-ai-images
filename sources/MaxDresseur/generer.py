# Max, soigneur de dinosaures (personnage original) + bébé tricératops "Pico"
SKIN="#f2c29b"; SKIN_D="#d99e74"; HAT="#c9a46a"; HAT_D="#9c7a45"; BAND="#6b4a2b"
SHIRT="#5f8f4e"; SHIRT_D="#46703a"; SCARF="#f08a3c"; HAIR="#7a4a26"
DINO="#7cc576"; DINO_D="#4f9a4a"; FRILL="#f2b84b"; HORN="#fff4d6"; OL="#2b2118"

def eyes(kind):
    L,R=(94,112),(126,112)
    if kind=="open":   return "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="6.5" fill="{OL}"/><circle cx="{x+1.8}" cy="{y-2.2}" r="1.8" fill="#fff"/>' for x,y in (L,R))
    if kind=="wide":   return "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="7.5" fill="{OL}"/><circle cx="{x+2}" cy="{y-2.5}" r="2.2" fill="#fff"/>' for x,y in (L,R))
    if kind=="up":     return "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="6.5" fill="#fff" stroke="{OL}" stroke-width="1.5"/><circle cx="{x+2}" cy="{y-3}" r="3.3" fill="{OL}"/>' for x,y in (L,R))
    if kind=="happy":  return "".join(f'<path d="M{x-6} {y+2} Q{x} {y-7} {x+6} {y+2}" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>' for x,y in (L,R))
    if kind=="dizzy":  return "".join(f'<path d="M{x-5} {y-5} L{x+5} {y+5} M{x+5} {y-5} L{x-5} {y+5}" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>' for x,y in (L,R))
    if kind=="closed": return "".join(f'<path d="M{x-6} {y} Q{x} {y+5} {x+6} {y}" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>' for x,y in (L,R))
def brows(kind):
    if kind=="up":    return f'<path d="M87 99 Q94 94 101 98 M119 98 Q126 94 133 99" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"/>'
    if kind=="worry": return f'<path d="M87 101 Q94 96 101 98 M119 98 Q126 96 133 101" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"/>'
    if kind=="think": return f'<path d="M87 100 Q94 98 101 100 M119 96 Q126 91 133 95" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"/>'
    return f'<path d="M88 101 Q94 98 100 100 M120 100 Q126 98 132 101" fill="none" stroke="{HAIR}" stroke-width="3" stroke-linecap="round"/>'
def mouth(kind):
    if kind=="smile": return f'<path d="M98 131 Q110 142 122 131" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>'
    if kind=="grin":  return f'<path d="M96 129 Q110 147 124 129 Z" fill="#7a2e22" stroke="{OL}" stroke-width="2.2" stroke-linejoin="round"/><path d="M100 131 L120 131 L118 135 L102 135Z" fill="#fff"/>'
    if kind=="talk":  return f'<ellipse cx="110" cy="134" rx="8" ry="7" fill="#7a2e22" stroke="{OL}" stroke-width="2.2"/><ellipse cx="110" cy="138" rx="4.5" ry="2.5" fill="#e8786a"/>'
    if kind=="o":     return f'<ellipse cx="110" cy="134" rx="4.5" ry="5.5" fill="#7a2e22" stroke="{OL}" stroke-width="2"/>'
    if kind=="hmm":   return f'<path d="M102 134 Q110 131 119 135" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>'
    if kind=="wavy":  return f'<path d="M99 135 Q103 131 107 135 T115 135 T123 135" fill="none" stroke="{OL}" stroke-width="2.6" stroke-linecap="round"/>'
    if kind=="shh":   return f'<path d="M103 134 Q110 131 117 134" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>'

def body():
    return f'''
  <path d="M52 240 Q54 178 92 166 L128 166 Q166 178 168 240 Z" fill="{SHIRT}" stroke="{OL}" stroke-width="2.5"/>
  <path d="M110 168 L110 240" stroke="{SHIRT_D}" stroke-width="2"/>
  <rect x="70" y="190" width="22" height="16" rx="3" fill="{SHIRT_D}" stroke="{OL}" stroke-width="1.6"/>
  <rect x="128" y="190" width="22" height="16" rx="3" fill="{SHIRT_D}" stroke="{OL}" stroke-width="1.6"/>
  <path d="M88 160 Q110 182 132 160 L128 172 Q110 186 92 172 Z" fill="{SCARF}" stroke="{OL}" stroke-width="2"/>
  <rect x="99" y="146" width="22" height="18" fill="{SKIN_D}"/>'''
def head(e,b,m,blush=True):
    return f'''
  <ellipse cx="62" cy="116" rx="7" ry="10" fill="{SKIN}" stroke="{OL}" stroke-width="2.2"/>
  <ellipse cx="158" cy="116" rx="7" ry="10" fill="{SKIN}" stroke="{OL}" stroke-width="2.2"/>
  <ellipse cx="110" cy="114" rx="46" ry="44" fill="{SKIN}" stroke="{OL}" stroke-width="2.5"/>
  <path d="M66 98 Q70 80 92 80 L82 92 Q92 84 104 86 L98 94 Q116 84 132 88 Q150 84 154 98 Q140 90 128 94 Q112 88 96 96 Q80 92 66 98Z" fill="{HAIR}"/>
  {'<ellipse cx="84" cy="126" rx="7" ry="4.5" fill="#f19a8a" opacity=".55"/><ellipse cx="136" cy="126" rx="7" ry="4.5" fill="#f19a8a" opacity=".55"/>' if blush else ''}
  <path d="M106 118 Q110 124 114 118" fill="none" stroke="{SKIN_D}" stroke-width="2.4" stroke-linecap="round"/>
  {brows(b)}{eyes(e)}{mouth(m)}
  <ellipse cx="110" cy="80" rx="64" ry="13" fill="{HAT}" stroke="{OL}" stroke-width="2.5"/>
  <path d="M74 80 Q76 46 110 44 Q144 46 146 80 Z" fill="{HAT}" stroke="{OL}" stroke-width="2.5"/>
  <path d="M100 47 Q110 58 120 47" fill="none" stroke="{HAT_D}" stroke-width="2"/>
  <path d="M75 72 Q110 80 145 72 L146 80 Q110 88 74 80Z" fill="{BAND}"/>
  <path d="M132 66 l7 -3 l3 7 l-7 3z" fill="{FRILL}" stroke="{OL}" stroke-width="1.2"/>'''

def dino(state="happy", dx=-16, dy=-2):
    eye = {"happy":f'<path d="M185 170 Q190 164 195 170" fill="none" stroke="{OL}" stroke-width="2.6" stroke-linecap="round"/>',
           "open":f'<circle cx="190" cy="169" r="4" fill="{OL}"/><circle cx="191.5" cy="167.5" r="1.4" fill="#fff"/>',
           "dizzy":f'<path d="M186 165 l8 8 m0 -8 l-8 8" stroke="{OL}" stroke-width="2.4" stroke-linecap="round"/>',
           "sleep":f'<path d="M185 169 Q190 173 195 169" fill="none" stroke="{OL}" stroke-width="2.4" stroke-linecap="round"/>'}[state]
    mouth = f'<path d="M196 186 Q203 190 210 185" fill="none" stroke="{OL}" stroke-width="2.2" stroke-linecap="round"/>' if state!="dizzy" else f'<ellipse cx="203" cy="187" rx="3.5" ry="3" fill="{OL}"/>'
    return f'''<g transform="translate({dx},{dy})">
  <path d="M150 240 Q150 200 170 192 L200 196 Q214 210 212 240Z" fill="{DINO}" stroke="{OL}" stroke-width="2.4"/>
  <path d="M158 158 Q168 128 196 130 Q222 134 226 160 Q214 152 206 156 Q198 146 186 150 Q172 148 158 158Z" fill="{FRILL}" stroke="{OL}" stroke-width="2.4"/>
  <circle cx="176" cy="142" r="3" fill="{DINO_D}"/><circle cx="194" cy="137" r="3" fill="{DINO_D}"/><circle cx="211" cy="143" r="3" fill="{DINO_D}"/>
  <ellipse cx="192" cy="176" rx="30" ry="24" fill="{DINO}" stroke="{OL}" stroke-width="2.4"/>
  <path d="M206 160 L214 140 L216 162Z" fill="{HORN}" stroke="{OL}" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M176 158 L172 140 L184 156Z" fill="{HORN}" stroke="{OL}" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M216 178 L228 172 L220 184Z" fill="{HORN}" stroke="{OL}" stroke-width="1.8" stroke-linejoin="round"/>
  <ellipse cx="180" cy="184" rx="5" ry="3" fill="#f19a8a" opacity=".6"/>
  {eye}{mouth}</g>'''

def svg(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">{inner}</svg>'
def arm(path): return f'<path d="{path}" fill="{SHIRT}" stroke="{OL}" stroke-width="2.4" stroke-linejoin="round"/>'
def hand(x,y,r=9): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" stroke="{OL}" stroke-width="2.2"/>'

S={}
S["idle"]=svg(body()+head("open","normal","smile")+dino("happy"))
S["listening"]=svg(body()+head("wide","up","o")+arm("M60 200 Q44 160 52 130 L66 132 Q62 160 72 190Z")+hand(58,124,10)
   +f'<path d="M36 104 Q28 116 36 128 M26 96 Q14 116 26 136" fill="none" stroke="#4fc3f7" stroke-width="3" stroke-linecap="round"/>'+dino("open"))
S["thinking"]=svg(body()+head("up","think","hmm")+arm("M70 206 Q70 172 98 150 L106 158 Q84 178 84 208Z")+hand(102,150,9)
   +f'<circle cx="160" cy="62" r="4" fill="#fff" stroke="{OL}" stroke-width="1.6"/><circle cx="170" cy="50" r="6" fill="#fff" stroke="{OL}" stroke-width="1.6"/>'
   +f'<circle cx="188" cy="34" r="15" fill="#fff" stroke="{OL}" stroke-width="1.8"/><text x="188" y="41" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="20" fill="{SCARF}">?</text>'+dino("open"))
S["replying"]=svg(body()+head("open","up","talk")+arm("M60 210 Q44 176 30 150 L20 160 Q36 186 48 214Z")+hand(24,152,10)
   +f'<path d="M164 104 L178 98 M166 118 L182 118 M164 132 L178 138" stroke="{SCARF}" stroke-width="3.2" stroke-linecap="round"/>'+dino("happy"))
S["error"]=svg(body()+head("dizzy","worry","wavy",blush=False)+f'<path d="M160 92 Q166 104 160 110 Q154 104 160 92Z" fill="#7fd0ff" stroke="{OL}" stroke-width="1.5"/>'
   +f'<text x="40" y="60" font-family="Arial Black,Arial" font-weight="900" font-size="26" fill="#ff6b5f" stroke="{OL}" stroke-width="1.2">!</text>'+dino("dizzy"))
S["timer_finished"]=svg(body()+head("happy","up","grin")+arm("M60 206 Q42 170 44 136 L58 136 Q58 168 74 198Z")+hand(50,132,10)
   +arm("M160 206 Q178 170 176 136 L162 136 Q162 168 146 198Z")+hand(170,132,10)
   +f'<circle cx="110" cy="24" r="16" fill="#ffd166" stroke="{OL}" stroke-width="2"/><circle cx="110" cy="24" r="11" fill="#fff" stroke="{OL}" stroke-width="1.4"/><path d="M110 24 L110 16 M110 24 L116 27" stroke="{OL}" stroke-width="2" stroke-linecap="round"/>'
   +f'<path d="M86 14 l-8 -6 M134 14 l8 -6 M84 30 l-10 0 M136 30 l10 0" stroke="#ffd166" stroke-width="3" stroke-linecap="round"/>')
S["mute"]=svg(body()+head("closed","normal","shh")+arm("M70 210 Q70 176 98 140 L106 146 Q86 176 84 212Z")+hand(104,140,9)
   +f'<rect x="107" y="114" width="5" height="28" rx="2.5" fill="{SKIN}" stroke="{OL}" stroke-width="1.6"/>'
   +f'<text x="170" y="60" font-family="Arial Black,Arial" font-weight="900" font-size="18" fill="#a9b4ff">z</text><text x="186" y="44" font-family="Arial Black,Arial" font-weight="900" font-size="13" fill="#a9b4ff">z</text>'+dino("sleep"))
# loading : œuf qui éclot + traces de pas
S["loading"]=svg(f'''<g>
  <path d="M120 40 Q160 40 168 110 Q172 170 120 176 Q68 170 72 110 Q80 40 120 40Z" fill="#fff4d6" stroke="{OL}" stroke-width="3"/>
  <circle cx="100" cy="90" r="8" fill="{DINO}" opacity=".6"/><circle cx="140" cy="130" r="10" fill="{DINO}" opacity=".6"/><circle cx="132" cy="70" r="5" fill="{DINO}" opacity=".6"/>
  <path d="M80 112 L94 100 L104 114 L118 98 L130 114 L144 100 L160 112" fill="none" stroke="{OL}" stroke-width="3" stroke-linejoin="round"/>
  <g fill="{SCARF}">{''.join(f'<g transform="translate({x},{y}) rotate({r})"><ellipse cx="0" cy="0" rx="7" ry="9"/><circle cx="-7" cy="-11" r="3"/><circle cx="0" cy="-14" r="3"/><circle cx="7" cy="-11" r="3"/></g>' for x,y,r in ((58,208,-30),(92,216,-10),(128,216,10),(162,208,30)))}</g></g>''')
import os
os.makedirs('svg',exist_ok=True)
for k,v in S.items(): open(f'svg/{k}.svg','w').write(v)
print(list(S))
