<div align="center">

<img src="https://raw.githubusercontent.com/AldairSbarros/Aletheia_v1.1/master/frontend/src/assets/aletheia_logo.png" alt="AletheIA" width="220" />

# AletheIA — Plataforma Teológica com IA

**Ferramentas especializadas · Multi-IA orquestrada · Geração paralela de conteúdo · RAG com 10 milhões de vetores**

> Documentação operacional revisada em 21 de agosto de 2026. Para iniciar o
> sistema e consultar as rotas atuais, veja [docs/ANALISE_E_COMANDOS.md](docs/ANALISE_E_COMANDOS.md) e [docs/GUIA_ENDPOINTS_SWAGGER.md](docs/GUIA_ENDPOINTS_SWAGGER.md).

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React_18-61DAFB?style=flat-square&logo=react)](https://react.dev)
[![Qdrant](https://img.shields.io/badge/VectorDB-Qdrant-DC244C?style=flat-square)](https://qdrant.tech)
[![Groq](https://img.shields.io/badge/LLM-Groq_Llama_3.3_70B-F55036?style=flat-square)](https://groq.com)
[![Gemini](https://img.shields.io/badge/IA-Gemini_2.5-4285F4?style=flat-square&logo=google)](https://ai.google.dev)

</div>

---

## O que é AletheIA?

**AletheIA** (*do grego ἀλήθεια — verdade*) é uma plataforma de inteligência artificial especializada em teologia bíblica, pastoral e acadêmica. Diferente de chatbots genéricos, cada ferramenta usa **RAG (Retrieval-Augmented Generation)** buscando em um acervo real de obras teológicas indexadas — nunca inventa citações, nunca fabrica autores.

O sistema orquestra múltiplos modelos de IA de forma inteligente: cada ferramenta recebe exatamente o modelo mais adequado para sua função.

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React 18)                      │
│  TypeScript · Tailwind CSS v4 · Vite · Framer Motion        │
│  Porta: 5173 (dev) · Build: /dist                           │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP / SSE
┌────────────────────▼────────────────────────────────────────┐
│                  BACKEND (FastAPI)                           │
│  Python 3.12 · Uvicorn · RAG Pipeline · Multi-IA Router     │
│  Porta: 8000                                                 │
└──────┬──────────────┬──────────────┬──────────────┬─────────┘
       │              │              │              │
┌──────▼──────┐ ┌─────▼─────┐ ┌────▼────┐  ┌─────▼──────┐
│   Qdrant    │ │   Groq    │ │ Gemini  │  │  Imagen 4  │
│ (vetores)   │ │ Llama 3.3 │ │ 2.5 Pro │  │  (imagens) │
│ 10M chunks  │ │  70B Chat │ │  Flash  │  │            │
└─────────────┘ └───────────┘ └─────────┘  └────────────┘
                                                  │
                                        ┌─────────▼──────────┐
                                        │  Digital Bible Plat │
                                        │  (DBP v4 API)       │
                                        │  diversos idiomas   │
                                        │  áudio·vídeo·busca  │
                                        └─────────────────────┘
```

---

## 🛠️ As 10 Ferramentas

### 💬 Chat Teológico
**Rota:** `/app/chat` · **Modelo:** `Groq / Llama 3.3 70B Versatile` · **Streaming SSE**

O coração do sistema. Converse com pastores como Calvino, Spurgeon, Keller e Bonhoeffer — não com um bot treinado em internet, mas com respostas **extraídas de suas obras reais** via RAG.

- 🔍 Busca semântica em tempo real em 10 milhões de fragmentos
- 📚 Cita autor, obra, página e ano de cada resposta
- 🌊 Streaming palavra a palavra (SSE)
- 🔢 Números Strong linkados com tooltip (G1234 / H5678)
- 🎙️ 6 modos: Geral, Autores, Sermão, Artigo, Debate
- ⚡ Latência < 1s (Groq hardware dedicado)

---

### 🎤 Gerador de Sermões Pro
**Rota:** `/app/sermao` · **Modelo:** `Gemini 2.5 Flash` · **Tokens:** 8.192/seção · **Geração paralela (4 seções simultâneas ~15-20s)**

O gerador mais completo do mercado evangelical. Fluxo em 4 etapas com **10 combinações** de tipo de sermão. As 4 seções do sermão (Introdução, Desenvolvimento, Aplicação, Conclusão) são geradas em paralelo com o mesmo contexto RAG.

**Por Estrutura:**
| Tipo | Descrição |
|------|-----------|
| 📖 Expositivo | Percorre o texto versículo a versículo |
| ✍️ Textual | As divisões emergem das palavras do versículo-base |
| 🔗 Temático | Tema central sustentado por múltiplos textos |

**Por Ocasião:**
| Tipo | Uso |
|------|-----|
| 📗 Edificante | Ensino profundo para crentes |
| 🌍 Evangelístico | Convite à conversão |
| 🕊️ Devocional | Vida espiritual pessoal |
| ⚡ Profético | Interpela a realidade social |
| 🎉 Comemorativo | Páscoa, Natal, aniversários |
| 🕯️ Fúnebre | Consolo com esperança cristã |
| 💍 Nupcial | Bênção do matrimônio |

**Por Formato:**
| Tipo | Estilo |
|------|--------|
| 📋 Convencional | Introdução, pontos, aplicação, conclusão |
| 🎭 Narrativo | Dramatiza a cena bíblica |
| 👤 Biográfico | Centra em um personagem bíblico |
| ⚖️ Dialético | Apresenta tensão teológica e resolução |

**Recursos pós-geração:**
- 🎙️ **Áudio** — Narração com processamento local configurável e fallback remoto
- 🖼️ **Imagem temática** — Geração pelo modelo configurado, com fallback de imagem
- 📄 Export PDF · 📋 Copiar tudo

**Estilos teológicos:** Reformado (Calvino/Spurgeon) · Pentecostal · Acadêmico

---

### 📗 Apostila Ministerial Pro
**Rota:** `/app/apostila` · **Modelo:** `Gemini 2.5 Flash` · **Tokens:** 6.000/ministração · **Geração paralela (~20s fixo para qualquer quantidade)**

Gera apostilas completas para escola bíblica, células e treinamentos ministeriais com a mesma profundidade estrutural do Gerador de Sermões.

- **Títulos personalizáveis** — defina o tema de cada ministração individualmente (ou deixe o sistema criar)
- **Referência bíblica por ministração** — campo opcional por ministração (ex: `João 3.16`, `Rm 8.1-4`) que aciona **RAG duplo**: busca semântica geral + busca focada no texto bíblico
- **Estrutura homilética completa** por ministração:
  - `INTRODUÇÃO` — contextualização, gancho narrativo, apresentação do texto-base
  - `DESENVOLVIMENTO` — exegese detalhada, doutrina, debates históricos, citações de teólogos
  - `APLICAÇÃO` — aplicação prática, exemplos concretos, chamada para ação
  - `CONCLUSÃO` — síntese, apelo pastoral/evangélístico, bênção final
- Geração paralela: todas as ministrações são processadas simultaneamente
- RAG específico por ministração (busca focada no subtema de cada uma)
- Referências ABNT das fontes reais do acervo
- Export PDF profissional

**Recursos pós-geração por ministração:**
- 🎙️ **Áudio** — Narração com processamento local configurável e fallback remoto
- 🖼️ **Imagem temática** — Geração pelo modelo configurado, com fallback de imagem

---

### 📘 Livro Teológico Pro
**Rota:** `/app/livro` · **Modelo:** `Gemini 2.5 Pro` · **Tokens:** 2.048 (sumário) + 16.384/capítulo · **Geração paralela (~60s para qualquer quantidade)**

Obra completa com coerência temática entre capítulos.

- Sumário gerado primeiro, depois todos os capítulos processados em paralelo
- **5 a 12 capítulos** configuráveis (~20-30 páginas a ~50-70 páginas)
- Cada capítulo com 3-4 subseções e texto acadêmico denso
- RAG específico por capítulo (busca focada no subtema)
- Referências ABNT consolidadas

---

### 🔬 Estudo Bíblico Pro
**Rota:** `/app/estudo` · **Modelo:** `Groq / Qwen 3 32B` · **Tokens:** 1.200/seção + 600 WhatsApp · **Geração paralela (6 tarefas simultâneas ~12s)**

Exegese acadêmica completa com análise de idiomas originais.

**Seções geradas em paralelo:**
1. Contexto Histórico-Cultural
2. Análise do Texto Original (grego/hebraico)
3. Teologia do Texto
4. Debates Doutrinários
5. Aplicação Contemporânea
6. *(paralelo)* Versão WhatsApp

**Diferencial:** Versão formatada para WhatsApp com emojis — pronta para grupos de célula.

---

### 📰 Artigo Científico Pro
**Rota:** `/app/artigo` · **Modelo:** `Gemini 2.5 Flash` · **Tokens:** 4.096/seção · **Geração paralela (6 tarefas simultâneas ~20s)**

Artigo acadêmico rigoroso no padrão ABNT — 5 seções e título gerados em paralelo:

1. Introdução e Delimitação do Problema
2. Fundamentação Teórica e Revisão Bibliográfica
3. Análise Exegética e Doutrinária
4. Correntes Divergentes e Debate Acadêmico
5. Conclusão, Síntese e Perspectivas
6. *(paralelo)* Título acadêmico gerado simultaneamente

- Cada seção com RAG específico (busca focada no subtema)
- Citações em formato ABNT natural — sem marcadores internos `[FONTE X]`
- Referências ABNT de fontes reais

---

### 🧡 Conselheiro Pastoral Pro
**Rota:** `/app/conselheiro` · **Modelo:** `Gemini 2.5 Pro` · **Tokens:** 8.192/eixo (mínimo garantido) · **Geração paralela (6 eixos simultâneos ~30s)**

Parecer multidisciplinar completo para casos pastorais sensíveis. Analisa o caso em **5 eixos simultâneos** + diagnóstico geral:

| Eixo | Perspectiva |
|------|-------------|
| 🧠 Psicologia Pastoral | Saúde emocional, vínculos, trauma |
| ⚖️ Ética e Direito Canônico | Responsabilidade moral, normas eclesiásticas |
| 📖 Teologia e Exegese | Fundamentos bíblicos para o caso |
| 📋 Plano de Intervenção | 6-8 passos práticos e concretos |
| 🔭 Prognóstico Pastoral | Perspectivas de restauração |

- Diagnóstico geral consolidado ao final
- Follow-up para aprofundamento de aspectos específicos
- Tratamento ético de dados — sem armazenamento de casos

---

### 📖 Bíblia
**Rota:** `/app/biblia` · **API:** `Digital Bible Platform v4` · **Proxy leve, sem IA generativa**

Leitura completa da Bíblia com seleção de idioma, versão e navegação por livro/capítulo. Dados reais servidos via [Digital Bible Platform](https://www.digitalbibleplatform.com) — mais de 2.400 versões em centenas de idiomas.

**Funcionalidades:**
- 🌍 **Seletor de idioma com busca** — 12 idiomas pré-carregados (incl. Ticuna) + campo de busca que consulta os diversos idiomas da plataforma em tempo real
- 📚 **Seletor de versão** — todas as traduções disponíveis para o idioma escolhido, com **badges de mídia** (🔊 Áudio, 🎭 Drama, 🎬 Vídeo) indicando o que está disponível
- 📜 **Lista de livros** — AT e NT separados, com seleção por clique
- 📖 **Leitura fluida** — versos em fluxo contínuo, numeração em dourado sobrescrita
- 🔢 **Seletor de capítulo** — dropdown + navegação Anterior/Próximo (atravessa livros automaticamente)
- 🔊 **Player de áudio** — reproduz MP3 narrado (verde) ou dramatizado/teatralizado (roxo) quando disponível para o capítulo, com indicador de duração e botão ▶/⏸
- � **Read-along (karaoke)** — quando a versão fornece timestamps (ex: ARC português, KJV inglês), o versículo em reprodução fica destacado em âmbar e a tela acompanha automaticamente
- �🎬 **Player de vídeo** — banner com thumbnail e modal fullscreen `<video>` para versões com dramatização em vídeo
- 🔍 **Busca** — pesquisa de termos com destaque e atalho para o capítulo/versículo
- 🏠 **Destaque na landing** — card colapsável abaixo do chat (estado inicial) com CTA direto para a ferramenta e recursos (diversos idiomas · áudio e karaokê · vídeo quando disponível); recolhe ao iniciar a conversa

**Requisito:** `BIBLE_KEY` configurada no `backend/.env` ([obter chave gratuita](https://www.digitalbibleplatform.com/platform/)).

---

## 🤖 Roteamento de IA

O sistema escolhe automaticamente o modelo ideal para cada tarefa:

| Ferramenta | Modelo | Tokens | Estratégia |
|------------|--------|--------|------------|
| Chat (streaming) | `Groq / openai/gpt-oss-120b` | — | SSE, latência < 1s |
| Sermão | `Gemini 2.5 Flash` | 8.192/seção | 4 seções paralelas |
| Apostila | `Gemini 2.5 Flash` | 6.000/min. | N ministrações paralelas · RAG duplo com ref. bíblica |
| Livro | `Gemini 2.5 Pro` | 16.384/cap. | Todos os capítulos paralelos |
| Estudo Bíblico | `Groq / Qwen 3 32B` | 1.200/seção | 6 tarefas paralelas |
| Artigo | `Gemini 2.5 Flash` | 4.096/seção | 6 tarefas paralelas |
| Conselheiro | `Gemini 2.5 Pro` | 8.192/eixo | 6 eixos paralelos |
| Áudio (Sermão/Apostila) | `Gemini 2.5 Flash TTS` | — | Narração profissional por seção |
| Imagem (Sermão/Apostila) | `Imagen 4.0 Generate` | — | Arte inspiracional por seção |
| **Bíblia** | `Digital Bible Platform v4` | — | Proxy puro — sem IA, latência < 500ms |

**Fallback automático:** Se um modelo Gemini falhar, o sistema cai automaticamente para Groq sem interromper a experiência do usuário.

**Thinking tokens (`gemini-2.5-pro`):** O modelo usa raciocínio interno obrigatório que consome `max_output_tokens`. O sistema aplica automaticamente `effective_tokens = max(tokens, 8192)` para garantir que sempre haja tokens suficientes para thinking + texto de saída.

---

## 🎙️ Voz, Gestão de Acervo e Monetização Avançada

### 🗣️ Acessibilidade e Interatividade por Voz
O sistema possui integração nativa no frontend para ditado e fala, facilitando o uso:
- **Ditado de Perguntas (Speech-to-Text - STT):** Através do ícone de microfone (`Mic2`) no Chat e na Landing Page, o usuário dita seu prompt e o sistema transcreve para o campo de texto usando a API de voz nativa do navegador (`webkitSpeechRecognition`).
- **Leitura em Voz Alta (Text-to-Speech - TTS):** No Chat e na Landing Page, o usuário pode clicar no ícone de áudio (`Volume2`/`VolumeX`) para ouvir as respostas teológicas em português brasileiro (`pt-BR`) via síntese nativa de voz (`window.speechSynthesis`). O Markdown das respostas é automaticamente sanitizado para uma narração oral contínua.

### 📥 Ingestão de Obras pelo Painel Admin
Os administradores contam com uma central de ingestão de conteúdo diretamente no navegador:
- **Envio Multi-Formato:** Upload de arquivos `.pdf`, `.docx`, `.txt` ou `.md` diretamente ao Qdrant.
- **Isolamento de Acervos:** Suporte para escolher coleções existentes no cluster Qdrant (como a base principal `teologia_v3_master`) ou provisionar novas coleções privadas otimizadas para clientes de plano *Corporate*.
- **Task Worker Secundário:** Ingestão de background assíncrona que extrai textos, converte no tamanho ideal de chunks e grava em lotes associados a chaves UUID v5, com gerenciamento do status do job e contagem de vetores.

### 📲 WhatsApp — Devocional Diário Automático
**Rota:** `/app/whatsapp` · **Disponível para:** planos Basic, Pro, Enterprise, Corporate e Master (free_trial não incluído)

Cada cliente conecta o **próprio WhatsApp** e recebe uma mensagem devocional gerada por IA todos os dias nos grupos da sua igreja — com texto completo, imagem temática e agenda semanal de assuntos, sem precisar copiar/colar nada manualmente.

**Como o pastor/administrador usa (menu → WhatsApp):**
1. **Conectar o próprio WhatsApp:** clique em **Conectar WhatsApp** e escaneie o QR Code exibido na tela com o número que vai enviar as mensagens — cada cliente tem sua própria conexão, isolada dos demais.
2. **Buscar grupos automaticamente:** clique em **Buscar grupos do WhatsApp** para listar todos os grupos do número conectado (nome + nº de participantes) e adicione com um clique — sem precisar descobrir o ID manualmente.
3. **Ativar/desativar grupos:** cada grupo cadastrado tem um botão de liga/desliga — desative temporariamente um grupo sem precisar removê-lo. Limite de grupos por plano: Basic 5, Pro 15, Enterprise 25, Corporate/Master ilimitado.
4. **Agenda semanal de temas:** defina um tema para cada dia da semana (ex.: Segunda "esperança", Terça "gratidão"...) e o horário do disparo automático. Salvar aplica na hora, sem reiniciar nada — mude os temas quando quiser.
5. **Disparo manual (teste ou avulso):** digite um tema e clique em **Enviar devocional agora** — roda em segundo plano (mostra "Gerando e enviando…") e envia para todos os grupos ativos, com intervalo entre cada envio (evita bloqueio do número pelo WhatsApp).

**O que a mensagem inclui:** uma **imagem temática gerada por IA** (sem texto na imagem) como foto, com o **devocional completo como legenda** — saudação do dia, reflexão pastoral desenvolvida com base no acervo teológico (RAG), um versículo bíblico central com breve explicação, e um convite para conhecer o AletheIA (`aletheia.ia.br`). Se o envio da imagem falhar por qualquer motivo, o sistema envia o texto sozinho automaticamente.

**Arquitetura multi-tenant:** cada licença tem sua própria instância na Evolution API (mesmo servidor, múltiplas conexões de WhatsApp isoladas), seus próprios grupos e sua própria agenda semanal — nenhum cliente vê os dados de outro. Um Painel Admin complementar (uso exclusivo do administrador do sistema) mantém uma visão de gestão global para suporte.

> **Correção 08/10/2026:** O devocional das 06:30 parou de rodar por crash loop do container (`sentence-transformers` sem pin → `ModuleNotFoundError`). Fixado no commit `62eed15` com pin `sentence-transformers==5.1.0` + `transformers==4.49.0`. Container estável, scheduler re-registrado (`✅ Agendador do devocional ativo para tenant 39C0 — todo dia às 06:30`).

---

## 🤖 WhatsApp — Auto-Resposta Teológica (AletheIA_Chat)

**Número:** `559284049322` (instância `AletheIA_Chat`)  
**Rota interna:** `POST /api/whatsapp/handle` (webhook Evolution API)

Quando alguém envia mensagem real para este número, o sistema responde automaticamente com teologia baseada no acervo (RAG + Groq):

1. **Evolution API** recebe a mensagem → dispara webhook `POST https://api.aletheia.ia.br/api/whatsapp/handle`
2. **Backend** normaliza payload (`_whatsapp_normalizar`) — aceita formato bruto Evolution `{instance, event, data:{key, message}}` ou já-normalizado
3. **Pipeline RAG** busca no Qdrant (10M vetores) → contexto para **Groq `openai/gpt-oss-120b`**
4. **Resposta** enviada via Evolution `sendMedia` (imagem/logo) + `sendText` (texto teológico) na instância `AletheIA_Chat`
5. **Anti-eco/anti-fuga:** só instâncias listadas em `WA_AUTO_REPLY_INSTANCES` (`AletheIA_Chat`) auto-respondem — o nº pessoal (`AletheIAZap`) NÃO responde em grupos

**Fluxo completo testado:** `curl` direto no backend → `sent: true`, `sendMedia 201`, `sendText 201`, `n_fontes=12`.

> O n8n (`SfvwxglyiH3EKUhs`) permanece para outras automações; a ponte WhatsApp→IA agora é **direta no backend** (webhook Evolution → `https://api.aletheia.ia.br/api/whatsapp/handle`) para evitar bugs de expressão do n8n 1.87 em modo produção.

### ✈️ Telegram — Devocional Diário Automático
**Rota:** `/app/telegram` · **Disponível para:** planos Basic, Pro, Enterprise, Corporate e Master (free_trial não incluído)

Mesma proposta do WhatsApp Devocional, mas usando a **API oficial do Telegram** (Bot API) — bem mais simples de conectar, pois não exige QR Code nem instância própria por cliente: **um único bot** (`@AletheIA_oficial_bot`) atende todos os clientes.

**Como o pastor/administrador usa (menu → Telegram):**
1. **Adicionar o bot ao grupo:** abra `t.me/<bot>` e adicione-o ao grupo/canal da igreja — sem QR Code.
2. **Buscar grupos automaticamente:** envie qualquer mensagem no grupo (ex.: "/start") e clique em **Buscar grupos do Telegram** para localizá-lo e cadastrar com um clique.
3. **Ativar/desativar grupos, agenda semanal de temas e disparo manual:** funcionam exatamente como no WhatsApp (mesmos limites por plano).

**Isolamento multi-tenant:** como o bot é compartilhado, um mapa de "reivindicação" (`telegram_claims.json`) garante que um grupo já cadastrado por um cliente não possa ser registrado por outro.

### 🔐 Monetização, Planos e Degustação Incondicional por IP
Uma arquitetura de negócios completa e blindada, baseada em assinaturas do Stripe, planos exclusivos e degustação baseada em IP:
- **Entrada sem Fricção por IP:** Por padrão de fábrica, o app inicia conectado à licença `"IP_FREE_ACCESS"`, desplugando o utilizador de barreiras de entrada e logando-o imediatamente no painel de ferramentas.
- **Identificação Dinâmica por Proxy:** O IP real do visitante é capturado analisando cabeçalhos comuns do proxy reverso de VPS (`X-Forwarded-For`, `X-Real-IP`), com fallback para `request.client.host`.
- **Limitação Baseada em IP em `limites_ip.json` (Exclusivo para degustação livre sem cadastro):**
  - **Trial Temporal de 30 Dias** para os canais de alta interação de teste: **Chat** e **Gerador de Sermões**.
  - **Limites Numéricos Vitalícios de Teste** para ferramentas focadas: **Apostila** (limitado a 10 gerações por IP), **Estudo Bíblico** (10), **Livro** (1) e **Artigo** (1).
  - **Planos de Assinatura Preservados:** Usuários com chaves de licença ativas de planos pagos (Básico, Pro, Enterprise, Corporate) **mantêm integralmente suas cotas e limites mensais recorrentes normais** (de 600 a 5000 mensagens de chat/mês, múltiplos sermoes, livros, etc.), sem sofrer qualquer impacto por essa segmentação baseada em IP.
  - **Bloqueio Seletivo:** O Conselheiro Pastoral é retido para uso apenas em contas com plano ativo por IP (retorna erro HTTP 402).
- **Banner Superior Inteligente:** Um alerta em gradiente laranja é acionado quando o usuário por IP consome mais de 50%+ da cota de qualquer recurso, motivando-o a clicar no botão de "Ver Assinaturas".
- **Conversão de Conta Dinâmica:** Se o utilizador por IP decide assinar um plano pago (`Config.tsx`), o frontend detecta, coleta seu e-mail através de um prompt amigável, cria a conta no backend, efetua o auto-login imediato e redireciona o usuário ao Checkout Stripe (cartão de assinatura mensal ou Pix de 30 dias avulsos) sob sua nova licença permanente.

---

## ⚡ Desempenho — Geração Paralela

Todas as ferramentas multi-seção usam `asyncio.gather + asyncio.to_thread` para processar seções simultâneas:

| Ferramenta | Antes | Depois |
|---|---|---|
| Sermão | ~60s (1 call) | **~15-20s** (4 paralelas) |
| Apostila 3 ministrações | ~30s (1 call, sem estrutura) | **~20s** (3 paralelas, estrutura homilética) |
| Apostila 8 ministrações | ~40s (1 call, qualidade baixa) | **~20s** (8 paralelas, RAG duplo/bíblico) |
| Livro 7 capítulos | ~350s ⚠️ | **~60s** ✅ |
| Livro 12 capítulos | ~600s ❌ timeout | **~65s** ✅ |
| Estudo Bíblico | ~25s (1 call) | **~12s** (6 paralelas) |
| Artigo | ~75s (sequencial) | **~20s** (6 paralelas) |
| Conselheiro | ~150s ❌ timeout | **~30s** ✅ |

---

## ⚡ Stack Técnica

### Backend
```
FastAPI 0.139.0          — API REST + SSE streaming
Python 3.12              — Runtime
Uvicorn                  — ASGI server com --reload
Qdrant Client            — Vector database (10M vetores)
SentenceTransformers     — Modelo de embedding all-MiniLM-L12-v2
Groq SDK                 — Chat + Qwen via API OpenAI-compatible
google-genai 2.10+       — Gemini Pro/Flash + TTS + Imagen
httpx 0.28+              — Cliente HTTP async para proxy da Bíblia
stripe 15+               — Pagamentos (checkout cartão recorrente + Pix)
geoip2                   — Geolocalização anônima de acessos (GeoLite2)
PBKDF2-HMAC-SHA256       — Hash de senha do usuário master
HMAC-SHA256              — Tokens de admin com TTL de 8h
```

### Frontend
```
React 18                 — UI framework
TypeScript               — Type safety
Vite 8.1.3               — Build tool
Tailwind CSS v4          — Utility-first CSS
Framer Motion            — Animações fluidas
Lucide React             — Ícones vetoriais
React Router DOM         — Roteamento SPA
Zustand                  — State management (auth)
```

### Infraestrutura
```
Qdrant (Docker)          — Vector store, porta 6333
Python venv              — Isolamento de dependências
GeoLite2-Country.mmdb    — Base GeoIP local (8.5 MB)
logs/rag_queries.jsonl   — Log de queries RAG (IPs anonimizados)
logs/stats_acesso.json   — Estatísticas geográficas agregadas
```

---

## 🚀 Setup Local

### Pré-requisitos
- Python 3.12+
- Node.js 20+
- Docker (para Qdrant)

### 1. Qdrant
```bash
docker run -d --name aletheia_qdrant \
  -p 6333:6333 \
  -v $(pwd)/qdrant_data:/qdrant/storage \
  qdrant/qdrant
```

### 2. Backend
```bash
cd /path/to/Aletheia_v1.2
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

# Configurar variáveis de ambiente
cp backend/.env.example backend/.env
# Editar backend/.env com suas chaves

# Iniciar servidor
./backend/start.sh
# ou: uvicorn backend.api_server:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Frontend
```bash
cd frontend
npm install
npm run dev
# Acesse: http://localhost:5173
```

---

## 🔑 Variáveis de Ambiente

```env
# backend/.env

GROQ_API_KEY=           # Chave Groq (obrigatório — chat + estudo)
GEMINI_API_KEY=         # Chave Google AI (obrigatório — sermão, livro, artigo...)
GOOGLE_API_KEY=         # Mesma chave Gemini

QDRANT_HOST=localhost   # "qdrant" dentro do Docker
QDRANT_PORT=6333
QDRANT_COLLECTION=teologia_v3_master

EMBED_MODEL=all-MiniLM-L12-v2
GROQ_MODEL=openai/gpt-oss-120b
MODEL_FAST=gemini-3.1-flash-lite
MODEL_SMART=gemini-2.5-pro

# Usuário master (acesso completo)
MASTER_EMAIL=
MASTER_CHAVE=
MASTER_PASSWORD_HASH=   # PBKDF2-HMAC-SHA256
MASTER_PASSWORD_SALT=
ADMIN_SECRET=           # HMAC para tokens de admin

# Bíblia — Digital Bible Platform (https://www.digitalbibleplatform.com)
BIBLE_KEY=              # Chave gratuita da Digital Bible Platform v4

# Pagamentos — Stripe (https://stripe.com)
STRIPE_API_KEY=         # Secret key (sk_test_... ou sk_live_...)
STRIPE_WEBHOOK_SECRET=  # Segredo do webhook (whsec_...)
SITE_URL=http://localhost:5173   # URL do frontend p/ redirect pós-pagamento
ADMIN_KEY=              # Chave do painel admin (header X-Admin-Key)
BONUS_DIAS_INDICACAO=7  # Dias de bônus (indicador + indicado) no programa de indicação
GITHUB_TOKEN=           # Token (fine-grained, só leitura) p/ o admin checar atualizações — repo é privado
GITHUB_REPO=AldairSbarros/Aletheia_v1.1
API_PUBLIC_URL=https://api.aletheia.ia.br  # usado no link de opt-out das mensagens de leads WhatsApp
RESEND_API_KEY=         # API Key do Resend (https://resend.com) p/ enviar a newsletter diária
RESEND_FROM=AletheIA <onboarding@resend.dev>  # remetente (troque após verificar o domínio no Resend)
NEWSLETTER_HORA=06:30   # horário do envio diário da newsletter

# WhatsApp — Evolution API (devocional diário para grupos da igreja)
EVOLUTION_API_URL=      # URL da instância Evolution API (ex: http://ic-evolutionapi-aKTG:8080)
EVOLUTION_API_KEY=      # apikey global da instância Evolution API
EVOLUTION_INSTANCE=     # nome da instância conectada (padrão: AletheIAZap)
WHATSAPP_DEFAULT_GROUP= # grupo padrão para envio manual avulso (opcional)
WHATSAPP_DEVOCIONAL_AUTO=false   # true = ativa envio automático diário
WHATSAPP_DEVOCIONAL_HORA=06:00   # horário do disparo automático (fuso America/Sao_Paulo)
WHATSAPP_DEVOCIONAL_TEMA=esperança  # tema padrão quando o disparo automático não especifica outro
WHATSAPP_DELAY_SEGUNDOS=8        # intervalo entre envios a grupos diferentes (antispam)

# Backup automático dos dados persistentes (licenças, grupos, agenda, uploads)
BACKUP_AUTO_DIARIO=true  # true = gera backup .tar.gz automaticamente todo dia
BACKUP_HORA=03:00        # horário do backup automático (fuso America/Sao_Paulo)
BACKUP_RETENCAO=30       # quantos backups mais recentes manter (os mais antigos são apagados)
```

---

## 🛟 Backup e restauração de dados

Dados como licenças, grupos/agenda de WhatsApp e Telegram e uploads ficam em
`backend/app/data/` e `backend/uploads/` — pastas montadas como *bind mount* no
Docker (`docker-compose.yml`), então **já sobrevivem normalmente a um
`docker-compose up -d --build`**. Mesmo assim, para proteger contra erro humano,
exclusão acidental ou migração de servidor, existem duas camadas de backup:

1. **Automática (dentro do backend):** todo dia, no horário definido por
   `BACKUP_HORA`, o backend gera sozinho um `.tar.gz` em `./backups/` (montado
   em `/app/backups` no container). Controlado por `BACKUP_AUTO_DIARIO`/`BACKUP_HORA`/`BACKUP_RETENCAO`.
   Endpoints admin (`X-Admin-Key`): `POST /api/admin/backup/gerar` (gera agora),
   `GET /api/admin/backup/listar`, `GET /api/admin/backup/download/{arquivo}`.
2. **Scripts para deploy/VPS** (`scripts_deploy/`):
   - `backup_dados.sh` — gera backup manualmente (mesma lógica, via shell).
   - `restaurar_dados.sh [arquivo]` — restaura o backup mais recente (ou um específico).
   - `deploy_seguro.sh [servico]` — faz backup automático **antes** de `git pull` +
     `docker-compose up -d --build`, garantindo que nenhuma atualização de código
     jamais apague licenças, grupos ou agenda dos usuários.

Use `deploy_seguro.sh` no lugar de rodar `docker-compose up -d --build` direto no
VPS — assim toda atualização já fica protegida por um backup recente.

O painel Admin (`/app/admin`) também tem botões para **gerar/baixar backup na hora** e
**verificar se há atualização disponível** (compara o commit em produção com o GitHub —
só leitura, não aplica nada sozinho; se houver atualização, mostra o comando pra rodar via SSH).
A checagem de atualização exige `GITHUB_TOKEN` (o repositório é privado — sem o token o
botão explica como gerar um). O botão de backup usa os mesmos endpoints admin acima.

## 📣 Crescimento: indicação, analytics e branding no devocional

- **Programa de indicação:** todo usuário tem um código/link próprio (`GET /api/conta/indicacao`,
  exibido em Configurações → "Indique e ganhe"). Quem cria conta pelo link (`?ref=CODIGO`, capturado
  automaticamente na landing e enviado em `POST /api/auth/criar`) e quem indicou ganham
  `BONUS_DIAS_INDICACAO` dias cada (padrão 7).
- **Analytics na landing:** GA4 e Meta Pixel são opcionais e configurados por variável de ambiente
  do frontend (`frontend/.env` local ou build args `VITE_GA_ID`/`VITE_META_PIXEL_ID` no
  `docker-compose.yml`/`.env` raiz). Sem essas variáveis, o tracking vira no-op. Eventos de funil
  disparados: `testar_gratis`, `conta_criada`, `iniciou_checkout`.
- **Devocional com link rastreável:** as mensagens automáticas de WhatsApp/Telegram já incluem um
  rodapé com o link de indicação do próprio tenant (`_link_indicacao`), transformando cada envio
  para grupos/canais em um convite atribuível a quem enviou.
- **Leads WhatsApp (remarketing):** visitantes no trial por IP (sem cadastro) podem deixar o
  WhatsApp voluntariamente (banner opt-in exibido no app) e recebem uma sequência automática de
  3 mensagens (imediata, dia 3, dia 7) via Evolution API, com link de opt-out de um clique em cada
  mensagem. Painel admin mostra os leads capturados e permite ativar/desativar manualmente.
- **Feed RSS do devocional:** `GET /api/rss/devocional.xml` — feed público (sem cadastro) com o
  devocional diário do tenant master, arquivado automaticamente todo dia. Descoberível via
  `<link rel="alternate">` no `index.html` (RSS readers detectam sozinhos) e link visível em `/app/sobre`.
- **Newsletter por e-mail (Resend):** assinatura opt-in em `/app/sobre`, devocional diário enviado
  automaticamente (horário `NEWSLETTER_HORA`) a todos os assinantes ativos, com link de
  cancelamento de um clique (validado por token) em cada e-mail. Requer `RESEND_API_KEY` — sem ela,
  a inscrição funciona normalmente mas o envio falha graciosamente (só loga aviso).
- **Canal oficial no WhatsApp:** canal público (mantido manualmente, fora da API — WhatsApp Channels
  ainda não é suportado pela versão da Evolution API em produção) divulgado via componente
  `DevocionalPromo` (`frontend/src/components/shared/DevocionalPromo.tsx`), reutilizado na landing
  (`Auth.tsx`), no Chat (`SourcePanel.tsx`) e em `Sobre.tsx`, ao lado do RSS e da newsletter.

**Como o visitante se cadastra (sem conta, sem senha):** acessa `aletheia.ia.br/app/sobre` →
seção "📬 Devocional diário" no topo da página → digita o e-mail no campo → clica em
"Receber por e-mail". Pronto — recebe uma confirmação na hora e, a partir do dia seguinte, o
devocional automático todo dia de manhã. Para RSS, é só clicar no botão "Assine o Devocional
Diário por RSS" (abre a URL do feed, que qualquer leitor de RSS reconhece). O mesmo bloco de
divulgação (Canal WhatsApp + RSS + e-mail) também aparece na landing page e na barra lateral do Chat.

```
POST /api/auth/validar          — Valida chave de licença
POST /api/auth/criar            — Cria nova conta (30 dias trial, aceita `ref` opcional p/ indicação)
POST /api/auth/login-email      — Login com e-mail + senha (usuário master)
GET  /api/conta/indicacao       — Código/link de indicação do próprio usuário + indicados/bônus
POST /api/admin/login           — Login admin (retorna token HMAC 8h)
GET  /api/admin/verificar       — Valida token admin

GET  /api/admin/dashboard       — Métricas: totais, ativos, uso e distribuição por plano
GET  /api/admin/acessos         — Visitantes únicos, acessos por ferramenta/país, série temporal
GET  /api/admin/versao          — Compara o commit em produção com o mais recente do GitHub
GET  /api/admin/usuarios        — Lista usuários (plano, status, assentos Corporate)
POST /api/admin/usuarios/{chave}/plano     — Altera o plano de um usuário
POST /api/admin/usuarios/{chave}/bloquear  — Bloqueia/desbloqueia um usuário
POST /api/admin/licencas/gerar             — Gera licença(s) manual/sorteio (plano, dias, limites custom)
POST /api/admin/corporate/provisionar      — Provisiona assentos de equipe (até 10)
GET  /api/admin/corporate/{chave}/assentos — Lista os assentos de uma licença Corporate
POST /api/admin/corporate/{chave}/remover  — Remove um assento (rebaixa membro p/ free)

POST /api/leads/whatsapp/capturar          — Captura opt-in de WhatsApp no trial (envia 1ª msg na hora)
GET  /api/leads/whatsapp/sair               — Link de opt-out de um clique (enviado em cada mensagem)
GET  /api/admin/leads/whatsapp              — Lista leads capturados p/ remarketing (admin)
POST /api/admin/leads/whatsapp/{numero}/toggle — Ativa/desativa manualmente um lead (admin)
GET  /api/rss/devocional.xml                — Feed RSS público do devocional diário (sem cadastro)
POST /api/newsletter/inscrever              — Assina o devocional diário por e-mail (opt-in)
GET  /api/newsletter/cancelar                — Link de cancelamento de um clique (validado por token)
GET  /api/admin/newsletter/assinantes        — Lista assinantes da newsletter (admin)
POST /api/admin/newsletter/assinantes/{email}/toggle — Ativa/desativa manualmente (admin)

POST /api/pagamento/criar       — Cria sessão de checkout Stripe (cartão recorrente ou Pix)
POST /api/pagamento/webhook     — Webhook Stripe (libera/renova acesso automaticamente)

GET  /api/chat/stream           — Chat RAG streaming (SSE)
GET  /api/strong/{id}           — Definição de número Strong (G1234/H1234)

POST /api/sermao/gerar          — Gera sermão completo (JSON estruturado)
POST /api/sermao/audio          — Narração em áudio (base64 WAV) — usada por Sermão e Apostila
POST /api/sermao/imagem         — Imagem temática (base64 PNG) — usada por Sermão e Apostila

POST /api/apostila/gerar        — Gera apostila ministerial (refs_biblicas[] + estrutura homilética)
POST /api/livro/gerar           — Gera livro teológico completo
POST /api/estudo/gerar          — Gera estudo bíblico com exegese
POST /api/artigo/gerar          — Gera artigo científico ABNT
POST /api/conselheiro/parecer   — Parecer pastoral multidisciplinar
POST /api/conselheiro/followup  — Aprofundamento de caso

GET  /api/biblioteca/{chave}    — Documentos gerados pelo usuário
POST /api/pdf/gerar             — Gera PDF de qualquer conteúdo

GET  /api/biblia/idiomas        — Lista idiomas disponíveis (fallback 12 idiomas populares)
GET  /api/biblia/idiomas/buscar — Busca idiomas por nome na DBP (?q=ticuna)
GET  /api/biblia/versoes        — Versões por idioma; inclui media_types e todos os filesets (?language_id=por)
GET  /api/biblia/{id}/livros    — Lista livros (AT/NT) de uma versão
GET  /api/biblia/texto/{fileset_id}/{book}/{chapter} — Retorna versos do capítulo
GET  /api/biblia/midia/{fileset_id}/{book}/{chapter} — URL de áudio/vídeo para o capítulo
GET  /api/biblia/timestamps/{fileset_id}/{book}/{chapter} — Timestamps por versículo (read-along)
GET  /api/biblia/buscar         — Busca termos na Bíblia (?q=...&bible_id=...)

POST /api/whatsapp/devocional          — Gera e envia devocional avulso (texto + imagem) a um único número/grupo

# WhatsApp multi-tenant (autenticado por X-License-Key, plano pago obrigatório)
POST /api/whatsapp/instancia/criar     — Cria a instância Evolution API do cliente
GET  /api/whatsapp/instancia/qrcode    — Retorna o QR Code (base64) para parear o WhatsApp
GET  /api/whatsapp/instancia/status    — Estado da conexão (conectado/desconectado)
GET/POST/DELETE /api/whatsapp/grupos[/{numero}/toggle] — CRUD de grupos do próprio cliente
GET  /api/whatsapp/grupos-disponiveis  — Busca grupos do WhatsApp conectado do cliente
GET/POST /api/whatsapp/agenda          — Agenda semanal de temas do próprio cliente
POST /api/whatsapp/disparar            — Inicia disparo em background (retorna job_id)
GET  /api/whatsapp/disparar/status/{job_id} — Consulta progresso/resultado do disparo

# WhatsApp — visão/gestão global do Admin master (autenticado por X-Admin-Key)
GET  /api/admin/whatsapp/grupos        — Lista grupos de WhatsApp cadastrados (tenant master)
GET  /api/admin/whatsapp/grupos-disponiveis — Busca grupos do WhatsApp conectado (Evolution API), sem persistir
POST /api/admin/whatsapp/grupos        — Cadastra um grupo (numero + nome)
POST /api/admin/whatsapp/grupos/{numero}/toggle — Ativa/desativa um grupo
DELETE /api/admin/whatsapp/grupos/{numero}      — Remove um grupo cadastrado
POST /api/admin/whatsapp/disparar      — Inicia o disparo em background (retorna job_id)
GET  /api/admin/whatsapp/disparar/status/{job_id} — Consulta progresso/resultado do disparo
GET  /api/admin/whatsapp/agenda        — Retorna a agenda semanal de temas + horário
POST /api/admin/whatsapp/agenda        — Salva a agenda semanal e reagenda o disparo automático (sem restart)

# Backup de dados (autenticado por X-Admin-Key)
POST /api/admin/backup/gerar             — Gera um backup .tar.gz agora
GET  /api/admin/backup/listar            — Lista backups existentes (nome, tamanho, data)
GET  /api/admin/backup/download/{arquivo} — Baixa um arquivo de backup específico

# Telegram (bot único compartilhado, autenticado por X-License-Key, plano pago obrigatório)
GET  /api/telegram/bot-info            — @username do bot compartilhado (para montar o link t.me/...)
GET/POST/DELETE /api/telegram/grupos[/{chat_id}/toggle] — CRUD de grupos do próprio cliente
GET  /api/telegram/grupos-disponiveis  — Busca chats onde o bot foi adicionado recentemente (getUpdates)
GET/POST /api/telegram/agenda          — Agenda semanal de temas do próprio cliente
POST /api/telegram/disparar            — Inicia disparo em background (retorna job_id)
GET  /api/telegram/disparar/status/{job_id} — Consulta progresso/resultado do disparo
POST /api/telegram/devocional          — Gera e envia devocional avulso (texto + imagem) a um único chat (teste)
```

---

## 🔐 Autenticação

O sistema possui dois tipos de acesso:

**Chave de Licença** — Usuários comuns acessam via chave alfanumérica (ex: `ABCD1234EFGH`). Planos com limites mensais por ferramenta.

**E-mail + Senha** — Usuário master com acesso ilimitado. Senha hasheada com PBKDF2-HMAC-SHA256 (100.000 iterações). Login disponível em `/` → aba "E-mail".

### 💳 Planos e Cotas

| Recurso | Free (30 dias) | Básico | Pro | Enterprise | Corporate |
|---|---|---|---|---|---|
| **Preço** | Grátis | R$ 39,90/mês | R$ 89,90/mês | R$ 799/mês | R$ 1.999/mês · até 10 usuários |
| 💬 Chat (por dia) | 15 | 50 | 100 | 400 | 150 / assento |
| 💬 Chat (por mês / cap) | 100 | 600 | 1.500 | 5.000 | 1.200 / assento |
| ✝️ Sermões | 2 | 10 | 30 | 80 | 25 / assento |
| 📚 Apostilas | 1 | 5 | 10 | 30 | 10 / assento |
| 📖 Livros | 0 | 1 | 3 | 10 | 2 / assento |
| 🔬 Estudos Bíblicos | 2 | 6 | 15 | 50 | 15 / assento |
| 🎓 Artigos Científicos | 1 | 3 | 10 | 40 | 12 / assento |
| ⚖️ Consultas Conselheiro | 2 | 10 | 20 | 60 | 25 / assento |

> **Enterprise** usa cotas de uso-justo generosas (individual). **Corporate** é um plano de equipe: cada um dos até 10 assentos recebe a cota por assento indicada. A conta **master** (dono) é isenta de qualquer limite.

> O chat aplica **teto duplo**: limite diário (anti-abuso) e teto mensal (proteção de custo). As demais ferramentas têm cota mensal. Contadores diários zeram à meia-noite e os mensais na virada do mês. Cada licença pode ainda ter **limites customizados por ferramenta** definidos pelo admin, que sobrepõem os padrões do plano.

**Pagamentos (Stripe):** cartão em **assinatura mensal recorrente** ou **Pix** avulso (libera 30 dias). O checkout é criado pelo backend e o acesso é liberado automaticamente via webhook.

**Admin** — Painel administrativo em `/admin-login`. Token HMAC-SHA256 com TTL de 8 horas. Recursos: dashboard com contagem por plano, gestão de usuários (plano/bloqueio), **provisionamento de assentos Corporate**, **gerador manual de licenças/sorteio**, **visão geral dos clientes WhatsApp conectados** (chave, email, número, status) e **backup/restore** do banco de dados.

**Recuperação de Senha** — Usuários podem recuperar a chave de acesso via email na rota `/recuperar-senha`. O fluxo gera um token temporário e envia a chave cadastrada para o email do usuário.

---

## 📊 Privacidade e Segurança

- **IPs anonimizados** — Apenas os dois primeiros octetos são registrados (`177.x.x.x`)
- **Sem armazenamento de casos pastorais** — Conteúdo do Conselheiro nunca é persistido
- **Sem API keys no frontend** — Todas as chamadas de IA passam pelo backend
- **Rate limiting** por chave de licença em todas as ferramentas
- **Senhas** hasheadas com PBKDF2-HMAC-SHA256, nunca armazenadas em plaintext

---

## 📁 Estrutura do Projeto

```
Aletheia_v1.2/
├── backend/
│   ├── api_server.py        # Servidor principal — todos os endpoints
│   ├── requirements.txt     # Dependências Python
│   ├── start.sh             # Script de inicialização
│   ├── .env                 # Variáveis de ambiente (não commitado)
│   └── GeoLite2-Country.mmdb  # Base GeoIP local
│
├── frontend/
│   ├── src/
│   │   ├── pages/           # Páginas React (Auth, Chat, Sermao, ...)
│   │   ├── components/      # Componentes reutilizáveis
│   │   ├── services/        # api.ts, sse.ts
│   │   ├── stores/          # Zustand (auth)
│   │   ├── hooks/           # useChat, usePdf
│   │   ├── types/           # TypeScript types
│   │   └── assets/          # Logo e ícone AletheIA
│   ├── package.json
│   └── vite.config.ts
│
├── ingestao/                # Scripts de ingestão do acervo teológico
├── logs/                    # RAG queries + estatísticas de acesso
├── producao/                # Documentos gerados (sermões, apostilas, ...)
├── docs/                    # Documentação técnica adicional
├── admin_aletheia.py        # Painel admin CLI
└── docker-compose.yml       # Qdrant + serviços
```

---

## 🌍 Estatísticas Geográficas

O sistema coleta estatísticas agregadas e anonimizadas de acesso por país e ferramenta. Visualize via painel admin:

```bash
python admin_aletheia.py
# Opção [9] 📍 Estatísticas Geográficas
```

---

<div align="center">

**AletheIA** — *Porque a verdade teológica merece ferramentas à altura.*

<img src="https://raw.githubusercontent.com/AldairSbarros/Aletheia_v1.1/master/frontend/src/assets/aletheia_icon.png" alt="AletheIA" width="48" />

Desenvolvido por **Aldair Sbarros** · 2026

</div>
