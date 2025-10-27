from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

    <!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Primeira Venda no Orgânico — eBook | [Seu Nome]</title>
  <meta name="description" content="Aprenda passo a passo como conseguir sua primeira venda de forma 100% orgânica. Estratégias simples para Instagram, Reels, SEO e mensagens que convertem." />
  <meta property="og:title" content="Primeira Venda no Orgânico — eBook" />
  <meta property="og:description" content="Estratégias práticas para sua primeira venda sem gastar com tráfego pago." />
  <meta property="og:image" content="[URL_DA_IMAGEM_DE_CAPA]" />
  <meta name="author" content="[Seu Nome]" />

  <!-- JSON-LD para rich snippets (opcional) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "Primeira Venda no Orgânico - eBook",
    "image": ["[URL_DA_IMAGEM_DE_CAPA]"],
    "description": "Guia prático para conseguir a primeira venda usando apenas tráfego orgânico.",
    "sku": "ebook-primeira-venda",
    "offers": {
      "@type": "Offer",
      "url": "[URL_DA_PAGINA_DE_VENDA]",
      "priceCurrency": "BRL",
      "price": "29.90",
      "availability": "https://schema.org/InStock"
    }
  }
  </script>

  <!-- Estilos simples inline para você copiar sem dependências -->
  <style>
    :root{
      --accent:#0b8f76;
      --dark:#111827;
      --muted:#6b7280;
      --card:#ffffff;
      --radius:14px;
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    *{box-sizing:border-box}
    body{margin:0;background:#f8fafc;color:var(--dark);line-height:1.45}
    .container{max-width:1000px;margin:30px auto;padding:20px}
    header{display:flex;align-items:center;justify-content:space-between;gap:16px}
    .logo{display:flex;align-items:center;gap:12px}
    .logo img{height:52px;border-radius:8px}
    nav a{margin-left:12px;text-decoration:none;color:var(--muted);font-weight:600}
    .hero{display:grid;grid-template-columns:1fr 420px;gap:24px;align-items:center;margin-top:24px}
    @media(max-width:880px){ .hero{grid-template-columns:1fr;}}
    .card{background:var(--card);border-radius:var(--radius);padding:22px;box-shadow:0 6px 20px rgba(2,6,23,0.06)}
    .title{font-size:28px;font-weight:800;margin:0 0 8px}
    .subtitle{color:var(--muted);margin:0 0 18px}
    .price{font-size:22px;color:var(--accent);font-weight:800}
    .features{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
    .feature{background:#f1f5f9;padding:8px 12px;border-radius:10px;font-weight:600;color:var(--dark)}
    .cover{width:100%;border-radius:10px;overflow:hidden}
    .cover img{width:100%;display:block}
    .actions{display:flex;gap:12px;margin-top:18px;flex-wrap:wrap}
    .btn{padding:12px 18px;border-radius:12px;border:0;font-weight:700;cursor:pointer}
    .btn-buy{background:var(--accent);color:white}
    .btn-video{background:transparent;border:2px solid var(--accent);color:var(--accent)}
    .small{font-size:14px;color:var(--muted)}
    section{margin-top:22px}
    .grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    @media(max-width:880px){ .grid-3{grid-template-columns:1fr}}
    .testimonial{padding:16px;border-radius:12px;background:linear-gradient(180deg,#fff,#fbfdff);border:1px solid #eef2f7}
    .faq-item{margin-bottom:8px}
    .footer{margin-top:30px;padding:18px;border-radius:12px;text-align:center;color:var(--muted);font-size:14px}
    .whatsapp-badge{position:fixed;right:18px;bottom:18px;background:#25D366;color:white;border-radius:999px;padding:12px 16px;font-weight:800;box-shadow:0 8px 30px rgba(2,6,23,.15);text-decoration:none;display:flex;align-items:center;gap:10px}
    .meta{display:flex;gap:12px;align-items:center}
    .author{display:flex;gap:12px;align-items:center}
    .author img{width:54px;height:54px;border-radius:999px;object-fit:cover}
    .badge{background:#0f172a;color:white;padding:6px 10px;border-radius:999px;font-weight:800}
    .center{text-align:center}
    .video-wrap{position:relative;padding-top:56.25%}
    .video-wrap iframe{position:absolute;left:0;top:0;width:100%;height:100%;border-radius:10px;border:0}
  </style>
</head>
<body>
  <a class="whatsapp-badge" href="https://wa.me/55SEUNUMERO?text=Ol%C3%A1%21%20quero%20comprar%20o%20eBook%20%22Primeira%20Venda%20no%20Org%C3%A2nico%22%20e%20queria%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">
    📲 Comprar no Zap
  </a>

  <div class="container">
    <header>
      <div class="logo">
        <!-- Substitua pelo logo real -->
        <img src="[URL_DO_SEU_LOGO]" alt="Logo"/>
        <div>
          <div style="font-weight:800">Primeira Venda no Orgânico</div>
          <div class="small">eBook prático — [Seu Nome]</div>
        </div>
      </div>
      <nav>
        <a href="#sobre">Sobre</a>
        <a href="#conteudo">Conteúdo</a>
        <a href="#depoimentos">Depoimentos</a>
        <a href="#faq">FAQ</a>
      </nav>
    </header>

    <!-- HERO -->
    <main class="hero">
      <div class="card">
        <h1 class="title">Faça sua primeira venda usando apenas tráfego orgânico</h1>
        <p class="subtitle">Táticas testadas para Instagram, Reels, SEO, mensagens diretas que convertem e roteiro de ofertas — sem gastar com anúncios.</p>

        <div class="meta">
          <div class="price">R$29,90</div>
          <div class="small" style="margin-left:8px">ou negocie via WhatsApp</div>
        </div>

        <div class="features" aria-hidden>
          <div class="feature">Passo a passo</div>
          <div class="feature">Modelos de mensagem</div>
          <div class="feature">Estratégia para Reels</div>
          <div class="feature">Planilha simples</div>
        </div>

        <div class="actions">
          <!-- Botão para WhatsApp com mensagem pronta -->
          <button class="btn btn-buy" onclick="openWhatsApp()">
            📲 Comprar pelo Zap
          </button>

          <!-- Botão para abrir modal de vídeo -->
          <button class="btn btn-video" onclick="location.href='#video'">
            ▶️ Assistir prévia
          </button>

          <!-- Link de pagamento (substitua pelo seu gateway) -->
          <a class="btn" id="paymentLink" href="[LINK_DE_PAGAMENTO]" target="_blank" rel="noopener" style="border:2px solid #e6e9ef;border-radius:12px;padding:10px 14px">
            💳 Pagar com cartão
          </a>
        </div>

        <p class="small" style="margin-top:12px">Após o pagamento você receberá o PDF por e-mail e/ou link direto no WhatsApp — ou me mande "Comprovante" no zap.</p>

        <!-- Formulário simples para capturar e-mail (opcional) -->
        <form id="leadForm" onsubmit="submitLead(event)" style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap">
          <input type="email" id="email" placeholder="Seu melhor e-mail" required style="flex:1;padding:10px;border-radius:10px;border:1px solid #e6eef6"/>
          <input type="text" id="nome" placeholder="Seu nome (opcional)" style="width:220px;padding:10px;border-radius:10px;border:1px solid #e6eef6"/>
          <button class="btn" style="background:#111827;color:white;border-radius:10px;padding:10px 14px;" type="submit">Guardar e-mail</button>
        </form>
      </div>

      <!-- Lateral com a capa e vídeo -->
      <aside>
        <div class="card cover">
          <!-- Capa do eBook -->
          <img src="[URL_DA_CAPA_DO_EBOOK]" alt="Capa do eBook - Primeira Venda no Orgânico"/>

          <div style="padding:14px">
            <div style="font-weight:800;margin-bottom:6px">O que você vai aprender</div>
            <ul style="margin:0;padding-left:18px;color:var(--muted)">
              <li>Como achar público sem anúncios</li>
              <li>Roteiro de DM que converte</li>
              <li>Estrutura de oferta simples</li>
              <li>Checklist para 7 dias</li>
            </ul>

            <!-- Vídeo embutido (troque o ID pelo seu vídeo no YouTube) -->
            <div id="video" style="margin-top:12px">
              <div class="video-wrap">
                <iframe src="https://www.youtube.com/embed/ID_DO_SEU_VIDEO?rel=0" title="Prévia do eBook - Primeira Venda no Orgânico" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
              </div>
            </div>

            <div style="margin-top:12px" class="small">Vídeo: 5 min — resumo rápido com passo a passo.</div>
          </div>
        </div>
      </aside>
    </main>

    <!-- SOBRE -->
    <section id="sobre" class="card">
      <h2>Sobre o eBook</h2>
      <p>Esse eBook foi feito para quem nunca vendeu online e quer a primeira conversa que vira venda — sem investir em tráfego pago. Contém scripts prontos, exemplos reais e um plano de 7 dias para testar sua oferta.</p>

      <div style="display:flex;gap:12px;align-items:center;margin-top:12px">
        <div class="author">
          <img src="[URL_DA_SUA_FOTO]" alt="[Seu Nome]" />
          <div>
            <div style="font-weight:800">[Seu Nome]</div>
            <div class="small">Especialista em tráfego orgânico e vendas diretas</div>
          </div>
        </div>

        <div style="margin-left:auto">
          <div class="badge">Garantia de Satisfação</div>
        </div>
      </div>
    </section>

    <!-- CONTEÚDO / O QUE VEM DENTRO -->
    <section id="conteudo">
      <h2>O que tem dentro (sumário)</h2>
      <div class="grid-3" style="margin-top:12px">
        <div class="card">
          <h3>Módulo 1</h3>
          <p class="small">Preparação: identidade, público e oferta clara.</p>
        </div>
        <div class="card">
          <h3>Módulo 2</h3>
          <p class="small">Conteúdo que atrai: Reels, posts e SEO para perfil.</p>
        </div>
        <div class="card">
          <h3>Módulo 3</h3>
          <p class="small">Conversão: DMs, modelos e fechamento sem push.</p>
        </div>
      </div>
    </section>

    <!-- DEPOIMENTOS -->
    <section id="depoimentos">
      <h2>Depoimentos</h2>
      <div class="grid-3" style="margin-top:12px">
        <div class="testimonial">
          <p style="margin:0 0 8px">"Em 3 dias apliquei o roteiro e fechei minha primeira venda — sem anúncio!"</p>
          <div class="small">— Maria, Empreendedora</div>
        </div>
        <div class="testimonial">
          <p style="margin:0 0 8px">"SImples, direto ao ponto. As mensagens realmente funcionam."</p>
          <div class="small">— João, Produtor</div>
        </div>
        <div class="testimonial">
          <p style="margin:0 0 8px">"Adorei o plano de 7 dias, ficou fácil executar."</p>
          <div class="small">— Ana, Coach</div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="card">
      <h2>Perguntas frequentes</h2>
      <div class="faq-item">
        <strong>Quando recebo o eBook?</strong>
        <p class="small">Depois do pagamento, você recebe link por e-mail ou envio manual pelo WhatsApp (conforme combinado).</p>
      </div>
      <div class="faq-item">
        <strong>Posso pedir reembolso?</strong>
        <p class="small">Temos 7 dias para reembolso caso você não esteja satisfeito (ver política no e-mail).</p>
      </div>
      <div class="faq-item">
        <strong>É só para Instagram?</strong>
        <p class="small">As estratégias são aplicáveis em várias plataformas (Instagram, TikTok, Facebook e perfis/SEO).</p>
      </div>
    </section>

    <footer class="footer">
      <div>© <span id="ano"></span> [Seu Nome]. Todos os direitos reservados.</div>
      <div style="margin-top:8px">Precisa de ajuda? <a href="https://wa.me/55SEUNUMERO?text=Ol%C3%A1%20preciso%20de%20ajuda%20com%20o%20eBook" target="_blank" rel="noopener">Chamar no WhatsApp</a></div>
    </footer>
  </div>

  <!-- Scripts básicos -->
  <script>
    // Atualiza ano no rodapé
    document.getElementById('ano').textContent = new Date().getFullYear();

    // Replace aqui: insira seu número no formato internacional sem sinais (ex: 5511999998888)
    const WA_NUMBER = "55SEUNUMERO";
    const WA_BASE = "https://wa.me/";

    function openWhatsApp(){
      const msg = encodeURIComponent("Olá! Quero comprar o eBook 'Primeira Venda no Orgânico'. Me passa as instruções, por favor.");
      const href = WA_BASE + WA_NUMBER + "?text=" + msg;
      window.open(href, "_blank");
    }

    // Simples: enviar e-mail para sua plataforma (este script só mostra como capturar dados)
    function submitLead(e){
      e.preventDefault();
      const email = document.getElementById('email').value;
      const nome = document.getElementById('nome').value;
      // Exemplo: salvar em localStorage ou enviar para sua API
      try {
        // salvar local
        const leads = JSON.parse(localStorage.getItem('leads') || "[]");
        leads.push({email, nome, date: new Date().toISOString()});
        localStorage.setItem('leads', JSON.stringify(leads));
        alert('E-mail guardado! Logo te envio novidades.');
        document.getElementById('leadForm').reset();
      } catch(err){
        console.error(err);
        alert('Erro ao guardar. Tenta novamente.');
      }
    }

    // Substitua o link de pagamento pelo seu sistema (MercadoPago, PagSeguro, PayPal, Stripe Checkout).
    // Exemplo: se usar MercadoPago, gere o link de preferência e coloque em #paymentLink href.
  </script>
</body>
</html>
