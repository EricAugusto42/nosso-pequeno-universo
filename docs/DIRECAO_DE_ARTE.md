# Direção de arte (base)
Resolução-base 320×180, escala inteira, `image-rendering: pixelated`. Toda a arte vem de `tools/build_assets.py`
(desenhada pixel a pixel, sem filtros, sem vetores). Rodar de novo regenera `assets/` e `assets/manifest.js`.
Paleta: 28 cores (`assets/reference/paleta.png`). Vermelho = Karollyne (cabelo r1/r3/r4, sem laranja/cobre); âmbar = luz.
Personagens: 26×48 px com contorno, mesma altura; 3 quadros (idle, idle com respiração, piscar).
Karollyne: cabelo longo, liso, vermelho; blusa creme, calça marinho. Eu: cabelo curto escuro, óculos finos, bigode discreto, moletom marinho.
Pastas: sprites/ cenários em scenes/ efeitos em fx/ referências em reference/ (ficha ×6, paleta, prévias). ui/ reservada.
## Próximas tarefas
Vistas de costas e perfil; expressões; sprites caminhando; cenários das fases 1, 6, 7, 8, 9, 10, 11; música (assets/audio/, não incluída);
efeitos sonoros; transições; salvamento local; fotos de referência (não havia nenhuma no projeto).

## Atualização: jogo completo (11 fases)
Cenários: room, city+cityfg, garden, road, sofa+sofafg, final. Poses: costas (eu_b/karollyne_b, andando), pequenas (_bs), entrega (eu_give) e recepção (karollyne_rcv).
Textos em js/content.js, fases e hotspots em js/stages.js, motor em js/engine.js. Regenerar arte: `python3 tools/build_scenes.py`.
Música: assets/audio/nosso-pequeno-universo.mp3 (não incluída).

## Atualização: 16 fases e áudio
Fases novas: Jogadora 1 (ficha), O vermelho é a cor dela (retrato), Nosso ritmo (notas), Conquistas, Jogador 2 (ficha). Palco: assets/scenes/select.png.
Áudio sintetizado em js/engine.js (WebAudio): sons de teclas/espaço/sino da máquina, cliques, notas e trilha chiptune original em loop (~19 s, 100 bpm).
Não há arquivo de música externo; para usar uma trilha própria, substitua a função music() por um <audio>.

## Atualização: aparência baseada nas fotos de referência
Personagens refeitos com tons de pele/cabelo amostrados das fotos (paleta f*/e*/hr*). Ele: mais alto e mais forte (bulk() em build_assets.py), cabelo curto cacheado, óculos sem aro, bigode e barba por fazer.
Ela: cabelo longo, liso e vermelho, pele clara. Retratos 64×80 (her_bust/him_bust) usados na capa e nas fichas; âncoras de cada traço ficam no manifest (campo "a").
Cenários: beach (início, anoitecer), sunset (caminhada), golden (buquê, fim de tarde), capa (tela inicial). Regenerar tudo: `python3 tools/build_v2.py`.
Música: nova trilha 8-bit romântica (92 bpm, 16 compassos, pulso 25% com vibrato, baixo triangular, arpejo suave), sintetizada em js/engine.js.

## Atualização: nova referência oficial (assets/reference/referencia_oficial.png)
Capa: metade esquerda da referência reduzida (÷2) e quantizada em 64 cores (assets/scenes/capa.png), com botão "Toque para começar" sobre o botão da arte.
Personagens: recortados da folha da direita (fundo removido, reduzidos para ~48-50 px, quantizados, contorno de 1 px): frente, costas, perfil, caminhada pequena, entrega do buquê e recebimento (tools/build_ref.py + tools/extract_ref.py).
Retratos e 5 expressões de cada um (face_k / face_e) aparecem nas fichas e na caixa de diálogo. Objetos (máquina, abajur, notebook, gato, caneca, planta) vêm da seção "Elementos do jogo".
Regenerar tudo: `python3 tools/build_ref.py`. Ele também roda build_v2.py (cenários de praia e do palco).
Ele é ~2 px mais alto que ela (aproximadamente a mesma altura).
