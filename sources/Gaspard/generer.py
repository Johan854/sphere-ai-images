# Sire Gaspard, chevalier original (casque rond, plumet rouge, tabard bleu à blason crayon)
OL="#1f2230"; SKIN="#f4c7a1"; SKIND="#dba07a"; STEEL="#c7ced8"; STEELD="#8e99a8"; PLUME="#e8453c"; TAB="#2f6fd6"; TABD="#1f4fa3"; GOLD="#ffcc3d"
def svg(i): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">{i}</svg>'
def body():
    return f'''<path d="M54 240 Q56 182 92 170 L148 170 Q184 182 186 240Z" fill="{STEEL}" stroke="{OL}" stroke-width="2.6"/>
  {''.join(f'<path d="M{x} 182 q6 6 12 0" fill="none" stroke="{STEELD}" stroke-width="2"/>' for x in range(66,174,12))}
  <path d="M84 176 L156 176 L150 240 L90 240Z" fill="{TAB}" stroke="{OL}" stroke-width="2.4"/>
  <path d="M84 176 L156 176 L154 186 L86 186Z" fill="{TABD}"/>
  <path d="M104 196 L136 196 L136 216 Q120 230 104 216Z" fill="{GOLD}" stroke="{OL}" stroke-width="2"/>
  <path d="M112 220 L128 200 L132 204 L116 224 L110 226Z" fill="#fff" stroke="{OL}" stroke-width="1.6"/><path d="M110 226 l2 -4 l3 3z" fill="{OL}"/>
  <ellipse cx="66" cy="184" rx="18" ry="12" fill="{STEEL}" stroke="{OL}" stroke-width="2.4"/><ellipse cx="174" cy="184" rx="18" ry="12" fill="{STEEL}" stroke="{OL}" stroke-width="2.4"/>'''
def helmet_back():
    return f'''<path d="M118 34 Q140 14 166 22 Q150 26 146 36 Q168 34 178 48 Q156 44 146 50Z" fill="{PLUME}" stroke="{OL}" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M64 118 Q60 52 120 46 Q180 52 176 118 L176 152 Q170 168 156 170 L84 170 Q70 168 64 152Z" fill="{STEEL}" stroke="{OL}" stroke-width="2.8"/>
  <path d="M120 46 L120 74" stroke="{STEELD}" stroke-width="3"/>
  <circle cx="72" cy="140" r="3" fill="{STEELD}"/><circle cx="168" cy="140" r="3" fill="{STEELD}"/><circle cx="72" cy="124" r="3" fill="{STEELD}"/><circle cx="168" cy="124" r="3" fill="{STEELD}"/>'''
def face():
    return f'''<path d="M82 92 Q82 80 96 80 L144 80 Q158 80 158 92 L158 140 Q158 162 120 164 Q82 162 82 140Z" fill="{SKIN}" stroke="{OL}" stroke-width="2.4"/>
  <path d="M82 92 Q84 84 92 82 Q104 92 120 86 Q136 92 148 82 Q156 84 158 92" fill="#8a5a33"/>
  <path d="M116 120 Q120 128 124 120" fill="none" stroke="{SKIND}" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M98 140 Q108 146 120 141 Q132 146 142 140 Q132 150 120 146 Q108 150 98 140Z" fill="#8a5a33"/>'''
def visor(): return f'<path d="M74 82 Q120 56 166 82 L162 92 Q120 70 78 92Z" fill="{STEELD}" stroke="{OL}" stroke-width="2.4"/>{"".join(f"<rect x=\'{x}\' y=\'74\' width=\'6\' height=\'3\' rx=\'1\' fill=\'{OL}\'/>" for x in (96,108,126,138))}'
def eyes(k):
    L,R=(104,108),(136,108)
    f={"open":lambda x,y:f'<ellipse cx="{x}" cy="{y}" rx="6" ry="7.5" fill="{OL}"/><circle cx="{x+2}" cy="{y-2.5}" r="2" fill="#fff"/>',
       "wide":lambda x,y:f'<ellipse cx="{x}" cy="{y}" rx="7" ry="8.5" fill="{OL}"/><circle cx="{x+2.2}" cy="{y-3}" r="2.6" fill="#fff"/>',
       "up":lambda x,y:f'<ellipse cx="{x}" cy="{y}" rx="6" ry="7.5" fill="#fff" stroke="{OL}" stroke-width="1.8"/><circle cx="{x+2}" cy="{y-3.5}" r="3.6" fill="{OL}"/>',
       "happy":lambda x,y:f'<path d="M{x-7} {y+2} Q{x} {y-8} {x+7} {y+2}" fill="none" stroke="{OL}" stroke-width="3.2" stroke-linecap="round"/>',
       "closed":lambda x,y:f'<path d="M{x-7} {y} Q{x} {y+6} {x+7} {y}" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>',
       "dizzy":lambda x,y:f'<path d="M{x-6} {y-6} L{x+6} {y+6} M{x+6} {y-6} L{x-6} {y+6}" stroke="{OL}" stroke-width="3.2" stroke-linecap="round"/>'}[k]
    return f(*L)+f(*R)
def brows(k):
    d={"normal":"M96 96 Q104 92 112 95 M128 95 Q136 92 144 96","up":"M96 92 Q104 86 112 90 M128 90 Q136 86 144 92",
       "think":"M96 96 Q104 94 112 96 M128 92 Q136 86 144 90","worry":"M96 94 Q104 90 112 96 M128 96 Q136 90 144 94"}[k]
    return f'<path d="{d}" fill="none" stroke="#6b4426" stroke-width="3.4" stroke-linecap="round"/>'
def mouth(k):
    return {"smile":f'<path d="M106 150 Q120 160 134 150" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>',
            "o":f'<ellipse cx="120" cy="153" rx="5" ry="6" fill="#7a2e22" stroke="{OL}" stroke-width="2"/>',
            "talk":f'<ellipse cx="120" cy="153" rx="9" ry="7.5" fill="#7a2e22" stroke="{OL}" stroke-width="2.2"/><ellipse cx="120" cy="157" rx="5" ry="2.4" fill="#e8786a"/>',
            "hmm":f'<path d="M110 153 Q118 150 130 154" fill="none" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>',
            "wavy":f'<path d="M106 154 Q110 150 114 154 T122 154 T130 154 T138 154" fill="none" stroke="{OL}" stroke-width="2.6" stroke-linecap="round"/>',
            "grin":f'<path d="M104 148 Q120 168 136 148Z" fill="#7a2e22" stroke="{OL}" stroke-width="2.2" stroke-linejoin="round"/><path d="M108 150 L132 150 L130 154 L110 154Z" fill="#fff"/>',
            "shh":f'<path d="M112 154 L128 154" stroke="{OL}" stroke-width="3" stroke-linecap="round"/>'}[k]
def cheeks(): return '<ellipse cx="96" cy="130" rx="7" ry="4.5" fill="#f19a8a" opacity=".55"/><ellipse cx="144" cy="130" rx="7" ry="4.5" fill="#f19a8a" opacity=".55"/>'
def arm(d): return f'<path d="{d}" fill="none" stroke="{OL}" stroke-width="19" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{STEEL}" stroke-width="14" stroke-linecap="round"/>'
def glove(x,y): return f'<circle cx="{x}" cy="{y}" r="10" fill="{STEELD}" stroke="{OL}" stroke-width="2.2"/>'
def char(e,b,m,blush=True): return body()+helmet_back()+face()+visor()+eyes(e)+brows(b)+mouth(m)+(cheeks() if blush else '')
S={}
S["idle"]=svg(char("open","normal","smile"))
S["listening"]=svg(char("wide","up","o")+arm("M60 210 Q42 170 50 134")+glove(52,128)+f'<path d="M30 104 Q22 118 30 132 M18 96 Q6 118 18 140" fill="none" stroke="#7fc8ff" stroke-width="3" stroke-linecap="round"/>')
S["thinking"]=svg(char("up","think","hmm")+arm("M70 214 Q72 178 104 162")+glove(108,160)
   +f'<circle cx="168" cy="70" r="4" fill="#fff"/><circle cx="178" cy="58" r="6" fill="#fff"/><circle cx="192" cy="44" r="13" fill="#fff" stroke="{OL}" stroke-width="1.8"/><text x="192" y="51" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="17" fill="{TAB}">?</text>')
# replying : lève un crayon géant comme une épée
S["replying"]=svg(char("open","up","talk")+f'''<g transform="translate(-24 14) rotate(18 196 120)"><rect x="190" y="40" width="14" height="110" rx="3" fill="{GOLD}" stroke="{OL}" stroke-width="2.2"/>
  <path d="M190 40 L197 22 L204 40Z" fill="{SKIN}" stroke="{OL}" stroke-width="2"/><path d="M195 27 L197 22 L199 27Z" fill="{OL}"/><rect x="190" y="146" width="14" height="10" fill="#ff8fb3" stroke="{OL}" stroke-width="2"/></g>'''
   +arm("M170 214 Q190 176 178 150")+glove(178,148))
S["error"]=svg(char("dizzy","worry","wavy",blush=False)+f'<path d="M150 64 Q158 76 150 84 Q144 76 150 64Z" fill="#7fd0ff" stroke="{OL}" stroke-width="1.5"/>'
   +''.join(f'<path d="M{x} {y-6} L{x+2} {y-2} L{x+6} {y} L{x+2} {y+2} L{x} {y+6} L{x-2} {y+2} L{x-6} {y} L{x-2} {y-2}Z" fill="#ffe08a"/>' for x,y in ((70,52),(96,36),(144,36),(170,52))))
S["timer_finished"]=svg(char("happy","up","grin")+arm("M60 214 Q40 176 46 138")+glove(48,132)+arm("M180 214 Q200 176 194 138")+glove(192,132)
   +f'<path d="M120 4 q16 0 16 16 q-16 0 -16 -16z" fill="none"/><circle cx="120" cy="20" r="14" fill="{GOLD}" stroke="{OL}" stroke-width="2"/><circle cx="120" cy="20" r="9.5" fill="#fff" stroke="{OL}" stroke-width="1.4"/><path d="M120 20 L120 13 M120 20 L125 23" stroke="{OL}" stroke-width="2" stroke-linecap="round"/>'
   +f'<path d="M96 12 l-8 -5 M144 12 l8 -5" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>')
# mute : visière baissée + zZ
S["mute"]=svg(body()+helmet_back()+f'''<path d="M82 92 Q82 80 96 80 L144 80 Q158 80 158 92 L158 140 Q158 162 120 164 Q82 162 82 140Z" fill="{STEELD}" stroke="{OL}" stroke-width="2.6"/>
  {''.join(f'<rect x="92" y="{y}" width="56" height="5" rx="2.5" fill="{OL}"/>' for y in (104,116,128))}
  <text x="170" y="56" font-family="Arial Black,Arial" font-weight="900" font-size="18" fill="#a9b4ff">z</text><text x="186" y="40" font-family="Arial Black,Arial" font-weight="900" font-size="13" fill="#a9b4ff">z</text>''')
S["loading"]=svg(f'''<path d="M60 220 L60 120 L80 120 L80 104 L96 104 L96 120 L112 120 L112 104 L128 104 L128 120 L144 120 L144 104 L160 104 L160 120 L180 120 L180 220Z" fill="{STEEL}" stroke="{OL}" stroke-width="2.6"/>
  <path d="M104 220 L104 178 Q120 160 136 178 L136 220Z" fill="#6b4426" stroke="{OL}" stroke-width="2.4"/>
  <path d="M120 104 L120 40" stroke="{OL}" stroke-width="3"/><path d="M120 42 L156 52 L120 64Z" fill="{PLUME}" stroke="{OL}" stroke-width="2"/>
  <rect x="78" y="146" width="12" height="18" rx="6" fill="{OL}"/><rect x="150" y="146" width="12" height="18" rx="6" fill="{OL}"/>
  {''.join(f'<circle cx="{x}" cy="232" r="4" fill="{GOLD}"/>' for x in (100,120,140))}''')
import os; os.makedirs('svg',exist_ok=True)
for k,v in S.items(): open(f'svg/{k}.svg','w').write(v)
