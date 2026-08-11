# Publicando o site — do zero até o ar

Conta: **github.com/qualityandtrustservices**

**Boa notícia:** eu já deixei o repositório pronto dentro do zip — inicializado, com o commit feito e apontando pro seu GitHub. Você não precisa rodar `git init`, nem `git add`, nem `git commit`. Falta só o envio.

Existem **dois caminhos**. Escolha um.

---

# CAMINHO A — Sem instalar nada (recomendado pra primeira vez)

Você faz tudo pelo navegador, arrastando arquivos. Leva uns 10 minutos.

### A1. Criar o repositório

1. Logado no GitHub, clique no **+** no canto superior direito → **New repository**
2. **Repository name:** `quality-and-trust-website`
3. Deixe em **Public**
4. **NÃO marque** nenhuma caixinha (nada de "Add a README", ".gitignore" ou "license")
5. **Create repository**

### A2. Enviar os arquivos

Na tela que aparecer, clique em **uploading an existing file**.

> **Atenção:** o GitHub aceita no máximo **100 arquivos por vez** e a pasta `frames` tem 150. Por isso vamos em três levas.

**Leva 1 — a base**

Descompacte o zip. Entre na pasta `quality-and-trust-website`. Selecione e arraste pra janela do GitHub:

- a pasta `public` inteira **exceto** a subpasta `frames`
- os arquivos `README.md`, `GUIA-GITHUB.md`, `GUIA-PROMPTS-IA.md`, `gerar-frames-placeholder.py`

Escreva na caixa de baixo: `site base` e clique **Commit changes**.

**Leva 2 — primeira metade dos frames**

1. Clique em **Add file** → **Upload files**
2. Abra `public/frames` no seu computador
3. Selecione **do `frame_0001.jpg` até o `frame_0075.jpg`** (clique no primeiro, segure Shift, clique no último) e arraste

   ⚠️ Antes de soltar, arraste também o arquivo `manifest.json` que está nessa pasta.
4. **Importante:** na caixa de commit, escreva `frames 1` — mas **antes disso**, olhe o topo da página. Precisa aparecer o caminho `public/frames/`. Se não aparecer, veja a nota logo abaixo
5. **Commit changes**

**Leva 3 — segunda metade**

Mesma coisa, do `frame_0076.jpg` ao `frame_0150.jpg`.

> **Nota sobre o caminho da pasta:** ao arrastar arquivos soltos, o GitHub joga eles na raiz. Para forçar a pasta certa, na tela de upload digite `public/frames/` no campo de nome que aparece acima da área de arrastar, ou simplesmente **arraste a pasta `frames` inteira** em vez dos arquivos — o navegador preserva a estrutura e resolve tudo de uma vez. Se a pasta inteira passar sem reclamar do limite, melhor ainda: faça em uma leva só.

### A3. Conferir

Na página do repositório tem que aparecer a pasta `public`, e dentro dela `index.html`, `pricing.html`, o PDF, e as pastas `frames`, `images` e `videos`.

**Pule para a Parte 3 (Netlify).**

---

# CAMINHO B — Pela linha de comando

Mais rápido depois que estiver configurado, e é o que você vai usar pras atualizações do dia a dia.

### B1. Instalar o Git

**Windows:** baixe em **git-scm.com/download/win**, abra o instalador e clique **Next** em tudo. Depois procure **Git Bash** no menu Iniciar.

**Mac:** abra o Terminal e digite `git --version`. Se não tiver, o Mac oferece instalar. Aceite.

### B2. Criar o repositório no GitHub

Igual ao passo **A1** acima. Nome `quality-and-trust-website`, público, **sem marcar nenhuma caixinha**.

### B3. Abrir o terminal dentro da pasta

Descompacte o zip e coloque a pasta em `Documentos`.

- **Windows:** botão direito **dentro** da pasta `quality-and-trust-website` → **Git Bash Here**
- **Mac:** Terminal → digite `cd ` (com espaço) → arraste a pasta pra dentro da janela → Enter

**Confira:** digite `ls -a` e dê Enter. Precisa aparecer `public` e também `.git`. Se aparecer `.git`, é porque o repositório já está pronto, como eu deixei.

### B4. Enviar

Um comando só:

```
git push -u origin main
```

Vai abrir uma janela pedindo login no GitHub. Entre normalmente pelo navegador.

> **Se pedir usuário e senha no terminal:** o GitHub não aceita mais a senha da conta. Vá em github.com → foto no canto → **Settings** → role até **Developer settings** → **Personal access tokens** → **Tokens (classic)** → **Generate new token** → marque a caixa **repo** → gere e **copie o código**. Cole esse código no lugar da senha.

**Se der erro dizendo que o repositório remoto não existe:** você criou com outro nome. Rode:

```
git remote set-url origin https://github.com/qualityandtrustservices/NOME-QUE-VOCE-USOU.git
git push -u origin main
```

---

# Parte 3 — Colocar no ar com Netlify

Funciona igual, tendo você usado o caminho A ou o B.

1. Vá em **netlify.com** → **Sign up** → **Sign up with GitHub** → autorize
2. **Add new site** → **Import an existing project** → **GitHub**
3. Escolha o repositório `quality-and-trust-website`
4. Preencha exatamente assim:

| Campo | O que colocar |
|:---|:---|
| Branch to deploy | `main` |
| Base directory | *deixe vazio* |
| Build command | *deixe vazio* |
| **Publish directory** | **`public`** |

> **Publish directory é o único campo que importa de verdade.** Tem que ser `public`, porque é lá que está o `index.html`. Se errar, o site sobe em branco e parece que tudo deu errado — mas é só esse campo.

5. **Deploy**

Em menos de dois minutos você tem uma URL. Para trocar por um nome decente: **Site configuration** → **Change site name** → `qualityandtrust`. Vira `qualityandtrust.netlify.app`.

---

# Parte 4 — Domínio próprio (opcional)

`qualityandtrustservices.com` custa em torno de **US$ 12 a 15 por ano** — *estimativa baseada no preço típico de um `.com`. Confirme no registrador antes de comprar; não tenho como verificar o valor de hoje.*

1. Compre em **namecheap.com**, **porkbun.com** ou direto no Netlify
2. No Netlify: **Domain management** → **Add a domain**
3. O Netlify mostra os servidores DNS. Cole no painel de quem vendeu o domínio
4. De 1 a 24 horas pra propagar. O cadeado (HTTPS) o Netlify ativa sozinho e de graça

---

# Parte 5 — Atualizar depois

**Pelo navegador:** abra o arquivo no GitHub, clique no lápis, edite, **Commit changes**.

**Pelo terminal:**

```
git add .
git commit -m "descreva o que mudou"
git push
```

O Netlify percebe sozinho e republica em uns 30 segundos.

---

# O que trocar antes de mostrar pra cliente

Telefones, e-mail e Largo FL já estão certos no site inteiro. Faltam três coisas:

| O que | Onde | Por quê |
|:---|:---|:---|
| **Os preços** | `public/pricing.html` e o PDF | Marcados como **EXAMPLE** em verde. Todos inventados por mim como estrutura — **nenhum é pesquisa de mercado** |
| **Os depoimentos** | `public/index.html`, seção `#proof` | Estão com `[[Replace with a real review]]`. Sem avaliação real, **apague o bloco** em vez de inventar |
| **As imagens** | `public/images/` | Hoje são retângulos azuis com o nome do arquivo. O `GUIA-PROMPTS-IA.md` diz o que gerar e com que nome salvar |

---

# Erros comuns

| O que aparece | O que houve | Solução |
|:---|:---|:---|
| `fatal: not a git repository` | Terminal na pasta errada | `ls -a` precisa mostrar `.git` |
| `remote origin already exists` | Rodou `git remote add` de novo | Já está configurado. Vá direto pro `git push` |
| `failed to push some refs` | Marcou uma caixinha ao criar o repo | `git pull origin main --rebase` e depois `git push` |
| `Repository not found` | Nome diferente, ou não está logado | Confira o nome e refaça o login |
| Site no ar mas em branco | Publish directory errado | Netlify → mude pra `public` → redeploy |
| Imagens não aparecem | Nome do arquivo diferente | Minúsculas, com hífen, sem espaço, sem acento |
| Fontes estranhas | Rede bloqueando o Google Fonts | Normal em rede corporativa. No celular do cliente funciona |

---

# Uma coisa que provavelmente vale mais que o site

O site é o cartão de visita. **O Google Business Profile é quem traz cliente** em serviço local — é o que aparece no mapa quando alguém em Largo pesquisa "airbnb cleaning near me".

É grátis, leva uns 15 minutos, e você já tem tudo que ele pede: nome, telefones, e-mail, área de atuação e os serviços. Coloque a URL do site lá assim que estiver no ar.

*Recomendação baseada em como negócios locais costumam ser encontrados. Não tenho dados do seu mercado específico para comprovar o impacto no seu caso.*
