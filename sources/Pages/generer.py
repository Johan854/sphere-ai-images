H='<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">'
def wrap(bg, body, extra_bg=''):
    return H+f'<defs><clipPath id="c"><circle cx="120" cy="120" r="120"/></clipPath></defs><g clip-path="url(#c)"><rect width="240" height="240" fill="{bg}"/>{extra_bg}{body}</g></svg>'
eyes=lambda x1,x2,y,r=6:f'<circle cx="{x1}" cy="{y}" r="{r}" fill="#222"/><circle cx="{x2}" cy="{y}" r="{r}" fill="#222"/><circle cx="{x1+2}" cy="{y-2}" r="2" fill="#fff"/><circle cx="{x2+2}" cy="{y-2}" r="2" fill="#fff"/>'
P={}
# 1 Brico
P['brico']=wrap('#E3000B','''
<rect x="60" y="205" width="120" height="40" fill="#B00008"/>
<rect x="88" y="150" width="64" height="62" rx="6" fill="#FFD500" stroke="#C9A800" stroke-width="3"/>
<circle cx="104" cy="170" r="5" fill="#2A6FDB"/><circle cx="120" cy="170" r="5" fill="#27AE60"/><circle cx="136" cy="170" r="5" fill="#E3000B"/>
<rect x="56" y="155" width="30" height="16" rx="4" fill="#FFD500" stroke="#C9A800" stroke-width="3"/>
<rect x="154" y="140" width="16" height="30" rx="4" fill="#FFD500" stroke="#C9A800" stroke-width="3" transform="rotate(-20 162 155)"/>
<g transform="rotate(25 180 118)"><rect x="176" y="100" width="9" height="40" rx="3" fill="#9AA5B1"/><path d="M170 92 a13 13 0 1 0 26 0 l-7 0 l0 8 l-12 0 l0 -8 z" fill="#9AA5B1"/></g>
<rect x="80" y="64" width="80" height="80" rx="8" fill="#2A6FDB" stroke="#1D4E9E" stroke-width="3"/>
<rect x="92" y="48" width="20" height="16" rx="3" fill="#2A6FDB" stroke="#1D4E9E" stroke-width="3"/>
<rect x="128" y="48" width="20" height="16" rx="3" fill="#2A6FDB" stroke="#1D4E9E" stroke-width="3"/>
<rect x="94" y="84" width="52" height="30" rx="6" fill="#E8F1FF"/>
'''+eyes(108,132,98,7)+'''<path d="M106 124 q14 12 28 0" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>''')
# 2 Capitaine Nova
stars=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x,y,r in [(30,60,1.5),(60,30,1),(200,50,2),(180,90,1),(40,140,1),(215,150,1.5),(150,25,1),(90,40,1.2)])
P['nova']=wrap('#0B0B1E','''
<path d="M50 245 q0-60 60-62 l20 0 q60 2 60 62 z" fill="#F07F1A"/>
<rect x="108" y="183" width="24" height="60" fill="#D86A0C"/>
<circle cx="78" cy="205" r="7" fill="#FFE81F"/>
<rect x="110" y="158" width="20" height="28" fill="#F2C29B"/>
<path d="M78 112 q0-58 42-58 q42 0 42 58 l0 30 q-8 8 -14 0 l0-30 l-56 0 l0 30 q-6 8 -14 0 z" fill="#5B3A1E"/>
<ellipse cx="120" cy="120" rx="36" ry="42" fill="#F7D2B0"/>
<path d="M84 104 q36 -38 72 0 q-20 -14 -36 -12 q-18 -2 -36 12z" fill="#5B3A1E"/>
'''+eyes(106,134,120)+'''
<circle cx="98" cy="136" r="6" fill="#F5A3A3" opacity=".6"/><circle cx="142" cy="136" r="6" fill="#F5A3A3" opacity=".6"/>
<path d="M110 142 q10 8 20 0" stroke="#8A3B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
<g><circle cx="182" cy="208" r="26" fill="#EDEDED" stroke="#9AA5B1" stroke-width="3"/><path d="M164 205 a18 14 0 0 1 36 0 z" fill="#3D6FA8" opacity=".8"/></g>
<g><circle cx="196" cy="88" r="20" fill="#D9DEE5" stroke="#8A96A3" stroke-width="3"/><circle cx="196" cy="88" r="8" fill="#2A6FDB"/><circle cx="198" cy="86" r="3" fill="#fff"/><line x1="196" y1="68" x2="196" y2="56" stroke="#8A96A3" stroke-width="3"/><circle cx="196" cy="54" r="4" fill="#FFE81F"/>
<path d="M186 112 l20 0" stroke="#FFE81F" stroke-width="2" stroke-dasharray="3 3"/></g>
''',stars)
# 4 Lila l'exploratrice
P['lila']=wrap('#7A3E00','''
<path d="M58 245 q0-56 52-58 l20 0 q52 2 52 58 z" fill="#2E8B57"/>
<rect x="66" y="196" width="20" height="50" rx="6" fill="#8B5A2B"/>
<rect x="154" y="196" width="20" height="50" rx="6" fill="#8B5A2B"/>
<circle cx="120" cy="222" r="14" fill="#E6C15A" stroke="#8B6914" stroke-width="3"/><path d="M120 212 l4 10 l-4 10 l-4 -10z" fill="#C0392B"/>
<rect x="110" y="160" width="20" height="28" fill="#C68B5E"/>
<path d="M80 128 q-4 -66 40 -66 q44 0 40 66 z" fill="#2B1A10"/>
<ellipse cx="120" cy="126" rx="34" ry="40" fill="#D9A27A"/>
<path d="M86 110 q34 -40 68 -6 q-30 -12 -68 6z" fill="#2B1A10"/>
<path d="M154 120 q18 30 6 70" stroke="#2B1A10" stroke-width="12" fill="none" stroke-linecap="round"/>
'''+eyes(106,134,126)+'''
<path d="M108 146 q12 10 24 0" stroke="#7A2E1E" stroke-width="3" fill="none" stroke-linecap="round"/>
<g transform="translate(56 150)">
<path d="M0 28 q-6 -20 10 -30 q18 -6 22 14 q0 18 -14 22 z" fill="#E74C3C"/>
<path d="M2 30 l-10 22 l12 -8 z" fill="#2A6FDB"/><path d="M8 32 l-2 22 l8 -14 z" fill="#27AE60"/>
<circle cx="18" cy="2" r="12" fill="#E74C3C"/>
<path d="M28 0 q10 4 4 12 q-4 -4 -6 -4z" fill="#F4D03F"/>
<circle cx="20" cy="0" r="3.5" fill="#fff"/><circle cx="21" cy="0" r="2" fill="#222"/>
</g>
<g transform="translate(176 40) rotate(12)"><rect width="46" height="34" rx="3" fill="#F3E2B3" stroke="#B88A3E" stroke-width="2"/><path d="M8 26 q10 -14 18 -6 q8 6 12 -8" stroke="#B88A3E" stroke-width="2" fill="none" stroke-dasharray="3 3"/><path d="M34 6 l6 6 m0 -6 l-6 6" stroke="#C0392B" stroke-width="3"/></g>
''')
# 5 Calculo
P['calculo']=wrap('#2A6FDB','''
<ellipse cx="120" cy="150" rx="66" ry="78" fill="#8B5E3C"/>
<ellipse cx="120" cy="172" rx="42" ry="50" fill="#E9D3B4"/>
<path d="M104 160 l32 32 m0 -32 l-32 32" stroke="#2A6FDB" stroke-width="8" stroke-linecap="round"/>
<path d="M62 74 l14 30 l-26 -6z" fill="#8B5E3C"/><path d="M178 74 l-14 30 l26 -6z" fill="#8B5E3C"/>
<circle cx="96" cy="112" r="26" fill="#fff"/><circle cx="144" cy="112" r="26" fill="#fff"/>
<circle cx="96" cy="112" r="28" fill="none" stroke="#222" stroke-width="5"/><circle cx="144" cy="112" r="28" fill="none" stroke="#222" stroke-width="5"/>
<path d="M124 110 q-4 -6 -8 0" stroke="#222" stroke-width="5" fill="none"/>
<circle cx="98" cy="114" r="11" fill="#222"/><circle cx="142" cy="114" r="11" fill="#222"/>
<circle cx="102" cy="110" r="4" fill="#fff"/><circle cx="146" cy="110" r="4" fill="#fff"/>
<path d="M112 138 l8 14 l8 -14z" fill="#F4A259"/>
<path d="M56 160 q-20 30 4 56" stroke="#6E4A2F" stroke-width="16" fill="none" stroke-linecap="round"/>
<path d="M184 160 q20 30 -4 56" stroke="#6E4A2F" stroke-width="16" fill="none" stroke-linecap="round"/>
<path d="M98 226 l-6 12 m8 -12 l0 12 m8 -12 l6 12" stroke="#F4A259" stroke-width="5" stroke-linecap="round"/>
<path d="M134 226 l-6 12 m8 -12 l0 12 m8 -12 l6 12" stroke="#F4A259" stroke-width="5" stroke-linecap="round"/>
''')
# 6 Tic
P['tic']=wrap('#12233F','''
<circle cx="196" cy="56" r="20" fill="#FFD43B"/>
''' + ''.join(f'<line x1="196" y1="56" x2="{196+34*__import__("math").cos(a*0.785)}" y2="{56+34*__import__("math").sin(a*0.785)}" stroke="#FFD43B" stroke-width="3" stroke-dasharray="0 22 12"/>' for a in range(8)) + '''
<path d="M70 70 a26 26 0 0 1 40 -16 z" fill="#C0392B"/><path d="M170 70 a26 26 0 0 0 -40 -16 z" fill="#C0392B"/>
<path d="M88 200 l-14 24 m78 -24 l14 24" stroke="#9AA5B1" stroke-width="8" stroke-linecap="round"/>
<circle cx="120" cy="134" r="72" fill="#E74C3C"/>
<circle cx="120" cy="134" r="58" fill="#FFF8EE"/>
''' + ''.join(f'<circle cx="{120+50*__import__("math").sin(i*0.5236)}" cy="{134-50*__import__("math").cos(i*0.5236)}" r="2.5" fill="#999"/>' for i in range(12)) + eyes(104,136,124) + '''
<circle cx="96" cy="142" r="6" fill="#F5A3A3" opacity=".7"/><circle cx="144" cy="142" r="6" fill="#F5A3A3" opacity=".7"/>
<path d="M108 148 q12 12 24 0" stroke="#7A2E1E" stroke-width="3" fill="none" stroke-linecap="round"/>
<line x1="120" y1="134" x2="120" y2="96" stroke="#333" stroke-width="3" stroke-linecap="round" opacity=".35"/>
<path d="M50 140 q-22 -10 -18 -36" stroke="#E74C3C" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="32" cy="102" r="8" fill="#fff"/>
<path d="M190 140 q22 10 18 36" stroke="#E74C3C" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="208" cy="178" r="8" fill="#fff"/>
''')
for k,v in P.items(): open(k+".svg","w").write(v)

# 7 Pixel (Minecraft) - explorateur en blocs, design original
px=''
import random
random.seed(3)
for gx in range(0,240,20):
    for gy in range(200,240,20):
        c=random.choice(['#6B4423','#7A4F2A','#5E3B1E'])
        px+=f'<rect x="{gx}" y="{gy}" width="20" height="20" fill="{c}"/>'
for gx in range(0,240,20):
    c=random.choice(['#4CAF50','#5DBB3F','#3E9A3A'])
    px+=f'<rect x="{gx}" y="190" width="20" height="12" fill="{c}"/>'
P['pixel']=wrap('#3B7D23','''
<rect x="20" y="40" width="20" height="20" fill="#8BD3FF" opacity=".25"/><rect x="190" y="70" width="20" height="20" fill="#8BD3FF" opacity=".25"/>
<rect x="96" y="180" width="20" height="30" fill="#4A4A8A"/><rect x="124" y="180" width="20" height="30" fill="#4A4A8A"/>
<rect x="88" y="126" width="64" height="58" fill="#E07B24"/>
<rect x="88" y="126" width="64" height="10" fill="#C2621A"/>
<rect x="114" y="140" width="12" height="12" fill="#FFD43B"/>
<rect x="64" y="128" width="22" height="48" fill="#E07B24"/><rect x="64" y="168" width="22" height="12" fill="#E8B48A"/>
<rect x="154" y="128" width="22" height="48" fill="#E07B24"/><rect x="154" y="168" width="22" height="12" fill="#E8B48A"/>
<g transform="rotate(-35 172 150)"><rect x="168" y="112" width="8" height="56" fill="#8B5A2B"/><rect x="150" y="104" width="44" height="12" fill="#5ED3E0"/><rect x="146" y="108" width="8" height="10" fill="#5ED3E0"/><rect x="190" y="108" width="8" height="10" fill="#5ED3E0"/></g>
<rect x="84" y="62" width="72" height="66" fill="#E8B48A"/>
<rect x="84" y="50" width="72" height="22" fill="#F2C230"/>
<rect x="80" y="66" width="80" height="8" fill="#D9A520"/>
<rect x="111" y="52" width="18" height="14" fill="#FFF7B0"/><rect x="114" y="55" width="12" height="8" fill="#FFFFFF"/>
<rect x="98" y="88" width="14" height="14" fill="#fff"/><rect x="104" y="92" width="8" height="10" fill="#2B2B2B"/>
<rect x="128" y="88" width="14" height="14" fill="#fff"/><rect x="128" y="92" width="8" height="10" fill="#2B2B2B"/>
<rect x="106" y="112" width="28" height="6" fill="#9B5A3C"/><rect x="102" y="108" width="6" height="6" fill="#9B5A3C"/><rect x="132" y="108" width="6" height="6" fill="#9B5A3C"/>
''',px)

# 8 Filou (Chats farceurs)
P['filou']=wrap('#5A2D82','''
<rect x="0" y="188" width="240" height="60" fill="#8B5E3C"/><rect x="0" y="184" width="240" height="8" fill="#A47148"/>
<g transform="rotate(28 196 150)"><path d="M182 132 l28 0 l-4 34 l-20 0 z" fill="#fff" stroke="#ccc" stroke-width="2"/><path d="M210 140 q12 2 8 14 q-4 6 -10 4" stroke="#ccc" stroke-width="4" fill="none"/></g>
<path d="M212 178 q6 8 0 12" stroke="#D9C5A0" stroke-width="4" fill="none" stroke-linecap="round"/>
<text x="196" y="118" font-family="DejaVu Sans" font-weight="bold" font-size="20" fill="#FF9EC7">!</text>
<path d="M60 190 q-40 -20 -20 -70 q6 -10 10 0 q-12 40 18 56" fill="#F28C28" stroke="#C96A12" stroke-width="3"/>
<ellipse cx="112" cy="168" rx="52" ry="34" fill="#F28C28"/>
<ellipse cx="112" cy="180" rx="30" ry="20" fill="#FFE2C2"/>
<rect x="74" y="176" width="16" height="16" rx="8" fill="#F28C28"/><rect x="130" y="176" width="16" height="16" rx="8" fill="#F28C28"/>
<path d="M150 150 q28 -6 40 6" stroke="#F28C28" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="190" cy="157" r="9" fill="#FFE2C2"/>
<path d="M66 82 l8 -36 l26 24 z" fill="#F28C28" stroke="#C96A12" stroke-width="3"/><path d="M74 72 l4 -16 l12 12z" fill="#FF9EC7"/>
<path d="M158 82 l-8 -36 l-26 24 z" fill="#F28C28" stroke="#C96A12" stroke-width="3"/><path d="M150 72 l-4 -16 l-12 12z" fill="#FF9EC7"/>
<ellipse cx="112" cy="102" rx="50" ry="42" fill="#F28C28"/>
<path d="M100 64 l4 14 m8 -16 l0 16 m8 -14 l-4 14" stroke="#C96A12" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="94" cy="98" rx="11" ry="13" fill="#C9F25A"/><ellipse cx="130" cy="98" rx="11" ry="13" fill="#C9F25A"/>
<ellipse cx="96" cy="99" rx="4" ry="9" fill="#222"/><ellipse cx="132" cy="99" rx="4" ry="9" fill="#222"/>
<circle cx="98" cy="94" r="2.5" fill="#fff"/><circle cx="134" cy="94" r="2.5" fill="#fff"/>
<path d="M82 84 l18 6" stroke="#C96A12" stroke-width="4" stroke-linecap="round"/><path d="M142 84 l-18 6" stroke="#C96A12" stroke-width="4" stroke-linecap="round"/>
<path d="M108 114 l4 5 l4 -5z" fill="#E75480"/>
<path d="M98 122 q14 14 30 -2" stroke="#7A2E1E" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M60 112 l26 2 m-26 8 l26 -2 m78 -8 l-26 2 m26 8 l-26 -2" stroke="#fff" stroke-width="2" opacity=".8"/>
''')
for k,v in P.items(): open(k+".svg","w").write(v)
