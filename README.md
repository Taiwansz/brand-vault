# BRAND VAULT — ECOSSISTEMA DE IDENTIDADES VISUAIS

Repositorio central de marcas graficas, simbolos vetoriais e especificacoes de identidade visual para todos os projetos e repositorios de Matheus Sousa dos Santos (Taiwansz).

---

## 1. Principios Construtivos e Axiomas de Engenharia

Toda marca deste repositorio foi construida sob os criterios de conformidade do **Protocolo ThSyr de Identidade Visual**:

1. **Identificador, Nao Explicacao**: O logotipo nao tenta descrever o modelo de negocio; ele ancora a memoria atraves de uma forma geometrica pura, distintiva e memoravel.
2. **Pureza Vetorial Rigorosa (Zero Slop)**:
   - Formato padrao: `viewBox="0 0 256 256"`, proporcao exata 1:1.
   - Banimento total de `<text>` vivo (glifos convertidos em caminhos geometricos).
   - Ausencia absoluta de bitmaps (`<image>`), filtros rasterizados (`<filter>`) ou tags proprietarias.
   - Peso medio por simbolo: entre 500 e 800 bytes.
3. **Teste dos 16 Pixels**: Cada simbolo foi validado para preservar contraste e legibilidade funcional na escala microscopica de favicons e barras de status mobile.
4. **Viabilidade Monocromatica**: Todas as marcas possuem contraparte monocromatica testada para corte a laser, serigrafia e aplicacoes de alto contraste.
5. **Auditoria Algoritmica**: 100% dos simbolos foram submetidos a suite de inspecao do `thsyr logo audit` e aprovados sem falhas estruturais.

---

## 2. Matriz Geral do Acervo (15 Repositorios)

| Marca | Repositorio | Tipo de Marca | Tecnica Primaria | Geometria | Paleta de Cores |
|---|---|---|---|---|---|
| **ThSyr** | `ThSyr` | Letterform | Geometric Construction, Negative Space | Chevron, Triangulo | Carvao `#121316`, Carmesim `#E63946`, Ouro `#D4AF37` |
| **ThAspect** | `ThAspect` | Letterform | Brutalismo, Monoline Grid | Triangulo Assimetrico | Loop Black `#0A0A0A`, Ecru `#F4F1EA`, Laranja `#FF5722` |
| **ThPay** | `ThPay` | Combinacao | Duality Interlock, Continuous Line | Hexagono, Delta | Obsidiana `#0B0F19`, Esmeralda `#00A86B`, Menta `#10B981` |
| **SkillForge Frontend** | `SkillForge-Frontend` | Combinacao | Modular System, Bracket Code | Bigorna, Grid Bento | Ciano `#06B6D4`, Deep Space `#0F172A`, Violeta `#8B5CF6` |
| **CS-Vault 2026** | `CS-Vault-2026` | Emblema | Tessellation, Projecao Isometrica | Hexagono, Cubo | Ambar `#F59E0B`, Grafite `#1E293B`, Ardosia `#334155` |
| **APOS** | `apos` | Abstrato | Projecao Isometrica, Planta Baixa | Cubo Espacial, Eixo | Azul Planta `#0F2B48`, Ciano Eletrico `#00E5FF`, Aco `#94A3B8` |
| **Atlas** | `atlas` | Abstrato | Rotacao Dinamica, Aneis Orbitais | Circulo, Esfera Celestial | Marinho `#0A192F`, Cobalto `#2563EB`, Prata `#E2E8F0` |
| **Atlas HR Data Engine** | `atlas-hr-data-engine` | Abstrato | Modular, Vetores de Fluxo | Turbina Radial | Azul Petroleo `#082F49`, Ciano Kinetico `#14B8A6`, Celeste `#38BDF8` |
| **Atlas Showcase** | `atlas-landing-page` | Combinacao | Espaco Negativo, Prisma Ascendente | Prisma, Chevron | Safira `#0B132B`, Azul Real `#3B82F6`, Areia `#F8FAFC` |
| **Feriados Brasil** | `feriados-brasil` | Pictorial | Espaco Negativo, Grid de Calendario | Losango Nacional | Verde Brasil `#009C3B`, Ouro Solar `#FFDF00`, Azul `#002776` |
| **Jornada Excursoes** | `jornada-gestao-excursoes` | Pictorial | Linha Continua, Seta de Bussola | Circulo, Fita Infinita | Azul Rodovia `#1E3A8A`, Laranja Horizonte `#F97316`, Ceu `#38BDF8` |
| **Matheus Sousa** | `matheus-sousa-linkedin` | Monograma | Simetria Quiral, Chanfro 45° | Monograma MS | Onix `#111827`, Prata Titanio `#9CA3AF`, Ouro Champagne `#C5A880` |
| **Nosso Grande Dia** | `nosso-grande-dia` | Monograma / Selo | Linha Continua, Simetria Sagrada | Oval, Lao MV | Marinho CCB `#0C1B33`, Marsala `#6B1724`, Ouro `#D4AF37`, Creme `#FDFBF7` |
| **Receitas Andre da Empada** | `receitas` | Emblema | Rotacao Modular, Frisado Radial | Selo Circular, Balanca | Dourado Crosta `#D97706`, Terracota `#9A3412`, Creme `#FFFBEB` |
| **Marduk TS** | `shiny-carnival-fork` | Abstrato | Intertravamento, Piramides Gemeas | Prisma Duplo, Iris | Lapis Lazuli `#1E3A5F`, Violeta Solar `#C084FC`, Espaco `#0F172A` |

---

## 3. Estrutura do Repositorio

```
brand-vault/
├── README.md               # Documentacao master de arquitetura e inventario
├── catalog.json            # Catalogo estruturado consumivel por APIs e agentes
├── preview.html            # Folha de teste interativa com ladders de 16px a 256px
├── generate_vault.py       # Script deterministico de geracao e compilacao
└── brands/
    ├── thsyr/
    │   ├── thsyr-symbol.svg
    │   ├── thsyr-monochrome.svg
    │   ├── thsyr-lockup.svg
    │   └── spec.json
    ├── thaspect/
    │   ├── thaspect-symbol.svg
    │   ├── thaspect-monochrome.svg
    │   ├── thaspect-lockup.svg
    │   └── spec.json
    ├── thpay/
    │   ├── thpay-symbol.svg
    │   ├── thpay-monochrome.svg
    │   ├── thpay-lockup.svg
    │   └── spec.json
    ├── skillforge-frontend/
    ├── cs-vault-2026/
    ├── apos/
    ├── atlas/
    ├── atlas-hr-data-engine/
    ├── atlas-landing-page/
    ├── feriados-brasil/
    ├── jornada-gestao-excursoes/
    ├── matheus-sousa-linkedin/
    ├── nosso-grande-dia/
    ├── receitas-andre-empada/
    └── marduk-ts/
```

---

## 4. Auditoria e Integracao com o ThSyr

Para auditar qualquer marca com a engine do ThSyr:

```bash
# Auditoria de pureza vetorial
python3 /root/ThSyr/thsyr.py logo audit brands/thsyr/thsyr-symbol.svg

# Inspecao de todas as marcas de uma vez
python3 /root/ThSyr/thsyr.py logo audit brands/*/*-symbol.svg

# Geracao de variantes monocromaticas e web-icons
python3 /root/ThSyr/thsyr.py logo variants brands/thpay/thpay-symbol.svg --title "ThPay" --mono "#00A86B" --web-icons
```

---

## 5. Visualizacao Interativa

Abra o arquivo `preview.html` em qualquer navegador para inspecionar os simbolos, escalas microscopicas de 16px e 32px, paletas cromaticas e justificativas conceituais.
