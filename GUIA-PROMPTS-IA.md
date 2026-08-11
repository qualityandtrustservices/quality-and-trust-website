# Pacote Visual — Limpeza de Airbnb com Vista pro Mar
### Adaptação do guia "Assam Honey" (AutomationX) para turnover de temporada à beira-mar

---

## O posicionamento

Você não vende faxina. Você vende **o intervalo invisível entre um hóspede e o próximo**.

O anfitrião não está comprando limpeza — está comprando a nota 5 estrelas, o "estava impecável" na review, a tranquilidade de não precisar ir até o apartamento entre um check-out e um check-in no mesmo dia.

E o mar faz o trabalho pesado da imagem: ele é o cenário que todo apartamento de temporada litorânea tem, e é o que faz o visual parecer caro sem custar nada.

**A frase que o site inteiro sustenta:**
> *Do check-out ao check-in. Impecável, e o mar te esperando.*

---

## Antes de começar — 4 regras que não podem ser quebradas

**1. Gere as imagens EM ORDEM.** Da imagem 2 em diante, suba a anterior como referência. É isso — e só isso — que mantém iluminação, ângulo e composição idênticos entre os quadros. Se quebrar a corrente, o vídeo não anima suavemente.

**2. Prompts em inglês.** *Fato:* os modelos são treinados majoritariamente em inglês e a aderência ao prompt é mensuravelmente melhor. Copie exatamente como está, incluindo os finais `no text, no watermarks`.

**3. Câmera absolutamente travada.** A história não gira em torno de um objeto — gira em torno de **um mesmo ambiente com o mar ao fundo**. A câmera nunca se move. É a luz, a ordem e o mar que evoluem.

**4. Sem rostos.** Mãos, sim. Rostos, não. IA erra rosto e derruba a credibilidade de um site de serviço na hora.

---

## O ritual, contado pelo scroll

No guia do mel: *favo → mel escorre → jarra → colher → mãos*.

Aqui, o **turnover**:

> check-out (o rastro do hóspede) → a cortina abre e o mar aparece → água e espuma → a metade exata → superfície impecável, mar refletido → luz dourada inunda → pronto para o próximo hóspede

---

## PASSO 1 — As 7 imagens-chave do hero

**Linguagem visual compartilhada (em todos os prompts):** mesma sala de estar de apartamento de temporada, mesma câmera fixa em plano aberto na altura dos olhos, parede inteira de vidro à esquerda dando para uma varanda e o mar aberto ao fundo, fotografia arquitetônica de interiores ultra fotorrealista 8K, sem pessoas, sem texto, sem marca d'água.

A luz e o mar são os personagens: começam **cinza, opacos, quase apagados** e terminam **dourados, nítidos, abertos**.

---

### Imagem 1 — O Check-out
`image-1-checkout.png` · **referência: nenhuma**

```
A wide interior shot of a coastal vacation rental living room, shot from a fixed camera
at eye level, an entire glass wall on the left opening onto a balcony with the open sea
beyond, the sheer curtain half drawn so the ocean is dim and washed out, flat grey
overcast morning light, the apartment visibly just vacated — crumpled cushions thrown
across the sofa, a rumpled throw blanket half on the floor, used glasses and an open
snack packet on the coffee table, a suitcase strap trailing off frame, sand scattered
across the floor near the balcony door, salt haze dulling the glass, muted desaturated
colors, low contrast, ultra photorealistic 8K architectural interior photography,
cinematic, no people, no text, no labels, no watermarks
```

---

### Imagem 2 — O Mar Aparece
`image-2-mar-aparece.png` · **referência: image-1**

```
The exact same room from the exact same fixed camera position, the sheer curtain now
drawn fully open, revealing the full glass wall and the open sea beyond for the first
time, a soft shaft of pale daylight entering and cutting across the room, fine dust and
salt particles suspended in the air and catching that light, the ocean still hazy and
low contrast through the dirty glass, the room itself still cluttered and unchanged, the
contrast between the bright window and the dim interior growing, ultra photorealistic 8K
architectural interior photography, cinematic, no people, no text, no labels, no
watermarks
```

---

### Imagem 3 — A Água Chega
`image-3-agua-chega.png` · **referência: image-2**

```
The exact same room from the exact same fixed camera position, the same open glass wall
and sea beyond, now a scattering of fresh water droplets and delicate white foam bubbles
appearing across the coffee table and the lower glass panel in the foreground, the
droplets catching the daylight and glinting, faint steam rising, the clutter beginning to
disappear from the frame, the room behind still dim and unchanged, ultra photorealistic
8K architectural interior photography, cinematic macro detail on the foam, no people, no
text, no labels, no watermarks
```

---

### Imagem 4 — A Metade Exata
`image-4-metade.png` · **referência: image-3**

```
The exact same room from the exact same fixed camera position, the entire glass wall now
split precisely down the middle — the left half cleaned to perfect transparency, the
ocean beyond it sharp, vivid, deep blue and full of contrast, the right half still
clouded with salt haze and streaks, the sea behind it pale and washed out and blurred,
a clean wet edge separating the two halves with a few remaining foam bubbles along that
line, the difference between the two seas unmistakable, ultra photorealistic 8K
architectural interior photography, cinematic, no people, no text, no labels, no
watermarks
```

> **Este é o frame que vende o serviço inteiro.** É o único momento em que o visitante vê o antes e o depois na mesma imagem — e a diferença não está no chão, está *no mar*. Um lado é um mar sem graça, o outro é o mar do anúncio. Se algum frame merecer ser regerado dez vezes até ficar perfeito, é este.

---

### Imagem 5 — Vidro Impecável
`image-5-vidro-impecavel.png` · **referência: image-4**

```
The exact same room from the exact same fixed camera position, the entire glass wall now
flawlessly clean and completely transparent, the open sea beyond it sharp and saturated
from edge to edge with visible wave texture and depth, no streaks, no salt haze, no dust,
the floor spotless and glossy and reflecting the ocean light, the room cleared of all
clutter, the air crystal clear, the light warming from cold grey toward pale gold, ultra
photorealistic 8K architectural interior photography, cinematic, no people, no text, no
labels, no watermarks
```

---

### Imagem 6 — A Luz Dourada
`image-6-luz-dourada.png` · **referência: image-5**

```
The exact same room from the exact same fixed camera position, warm golden late-afternoon
sunlight now flooding through the spotless glass wall and filling the entire room, the
sea beyond glowing with a long band of golden reflection running toward the horizon, long
soft shadows stretching across the polished floor, every surface bright and reflective
and saturated, the whole space transformed and luminous, rich warm color grading, ultra
photorealistic 8K architectural interior photography, cinematic, no people, no text, no
labels, no watermarks
```

---

### Imagem 7 — Pronto para o Próximo Hóspede
`image-7-pronto.png` · **referência: image-6**

```
The exact same room from the exact same fixed camera position, bathed in warm golden light
with the glowing sea beyond, now perfectly styled for arrival — cushions arranged with
hotel precision, a throw blanket folded into a crisp band across the sofa arm, two white
towels rolled and stacked neatly on the coffee table with a small sprig of fresh
greenery placed on top, a simple vase of white flowers, a single wisp of steam rising
from a ceramic mug, a folded welcome note standing blank on the table, everything in
quiet hotel-grade order, the space calm and ready and inviting, warm inviting color
grading, ultra photorealistic 8K architectural interior photography, cinematic, no people,
no text, no labels, no watermarks
```

---

## PASSO 2 — Os 6 clipes de vídeo

Gere **um por vez** (enfileirar os seis derruba a qualidade). Cada clipe usa uma imagem como **frame inicial** e a próxima como **frame final**. De 3 a 5 segundos cada.

| Clipe | Início | Fim | Salvar como |
|:---|:---|:---|:---|
| 1 | image-1 | image-2 | `v1-checkout-para-mar.mp4` |
| 2 | image-2 | image-3 | `v2-mar-para-agua.mp4` |
| 3 | image-3 | image-4 | `v3-agua-para-metade.mp4` |
| 4 | image-4 | image-5 | `v4-metade-para-impecavel.mp4` |
| 5 | image-5 | image-6 | `v5-impecavel-para-dourado.mp4` |
| 6 | image-6 | image-7 | `v6-dourado-para-pronto.mp4` |

---

**Vídeo 1 — O Check-out → O Mar Aparece**
```
Ultra slow motion seamless transformation. A dim cluttered vacation rental living room
under flat grey light, a sheer curtain half covering a glass wall. The curtain slowly
draws fully open, revealing the open sea beyond, and pale daylight grows into the room
in a soft shaft, revealing fine dust and salt particles drifting gently through the air.
Nothing else in the room moves. Camera completely locked, zero movement, no shake, no
cuts, no text, no watermarks.
```

**Vídeo 2 — O Mar → A Água Chega**
```
Ultra slow motion seamless transformation. Dust drifts through daylight in a cluttered
coastal apartment with the sea visible through a hazy glass wall. Fresh water droplets
and delicate white foam bubbles begin appearing across the coffee table and the lower
glass panel, spreading gently and catching the light as they form, faint steam rising.
The clutter begins to fade from the frame. Camera completely locked, zero movement, no
shake, no cuts, no text, no watermarks.
```

**Vídeo 3 — A Água → A Metade Exata**
```
Ultra slow motion seamless transformation. Water and foam sit against a salt-hazed glass
wall overlooking a washed-out sea. An invisible clean wipe travels slowly from left to
right across the glass, lifting the haze away, and the ocean behind the cleaned portion
sharpens dramatically into deep saturated blue while the uncleaned half stays pale and
blurred, the clean edge advancing steadily until exactly half the wall is transformed.
Camera completely locked, zero movement, no shake, no cuts, no text, no watermarks.
```

**Vídeo 4 — A Metade → Vidro Impecável**
```
Ultra slow motion seamless transformation. A glass wall split half crystal clear and half
salt-hazed, the sea sharp on one side and washed out on the other. The clean edge
continues advancing to the right until the entire wall is flawlessly transparent and the
whole ocean snaps into sharp saturated focus from edge to edge, the last foam bubbles
dissolving away, the floor beneath brightening into a glossy reflection, the light
warming subtly from cold grey toward pale gold. Camera completely locked, zero movement,
no shake, no cuts, no text, no watermarks.
```

**Vídeo 5 — Impecável → A Luz Dourada**
```
Ultra slow motion seamless transformation. A spotless coastal apartment with a crystal
clear glass wall and a sharp blue sea beyond. Warm golden late-afternoon sunlight grows
steadily until it floods the entire room, a long band of golden reflection forming across
the water and running toward the horizon, long soft shadows stretching across the polished
floor, colors deepening and saturating. Camera completely locked, zero movement, no shake,
no cuts, no text, no watermarks.
```

**Vídeo 6 — A Luz → Pronto para o Próximo Hóspede**
```
Ultra slow motion seamless transformation. A spotless coastal apartment flooded with warm
golden light, the sea glowing beyond the glass. Cushions settle into hotel-precise
arrangement, a throw blanket folds itself into a crisp band across the sofa arm, two white
towels roll and stack neatly on the coffee table with a sprig of fresh greenery placed on
top, a vase of white flowers comes to rest, and a single wisp of steam begins rising from
a ceramic mug. Everything comes to quiet stillness, the space calm and ready for arrival,
the turnover complete. Camera completely locked, zero movement. Ultra slow motion,
cinematic, photorealistic, no text, no watermarks.
```

---

## PASSO 3 — Juntar os clipes

**Me mande os 6 arquivos e eu junto** — corte exato, sem recompressão dupla. Se preferir fazer você mesmo (Canva ou CapCut):

1. Novo projeto de **Vídeo**
2. Suba os 6 clipes na ordem `v1 → v2 → v3 → v4 → v5 → v6`
3. Em cada emenda: **Sem transição.** Corte seco. Nada de fade ou dissolve
4. Exportar MP4, qualidade máxima
5. Salvar como `turnover-final.mp4`

**Por que corte seco?** O último frame de cada clipe é *exatamente* o primeiro do próximo — foi assim que você gerou. Corte entre dois frames idênticos é invisível. Reproduz como uma tomada única.

---

## PASSO 4 — Extrair os frames (eu faço)

Me mande o `turnover-final.mp4` e eu rodo:

```
ffmpeg -i turnover-final.mp4 -vf "fps=20,scale=960:-1" -q:v 4 frames/frame_%04d.jpg
```

*Confirmado: ffmpeg está instalado aqui.* Resultado: ~600 JPEGs numerados que o site desenha num `<canvas>` conforme você rola a página. **Nunca** scrubbing de `<video>` — o Safari do iPhone estrangula isso e o hero trava.

---

## PASSO 5 — Assets de apoio

### 5a — Os 3 pacotes de serviço
*(equivalem aos 3 potes de mel do guia original)*

Use o primeiro como referência dos outros dois, pro enquadramento e a luz ficarem idênticos.

**TURNOVER** — `pacote-turnover.png` · *referência: nenhuma*
```
A serene coastal vacation rental bedroom in perfect hotel-grade order, bathed in warm
golden afternoon light from a large spotless window with the open sea beyond, crisp white
bed linen pulled taut with sharp hospital corners, two rolled white towels stacked at the
foot of the bed with a sprig of fresh greenery on top, a small vase of white flowers on
the nightstand, spotless glossy floor with soft reflections, calm and inviting, ultra
photorealistic 8K architectural interior photography, no people, no text, no labels, no
watermarks
```

**VIDROS E MARESIA** — `pacote-vidros.png` · *referência: turnover*
```
The same warm golden light quality and photographic style, an extreme close-up of a
balcony glass panel cleaned to complete invisibility, the open sea beyond it razor sharp
and deeply saturated with visible wave texture, the aluminium frame free of salt crust
and corrosion, a few golden light flares crossing the glass, ultra photorealistic 8K
architectural photography, no people, no text, no labels, no watermarks
```

**PROFUNDA PÓS-TEMPORADA** — `pacote-profunda.png` · *referência: turnover*
```
The same warm golden light quality and photographic style, an empty coastal apartment
interior at the end of the season, completely stripped and immaculate — bare polished
floors with no sand anywhere, spotless white walls, air conditioning vents clean and
bright, open kitchen cabinets showing empty spotless shelves, large clean windows with
the sea beyond, the space bright and completely reset, ultra photorealistic 8K
architectural interior photography, no people, no text, no labels, no watermarks
```

---

### 5b — Imagens de atmosfera (2)

**VIDRO E MAR, HORA DOURADA** — `bg-vidro-mar-dourado.png`
```
An extreme close-up of a perfectly clean floor-to-ceiling window pane with warm golden
late-afternoon sunlight streaming through it, the glass so transparent it is almost
invisible, the open sea and a soft bokeh of the horizon beyond, a few dust motes drifting
in the beam, warm amber and deep blue tones, wide atmospheric composition designed as a
luxury scroll website background, ultra photorealistic 8K, no people, no text, no
watermarks
```

**VARANDA, ANOITECER** — `bg-varanda-anoitecer.png`
```
A wide cinematic shot of a spotless coastal apartment balcony at dusk, warm lamp light
glowing softly from inside against deep blue twilight over a calm dark sea, the glass
railing perfectly clear, every surface calm and reflective, distant town lights along
the shoreline, atmospheric and moody, dark luxury editorial feel, ultra photorealistic
8K, no people, no text, no watermarks
```

---

### 5c — Detalhes / lifestyle (3)

**PANO NO VIDRO** — `detalhe-pano-vidro.png`
```
A close-up shot of a folded microfiber cloth gliding across a salt-hazed balcony glass
panel, leaving a perfectly streak-free trail behind it through which the sea appears
suddenly sharp and blue, warm golden light raking across the glass and catching the clean
edge, a human hand holding the cloth with a relaxed grip, only the hand visible, no face,
shallow depth of field, ultra photorealistic 8K editorial photography, no text, no
watermarks
```

**LENÇOL BRANCO** — `detalhe-lencol.png`
```
A close-up of a crisp white bed sheet being pulled taut and settling into place, the
fabric catching warm golden window light with soft folds and clean shadows, two hands
visible at the edges smoothing the surface, no faces, the blurred blue of the sea beyond
the window in the background, luxury hospitality editorial photography, ultra
photorealistic 8K, no text, no watermarks
```

**TOALHAS ENROLADAS** — `detalhe-toalhas.png`
```
An extreme close-up of two pristine white towels rolled tightly and stacked, a single
sprig of fresh green eucalyptus resting on top, warm golden side light raking across the
soft cotton texture, the blurred glow of a sunlit sea in the far background, ultra
detailed, shallow depth of field, luxury hospitality editorial photography, ultra
photorealistic 8K, no text, no watermarks
```

---

### 5d — Os 3 loops dos cards (~4s cada)

Suba a imagem correspondente como **frame inicial** de cada um.

**CLAREZA** — `card-clareza.mp4` · início: `detalhe-pano-vidro.png`
```
Using this image as the start frame, create a slow motion 4-second cinematic loop. The
microfiber cloth continues its smooth glide across the balcony glass, the streak-free
trail widening behind it as the sea beyond snaps into sharp saturated blue and golden
light floods through the newly cleared pane, no camera movement, loop-friendly ending.
```

**ORDEM** — `card-ordem.mp4` · início: `detalhe-lencol.png`
```
Using this image as the start frame, create a slow motion 4-second cinematic loop. The
white bed sheet billows softly upward and settles back down into a perfectly taut
surface, the folds smoothing away, warm golden light sliding across the fabric, no camera
movement, loop-friendly ending.
```

**ENTREGA** — `card-entrega.mp4` · início: `detalhe-toalhas.png`
```
Using this image as the start frame, create a slow motion 4-second cinematic loop. A
slow band of warm golden light travels across the rolled white towels, the cotton texture
lighting up as it passes, the eucalyptus sprig trembling almost imperceptibly, the sea
bokeh shimmering gently in the background, no camera movement, loop-friendly ending.
```

**Comprimir os três:**
```
ffmpeg -i card-clareza-raw.mp4 -vf scale=1280:-1 -movflags faststart \
  -vcodec libx264 -crf 20 -pix_fmt yuv420p -an card-clareza.mp4
```

---

## PASSO 6 — Estrutura de pastas

Minúsculas, hífen (nunca espaço nem underscore).

```
airbnb-vista-mar/
└── public/
    ├── index.html
    ├── frames/
    │   ├── frame_0001.jpg
    │   └── ... até frame_0XXX.jpg
    ├── images/
    │   ├── hero/
    │   │   ├── image-1-checkout.png
    │   │   ├── image-2-mar-aparece.png
    │   │   ├── image-3-agua-chega.png
    │   │   ├── image-4-metade.png
    │   │   ├── image-5-vidro-impecavel.png
    │   │   ├── image-6-luz-dourada.png
    │   │   └── image-7-pronto.png
    │   ├── servicos/
    │   │   ├── pacote-turnover.png
    │   │   ├── pacote-vidros.png
    │   │   └── pacote-profunda.png
    │   ├── backgrounds/
    │   │   ├── bg-vidro-mar-dourado.png
    │   │   └── bg-varanda-anoitecer.png
    │   └── detalhes/
    │       ├── detalhe-pano-vidro.png
    │       ├── detalhe-lencol.png
    │       └── detalhe-toalhas.png
    └── videos/
        ├── card-clareza.mp4
        ├── card-ordem.mp4
        └── card-entrega.mp4
```

**Não organize à mão.** Jogue tudo numa pasta, me mande, e eu separo pela nomenclatura.

---

## Anexo A — Suas fotos reais: como eu melhoro

Me mande o que você já tem. O que consigo fazer de fato, aqui, sem inventar nada:

| O que eu faço | Como |
|:---|:---|
| **Uniformizar a cor** | Aplico a mesma curva quente/dourada em todas, pra suas fotos reais conviverem com as geradas por IA sem parecerem de dois sites diferentes |
| **Aumentar resolução** | Upscale 2x a 4x com preservação de borda, pra foto de celular aguentar tela cheia |
| **Endireitar horizonte** | Crítico em foto com mar. Horizonte torto denuncia amadorismo instantaneamente |
| **Corrigir linhas tortas** | Correção de perspectiva — paredes e janelas voltam a ficar retas |
| **Recortar nos enquadramentos certos** | 16:9 pro hero, 4:5 pro card, 1:1 pro Instagram — do mesmo original |
| **Comprimir pra web** | WebP com qualidade visual preservada. Costuma cair 60–80% do peso |
| **Limpar ruído** | Foto tirada em ambiente escuro fica utilizável |
| **Recortar objeto do fundo** | Se precisar isolar um elemento |

**O que eu NÃO consigo fazer** — e é importante você saber antes de contar com isso:

- **Não consigo gerar imagem nova por IA** nesta sessão. Não tenho a ferramenta. Os prompts acima são pra você rodar no Google Flow / Nano Banana / Veo
- **Não consigo inventar detalhe que não está na foto.** Upscale recupera nitidez, não cria informação que o sensor não capturou. Se a foto está desfocada, ela continua desfocada — só maior
- **Não consigo baixar imagens da internet.** Restrição do ambiente, não é limitação técnica minha

---

## Anexo B — Onde achar mais imagens de graça

Como não posso baixar por você, aqui estão as fontes e os **termos exatos de busca** que funcionam. Todas são gratuitas e liberadas para uso comercial — *mas confirme a licença de cada foto antes de publicar, porque as plataformas mudam os termos e eu não tenho como verificar em tempo real.*

**Unsplash** (unsplash.com) — a melhor para interiores com luz natural
```
ocean view apartment interior
beach house living room
coastal apartment balcony sea
white bed linen hotel window
folded white towels hotel
airbnb beach apartment
```

**Pexels** (pexels.com) — melhor acervo de vídeo gratuito, útil pros loops dos cards
```
beach apartment interior
sea view window
hotel room clean
ocean balcony
```

**Pixabay** (pixabay.com) — acervo menor, mas às vezes tem ângulo que os outros não têm

**Termos que trazem os melhores resultados nesse nicho** (testados como padrão de busca, não como garantia):

| Você quer | Busque por |
|:---|:---|
| Hero com mar | `ocean view living room floor to ceiling window` |
| Quarto pronto | `hotel bed made white linen sea view` |
| Varanda | `apartment balcony ocean sunset` |
| Detalhe de toalha | `rolled towels spa` |
| Vidro limpo | `clean window glass reflection sea` |
| Atmosfera anoitecer | `coastal apartment dusk interior lights` |

**Regra de curadoria:** baixe só o que tem **luz natural quente e lateral**. Descarte tudo que tem luz de teto branca e dura — não vai casar com a linguagem visual do site e você vai perceber tarde demais.

**Um alerta honesto:** foto de banco de imagens tem um problema real em serviço local — o cliente reconhece que não é o seu trabalho. Estimativa minha, baseada em como esse setor costuma funcionar: use banco de imagens para **atmosfera e fundo**, e use foto real sua para **prova de trabalho**. Uma foto de celular do apartamento que você realmente entregou, bem tratada, converte mais que a melhor foto do Unsplash.

---

## O que mudou em relação ao guia original — e por quê

| Guia Assam Honey | Aqui | Motivo |
|:---|:---|:---|
| Fundo preto puro | Ambiente real com mar ao fundo | Turnover de temporada vende **claridade e vista**. Fundo preto venderia mistério |
| Objeto herói centralizado | Ambiente inteiro, câmera fixa | A transformação precisa de contexto espacial pra ser lida |
| 7 estados do mel | 7 estados do turnover | Mesma técnica de encadeamento, narrativa diferente |
| Frame 4: metade do pote | **Frame 4: metade do vidro** | O golpe de mestre da adaptação — a diferença não aparece no móvel, aparece *no mar* |
| Newsletter no final | Orçamento + WhatsApp + nº de imóveis | Anfitrião decide rápido e pelo celular |
| Sem fallback mobile | Fallback estático obrigatório | ~600 frames pesam de 15 a 40 MB, e o anfitrião abre seu site do celular, muitas vezes fora de casa |

---

*Adaptação do guia AutomationX "Assam Honey — Free Tools Edition", Build Guide Series No. 01, para o nicho de limpeza de imóveis de temporada litorâneos.*
