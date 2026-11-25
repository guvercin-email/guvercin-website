#!/usr/bin/env python3
"""Turkish content for guvercin.email.

A real translation, not a machine pass: the English pages and these pages say
the same things, but each reads as if it were written in its own language.
Output goes to /tr/.
"""
from common import *  # noqa: F401,F403

LANG = "tr"
DIR = "tr/"
LOCALE = "tr"

S = {
    "skip": "içeriğe geç",
    "home_label": "guvercin ana sayfa",
    "nav": [("features.html", "Özellikler"), ("download.html", "İndir"),
            ("open-source.html", "Açık Kaynak"), ("faq.html", "SSS"),
            ("contact.html", "İletişim")],
    "github_label": "guvercin GitHub'da",
    "theme_label": "temayı değiştir",
    "menu_label": "menü",
    "download": "İndir",
    "try_nav": "Çevrimiçi dene",
    "cta_h2": "gelen kutunu geri almaya hazır mısın?",
    "cta_p": "ücretsiz, açık kaynak ve hiçbir zaman eve telefon açmaz.",
    "cta_primary": "guvercin'i indir",
    "cta_secondary": "GitHub'da incele",
    "cta_try": "ya da önce tarayıcında dene →",
    "cta_small": "macOS · Windows · Linux — sürüm 0.1.0",
    "f_product": "Ürün", "f_project": "Proje", "f_support": "Destek",
    "f_legal": "Yasal",
    "f_features": "Özellikler", "f_download": "İndir", "f_beta": "Beta kanalı",
    "f_changelog": "Değişiklik günlüğü", "f_try": "Çevrimiçi dene",
    "f_github": "GitHub", "f_contribute": "Katkıda bulun", "f_roadmap": "Yol haritası",
    "f_license": "Lisans", "f_faq": "SSS", "f_contact": "İletişim",
    "f_bug": "Hata bildir", "f_privacy": "Gizlilik Politikası",
    "f_tagline": "açık kaynak e-posta, kendi bilgisayarında",
    "f_copyright": "© 2026 guvercin — açık kaynak, özenle yapıldı.",
    "lang_label": "Dil",
    "lang_site": "bu web sitesi",
    "lang_app": "uygulama bunları da konuşuyor",
    "lang_note": "web sitesi İngilizce ve Türkçe; uygulamanın kendisi 64 dille geliyor.",
}


# ============================================================== index.html ==
JSONLD = ""  # the structured data block lives on the English home page only

INDEX = f"""<main id="main">

<section class="hero">
  <div class="wrap center">
    <p class="overline"><span class="pill pill--yellow pill--dot">v0.1.0 · ücretsiz ve açık kaynak</span></p>
    <h1>gelen kutun, kendi masaüstünde</h1>
    <p class="lede">macOS, Windows ve Linux için ücretsiz ve açık kaynak bir e-posta uygulaması —
      takvim, kişiler ve görevler de içinde. postan bizim değil, senin makinende durur.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="download.html" data-os-button="long">Ücretsiz indir</a>
      <a class="btn btn--secondary btn--lg" href="{TRY}" target="_blank" rel="noopener">tarayıcında dene</a>
    </div>
    <p class="small">sonsuza dek ücretsiz · hesap gerekmez · takip yok ·
      <a href="{REPO}" target="_blank" rel="noopener">GitHub'da incele</a></p>
  </div>
  <div class="wrap hero__figure">
    {shot('mail', 'guvercin posta görünümü: solda klasör ağacı, ortada ileti listesi, sağda açık ileti', eager=True, cls='frame frame--hero')}
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <ul>
      <li>%100 açık kaynak</li>
      <li>reklam yok, takip yok</li>
      <li>her IMAP hesabıyla çalışır</li>
      <li>64 dil</li>
      <li>macOS, Windows ve Linux</li>
    </ul>
  </div>
</section>

<section class="section section--after-hero">
  <div class="wrap">
    <h2 class="visually-hidden">neler var</h2>
    <div class="grid grid--4">
      <div class="card card--link reveal" data-delay="0">
        {IC_STACK}
        <h3>bütün hesapların tek yerde</h3>
        <p>istediğin kadar IMAP ve SMTP hesabı ekle, ya da tek tıkla Google ile giriş yap.</p>
      </div>
      <div class="card card--link reveal" data-delay="1">
        {IC_CAL}
        <h3>postadan fazlası</h3>
        <p>aynı pencerede bir takvim, bir adres defteri ve bir görev listesi.</p>
      </div>
      <div class="card card--link reveal" data-delay="2">
        {IC_LOCK}
        <h3>tasarımı gereği özel</h3>
        <p>iletiler bilgisayarındaki şifreli yerel bir veritabanında durur; hiçbir şey bize
          yüklenmez.</p>
      </div>
      <div class="card card--link reveal" data-delay="3">
        {IC_HEART}
        <h3>senin kalır</h3>
        <p>açık kaynak, sonsuza dek ücretsiz, abonelik yok ve yükseltilecek bir şey yok.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="wrap center">
    <p class="overline">kurulum yok, hesap yok</p>
    <h2>indirmeden önce guvercin'i dene</h2>
    <p class="lede">canlı bir sürüm tarayıcında çalışıyor; diskine hiçbir şey koymadan posta
      görünümünü, takvimi ve ayarları gezebilirsin.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="{TRY}" target="_blank" rel="noopener">try.guvercin.email'i aç</a>
      <a class="btn btn--secondary btn--lg" href="download.html" data-os-button="long">guvercin'i indir</a>
    </div>
    <p class="small">asıl olan masaüstü uygulaması — bu sadece önce bir göz atmak için.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">
        {shot('offline', 'posta görünümünün üzerinde açılan ağ paneli internetin çevrimdışı olduğunu bildiriyor, ileti listesi yerel kopyadan okunmaya devam ediyor')}
      </div>
      <div class="reveal">
        <h2>masaüstü uygulaması gibi çalışan e-posta</h2>
        <p>sıralamasını değiştirebildiğin tam bir klasör ağacı, kapatabildiğin sohbet görünümü ve
          gerçekten okuduğun yere taşıyabildiğin bir okuma bölmesi. tema ve yazı boyutu hesap
          başına hatırlanır, yani iş hesabın kişisel hesabına hiç benzemek zorunda değil.</p>
        <p>arama yerel veritabanı üzerinde çalışır; yani sinyalin olmadığı bir trende de çalışır.
          ekleri ve satır içi görselleri de öyle.</p>
        <p><a href="features.html">bütün özellikleri gör →</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="wrap prose">
    <h2>postanı biz okuyamayız, başkası da okuyamaz</h2>
    <p>bir guvercin bulutu yok. uygulama bilgisayarından doğrudan kendi sağlayıcına bağlanır ve
      tuttuğu her şey — iletiler, taslaklar, ekler, takvim etkinlikleri, kişiler, görevler —
      diskindeki yerel bir veritabanında durur. telemetri yok, çökme raporu yok, reklam yok ve
      zaten açılacak bir hesap da yok.</p>
    <p>satacak bir şeyimiz yok, çünkü hiçbir şey almıyoruz.</p>
    <p><a href="privacy.html">gizlilik politikasını oku →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>ilk sorulan sorular</h2>
    <div class="accordion">
      <details>
        <summary>guvercin gerçekten ücretsiz mi?</summary>
        <div class="answer">
          <p>evet. ücretsiz ve açık kaynak; abonelik yok, ücretli sürüm yok, yükseltilecek bir şey
            yok. yapamayacağın tek şey onu satmak.</p>
        </div>
      </details>
      <details>
        <summary>hangi e-posta sağlayıcıları çalışıyor?</summary>
        <div class="answer">
          <p>IMAP ve SMTP konuşan her sağlayıcı — Gmail, Outlook ve Hotmail, Yandex, iCloud,
            Fastmail, üniversiten, kendi sunucun. Google hesapları tek tıkla giriş yapabilir.</p>
        </div>
      </details>
      <details>
        <summary>postam nerede saklanıyor?</summary>
        <div class="answer">
          <p>kendi bilgisayarındaki yerel bir veritabanında. hiçbir şey sunucularımıza ulaşmaz,
            çünkü sunucu diye bir şey yok.</p>
        </div>
      </details>
    </div>
    <p style="margin-top:24px"><a href="faq.html">bütün soruları gör →</a></p>
  </div>
</section>

</main>
"""

# =========================================================== download.html ==
DOWNLOAD = f"""<main id="main">

<section class="section section--cream">
  <div class="wrap center">
    <h1>guvercin'i indir</h1>
    <p class="lede">ücretsiz ve açık kaynak. hesap yok, takip yok, şart yok.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="{RELEASES}" data-release-link data-os-button="long" target="_blank" rel="noopener">guvercin'i indir</a>
    </div>
    <p class="small">sürüm {VERSION} · yayın tarihi {RELEASE_DATE[LANG]} · yaklaşık {DMG_MB} MB · macOS 11 veya üzeri</p>
    <p class="small"><a href="#all-downloads">sistemin bu değil mi? bütün indirmeler ↓</a></p>
    <p class="small">kurmaya hazır değil misin? <a href="{TRY}" target="_blank" rel="noopener">guvercin'i çevrimiçi dene →</a></p>
  </div>
</section>

<section class="section" id="all-downloads">
  <div class="wrap">
    <h2>bütün indirmeler</h2>
    <p class="note">bütün paketler aynı herkese açık depodan çıkıyor ve aşağıdaki her bağlantı
      GitHub sürümler sayfasına gidiyor.</p>
    <div class="grid grid--3" style="margin-top:32px">

      <div class="card" data-os-card="macos">
        <p class="overline">macOS</p>
        <span data-os-pill></span>
        <h3>macOS 11 veya üzeri</h3>
        <p>Applications klasörüne sürüklediğin bir disk kalıbı. tek bir universal paket —
          aynı dosya hem Apple Silicon hem Intel'de çalışıyor, seçim yapman gerekmiyor.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">İndir (.dmg)</a>
        </div>
        <p class="small" style="margin-top:16px">biçim: .dmg</p>
      </div>

      <div class="card" data-os-card="windows">
        <p class="overline">Windows</p>
        <span data-os-pill></span>
        <h3>Windows 10 veya 11</h3>
        <p>guvercin'i Başlat menüne koyan ve istersen mailto: bağlantıları için kaydeden bir NSIS
          yükleyicisi.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Yükleyici (.exe)</a>
        </div>
        <p class="small" style="margin-top:16px">biçim: .exe · yükleyici henüz kod imzalı olmadığı
          için Windows bir SmartScreen uyarısı gösterebilir — Ek bilgi → Yine de çalıştır'ı seç.</p>
      </div>

      <div class="card" data-os-card="linux">
        <p class="overline">Linux</p>
        <span data-os-pill></span>
        <h3>64-bit Linux</h3>
        <p>iki yaygın dağıtım ailesi için yerel paketler. WebKitGTK 4.1 ve libsecret gerekiyor,
          ki çoğu masaüstünde zaten var.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Debian / Ubuntu (.deb)</a>
          <a class="btn btn--secondary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Fedora / RHEL (.rpm)</a>
        </div>
        <p class="small" style="margin-top:16px">biçimler: .deb ve .rpm</p>
      </div>

    </div>
  </div>
</section>

<section class="section section--alt" id="beta">
  <div class="wrap">
    <div class="callout">
      <p><span class="pill pill--blue">beta</span></p>
      <h2 style="font-size:28px">beta kanalı</h2>
      <p>beta paketleri yeni özellikleri önce alır ve kararsız olabilir. verinin nasıl saklandığını
        da değiştirebilirler, o yüzden önemsediğin şeylerin yedeğini al. bir şey bozulursa lütfen
        GitHub'da bize söyle — beta zaten bunun için var.</p>
      <div class="btn-row">
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">macOS için beta</a>
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">Windows için beta</a>
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">Linux için beta</a>
      </div>
      <p style="margin-top:16px"><a href="{PRERELEASES}" target="_blank" rel="noopener">GitHub'daki bütün ön sürümler →</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>sistem gereksinimleri</h2>
    <div class="table-wrap">
      <table class="table-stack">
        <thead>
          <tr><th scope="col">platform</th><th scope="col">gerekenler</th></tr>
        </thead>
        <tbody>
          <tr><td>macOS</td><td>macOS 11 Big Sur veya üzeri; Apple Silicon ya da Intel.</td></tr>
          <tr><td>Windows</td><td>Windows 10 veya 11, 64-bit.</td></tr>
          <tr><td>Linux</td><td>WebKitGTK 4.1 ve libsecret bulunan güncel bir 64-bit dağıtım.</td></tr>
          <tr><td>hepsi</td><td>yaklaşık 200 MB boş disk alanı, artı eşitlenen postan için yer; 4 GB RAM; ilk eşitleme için internet bağlantısı.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>kurulum</h2>
    <div class="grid grid--3" style="margin-top:32px">
      <div class="card">
        <h3>macOS</h3>
        <ol class="steps">
          <li>.dmg dosyasını aç</li>
          <li>guvercin'i Applications klasörüne sürükle</li>
          <li>ilk açılışta uygulamaya sağ tıklayıp Aç'ı seç ve onayla — paket henüz noter onaylı
            olmadığı için normal çift tıklama engellenir.</li>
        </ol>
      </div>
      <div class="card">
        <h3>Windows</h3>
        <ol class="steps">
          <li>.exe yükleyicisini çalıştır</li>
          <li>SmartScreen çıkarsa Ek bilgi → Yine de çalıştır'ı seç</li>
          <li>guvercin'i Başlat menüsünden aç.</li>
        </ol>
      </div>
      <div class="card">
        <h3>Linux</h3>
        <ol class="steps">
          <li><code>sudo dpkg -i guvercin_0.1.0_amd64.deb</code> ya da
            <code>sudo rpm -i guvercin-0.1.0.x86_64.rpm</code> ile kur</li>
          <li>bağımlılıklar eksikse <code>sudo apt -f install</code> çalıştır</li>
          <li>guvercin'i uygulama menünden aç.</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">
        {shot('signin', 'Google ile devam et düğmesi ve otomatik bulunan IMAP/SMTP ayarlarıyla hesap ekleme penceresi')}
      </div>
      <div class="reveal">
        <h2>üç adımda hesabını ekle</h2>
        <ol class="steps">
          <li>“Google ile devam et”i seç ya da e-posta adresini yaz</li>
          <li>tarayıcında onayla, ya da IMAP ve SMTP bilgilerini gir — guvercin bunları senin için
            bulmayı dener</li>
          <li>ilk eşitlemeyi bekle; sonrasında postan çevrimdışıyken de elinin altında.</li>
        </ol>
        <p>istediğin kadar hesap ekleyebilirsin ve her biri kendi yerel veritabanını tutar.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap prose">
    <h2>kendin derle</h2>
    <p>kaynak herkese açık; indirdiğin uygulama, derleyebileceğin uygulamanın aynısı.</p>
    <div class="code">
      <button class="copy-btn" type="button" hidden>kopyala</button>
      <pre><code>git clone {REPO}.git
cd guvercin-desktop
npm install
npm run app:build</code></pre>
    </div>
    <p class="note">platformun için Rust ve Tauri ön gereksinimleri gerekecek —
      <a href="{README}" target="_blank" rel="noopener">depodaki README</a> hepsini sayıyor.</p>
    <p><a href="{RELEASES}" target="_blank" rel="noopener">bütün değişiklik günlüğü →</a></p>
    <p>bir sorun mu var? <a href="mailto:support@guvercin.email">support@guvercin.email</a> adresine
      yaz — hepsini okuyoruz.</p>
  </div>
</section>

</main>
"""

# =========================================================== features.html ==
FEATURE_ANCHORS = [
    ("mail", "posta"), ("sign-in", "giriş"), ("composer", "yazma"),
    ("calendar", "takvim"), ("contacts", "kişiler"), ("tasks", "görevler"),
    ("offline", "çevrimdışı"), ("appearance", "görünüm"), ("keyboard", "klavye"),
    ("privacy", "gizlilik"),
]


def feature(anchor, title, media, paragraphs, bullets=None, flip=False):
    ps = "\n        ".join(f"<p>{p}</p>" for p in paragraphs)
    bl = ""
    if bullets:
        lis = "\n          ".join(f"<li>{b}</li>" for b in bullets)
        bl = f"\n        <ul>\n          {lis}\n        </ul>"
    cls = "split split--flip" if flip else "split"
    return f"""    <div class="{cls} feature-section" id="{anchor}">
      <div class="split__media reveal">
        {media}
      </div>
      <div class="reveal">
        <h2>{title}</h2>
        {ps}{bl}
      </div>
    </div>
"""


FEATURES_BODY = "".join([
    feature("mail", "uslu duran bir gelen kutusu",
            shot("mail", "klasör ağacı, ileti listesi ve okuma bölmesinin yan yana durduğu posta görünümü"),
            ["birden fazla IMAP ve SMTP hesabı yan yana, her biri kendi yerel veritabanıyla. "
             "sıralamasını değiştirebildiğin tam bir klasör ağacı, özel etiket sıralaması ve "
             "okunmamış sayılarının nasıl görüneceğine dair bir seçim.",
             "sohbet görünümü açık ya da kapalı, ayarlanabilir bir okuma bölmesi, hesap başına tema "
             "ve yazı boyutu. arama — yapılandırılmış gelişmiş arama dahil — çevrimdışıyken de "
             "çalışmaya devam eder."],
            [".eml dosyalarını doğrudan aç — guvercin message/rfc822 dosyaları için kayıtlı bir uygulamadır",
             "bir iletiyi .eml ya da ham RFC822 olarak dışa aktar",
             "bir göndereni engelle, kural yerelde saklanır",
             "iletiyi yazdır"]),
    feature("sign-in", "Google için tek tık, diğer herkes için düz IMAP",
            shot("signin", "elle e-posta ve parola girişinin üstünde Google ile giriş sunan hesap ekleme penceresi"),
            ["“Google ile devam et”, sistem tarayıcında bir OAuth2 (XOAUTH2) PKCE akışı çalıştırır; "
             "yani parolan guvercin'e hiç yazılmaz ve hiçbir jeton arayüzden geçmez. uygulama çalışan "
             "bir OAuth istemcisiyle geliyor, o yüzden kutudan çıktığı gibi çalışır.",
             "diğer her şey için guvercin adresinden yola çıkıp sağlayıcının sunucularını yoklar; "
             "sunucu, port ve şifrelemeyi elle değiştirmene de izin verir. Gmail, Outlook ve Hotmail, "
             "Yandex, iCloud, Fastmail ve kendi sunucularınla çalışır."],
            flip=True),
    feature("composer", "düzgün yaz",
            shot("composer", "biçimlendirme şeridi, adres alanları ve iki ekli dosyası olan ayrı pencerede yazma ekranı"),
            ["biçimlendirme şeritli zengin metin editörü, sürükle bırak ekler ve ayrı bir yerel "
             "pencereye çıkarabildiğin bir yazma ekranı. taslaklar yerelde kaydedilir ve sonra "
             "gönderilebilir.",
             "dosya yöneticinde herhangi bir dosyaya sağ tıklayıp “guvercin ile gönder”i seçerek o "
             "dosya ekliyken bir ileti başlat — Windows ve Linux'ta otomatik olarak kaydedilir. "
             "macOS'te dosyayı pencereye sürükle ya da Birlikte Aç'ı kullan."]),
    feature("calendar", "haftan, aynı pencerede",
            shot("calendar", "yerleşik takvimin renkli etkinlikler içeren ay görünümü"),
            ["hesap başına birden fazla takvim, kendi sunucuna karşı CalDAV eşitlemesi, Google Takvim "
             "eşitlemesi ve .ics içe/dışa aktarımı.",
             "başka bir sekmede değil, postanın yanında durur; bütün mesele de bu."],
            flip=True),
    feature("contacts", "gerçekten senin olan bir adres defteri",
            shot("contacts", "aranabilir liste ve kişi detay panelinin bulunduğu kişiler görünümü"),
            ["kişi listeleri ve gruplar, vCard içe/dışa aktarımı ve Google Kişiler eşitlemesi.",
             "gönderen avatarları ileti görüntülenirken çözülür, adresler sen yazarken tamamlanır."]),
    feature("tasks", "postanın yanında yapılacaklar",
            shot("tasks", "yan yana üç görev listesi, kimi maddeler tamamlanmış"),
            ["birden fazla görev listesi, tamamlananları tek dokunuşla temizleme ve Google Görevler "
             "eşitlemesi — yani o e-postayla ilgili yapman gereken şey, e-postanın yanında duruyor."],
            flip=True),
    feature("offline", "uçakta da çalışan bir posta uygulaması",
            shot("offline", "internetin çevrimdışı olduğunu bildiren ağ paneli, arkasında ileti listesi hâlâ okunabilir durumda"),
            ["posta kutuları yerel bir veritabanına eşitlenir; böylece postan, eklerin, satır içi "
             "görsellerin ve arama bağlantı olmadan da çalışmaya devam eder.",
             "çevrimdışıyken yaptığın her şey kuyruğa alınır ve döndüğünde tekrar oynatılır; istediğin "
             "an tam ya da posta kutusu bazında eşitleme başlatabilirsin."]),
    feature("appearance", "kendine göre ayarla",
            shot("appearance", "açık, koyu ve sistemi izle tema kartlarının altında yazı tipi seçicisini gösteren görünüm ayarları"),
            ["açık ve koyu temalar, artı sistemi izleme, ve dosyadan içe aktarabildiğin özel temalar. "
             "uygulamayla birlikte 64 arayüz dili geliyor; hepsi depo üzerinden katkı olarak geldi.",
             "guvercin Hanken Grotesk ile gelir ve okuma yazı tipini hesap başına değiştirmene izin verir."],
            bullets=["Türkçe · English · Deutsch · Français · Español · Português",
                     "Русский · Українська · Polski · Nederlands · Svenska · Norsk",
                     "العربية · فارسی · हिन्दी · বাংলা · ไทย · 日本語 · 한국어 · 中文",
                     "…ve 40 tane daha"],
            flip=True),
    feature("keyboard", "her kısayol senin, değiştirebilirsin",
            shot("keyboard", "tuş görselleri ve anahtarlarıyla posta ve gezinme kısayollarını listeleyen kısayol ayarları"),
            ["kısayollar posta işlemleri, gezinme ve sekmeler, görünüm ve yerleşim, yazma ve uygulama "
             "diye gruplanmıştır; her biri tek tek yeniden atanabilir ya da kapatılabilir."]),
    feature("privacy", "hiçbir şey görmeyelim diye tasarlandı",
            shot("privacy", "saklanan verinin SQLCipher ve XChaCha20 üzerinden AES-256 ile şifrelendiğini gösteren, açık konumdaki şifreleme ayarı"),
            ["her veritabanı SQLCipher ile şifrelidir, önbelleğe alınan dosyalar da "
             "XChaCha20-Poly1305 ile mühürlenir; bu kapatılamaz. onları açan anahtar, kullanıcı "
             "profilindeki bir dosyadır ve senin adına çalışan her şey onu okuyabilir — bu yüzden "
             "tam disk şifrelemesini açık tut; ayrıntısı SECURITY.md'de.",
             "uzak görseller sen istemeden yüklenmez; yani bir iletiyi açmak gönderene hiçbir şey "
             "söylemez. uygulamanın hiçbir yerinde telemetri, çökme raporu ya da reklam yoktur. "
             "kaldırırken guvercin yerel verini silmeyi önerir — ya da yeniden kurulum için "
             "saklamayı."],
            flip=True),
])

KEYCAPS = [
    ("yeni ileti", ["Ctrl", "N"]), ("yanıtla", ["Ctrl", "R"]),
    ("tümünü yanıtla", ["Ctrl", "Shift", "R"]), ("ilet", ["Ctrl", "Shift", "F"]),
    ("arşivle", ["E"]), ("okundu işaretle", ["Ctrl", "U"]), ("ara", ["Ctrl", "F"]),
    ("eşitle", ["F5"]), ("gönder", ["Ctrl", "Enter"]), ("taslağı kaydet", ["Ctrl", "S"]),
    ("ayarlar", ["Ctrl", ","]), ("sekmeyi kapat", ["Ctrl", "W"]),
]
KEYCAP_HTML = "\n      ".join(
    "<li><span>" + name + "</span> " + " ".join(f"<kbd>{k}</kbd>" for k in keys) + "</li>"
    for name, keys in KEYCAPS
)

FEATURES = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>guvercin'in yaptığı her şey</h1>
    <p class="lede">bir posta uygulaması, bir takvim, bir adres defteri ve bir görev listesi —
      tek bir yerel pencerede, kendi makinende.</p>
    <nav aria-label="bu sayfadaki özellikler" style="margin-top:32px">
      <ul class="anchor-list">
        {''.join(f'<li><a href="#{a}">{l}</a></li>' for a, l in FEATURE_ANCHORS)}
      </ul>
    </nav>
  </div>
</section>

<section class="section">
  <div class="wrap">
{FEATURES_BODY}  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>hiçbir şeyi değiştirmezsen, varsayılanlar</h2>
    <ul class="keycaps" style="margin-top:24px">
      {KEYCAP_HTML}
    </ul>
  </div>
</section>

</main>
"""

# ======================================================== open-source.html ==
ROADMAP = [
    ("hesaplar arası birleşik arama", "planlanıyor"),
    ("PGP desteği", "planlanıyor"),
    ("daha fazla eşitleme sağlayıcısı", "planlanıyor"),
    ("imzalı ve noter onaylı paketler", "üzerinde çalışılıyor"),
    ("bir mobil yardımcı uygulama", "planlanıyor"),
]
ROADMAP_HTML = "\n      ".join(
    f'<li><span class="pill">{state}</span><span>{name}</span></li>' for name, state in ROADMAP
)

OPEN_SOURCE = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap prose">
    <h1>açık kaynak, çünkü bu senin postan</h1>
    <p>e-posta, çoğu insanın sahip olduğu en kişisel arşivdir. parola sıfırlamaları, sözleşmeler,
      fiyatta anlaştığın konuşma, artık aramızda olmayan insanlardan mektuplar. böyle bir arşivi
      okuyan yazılımın kendisi de okunabilir olmalı.</p>
    <p>guvercin'in her satırı herkese açık. herkes, bu sitenin söylediği şeyi yapıp yapmadığını —
      ve başka bir şey yapmadığını — kontrol edebilir.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="card">
      <p class="overline">depo</p>
      <h2 style="font-size:28px">guvercin-email/guvercin-desktop</h2>
      <p>Tauri, Rust ve React ile yazılmış bir masaüstü e-posta uygulaması. posta, takvim, kişiler
        ve görevler, SQLite ile yerelde saklanır.</p>
      <p>
        <span class="pill">yıldız: GitHub'da</span>
        <span class="pill">çatal: GitHub'da</span>
        <span class="pill">konu: GitHub'da</span>
        <span class="pill">v0.1.0</span>
      </p>
      <div class="btn-row" style="margin-top:8px">
        <a class="btn btn--primary" href="{REPO}" target="_blank" rel="noopener">depoyu aç</a>
        <a class="btn btn--secondary" href="{ISSUES}" target="_blank" rel="noopener">konulara göz at</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>teknoloji</h2>
    <div class="grid grid--4" style="margin-top:32px">
      <div class="card reveal" data-delay="0"><h3>Tauri</h3><p>yerel kabuk. uygulama başına paketlenmiş
        bir tarayıcı yerine tek küçük bir pencere.</p></div>
      <div class="card reveal" data-delay="1"><h3>Rust</h3><p>posta motoru — IMAP, SMTP ve eşitleme.
        başkalarının iletilerini ayrıştırırken bellek güvenliği önemlidir.</p></div>
      <div class="card reveal" data-delay="2"><h3>React</h3><p>arayüz. tanıdık bir katman, yani bir
        düzeltme göndermek için önce yeni bir arayüz kiti öğrenmek gerekmiyor.</p></div>
      <div class="card reveal" data-delay="3"><h3>SQLite</h3><p>yerel depolama. postan senin sahibi
        olduğun bir diskte, senin sahibi olduğun bir dosyada biter.</p></div>
    </div>
  </div>
</section>

<section class="section" id="contribute">
  <div class="wrap">
    <h2>nasıl katkıda bulunulur</h2>
    <p class="note">biz küçük bir açık kaynak projesiyiz, o yüzden bunların her biri gerçekten
      işe yarıyor.</p>
    <div class="grid grid--3" style="margin-top:32px">
      <div class="card">
        {IC_CODE}
        <h3>kod yaz</h3>
        <p>indirme sayfasındaki parçacıkla kaynaktan derle, iyi bir başlangıç konusu seç ve bir pull
          request aç.</p>
        <p><a href="{CONTRIB}" target="_blank" rel="noopener">katkı notları →</a></p>
      </div>
      <div class="card">
        {IC_MAIL}
        <h3>guvercin'i çevir</h3>
        <p>uygulama 64 dille geliyor; hepsi depo üzerinden katkı olarak geldi. bir dil eklemek,
          locales klasörüne tek bir JSON dosyası eklemek demek.</p>
        <p><a href="{LOCALES}" target="_blank" rel="noopener">locales klasörü →</a></p>
      </div>
      <div class="card">
        {IC_BUG}
        <h3>bildir ve dene</h3>
        <p>işletim sistemini, uygulama sürümünü ve tekrar üretme adımlarını yazarak konu aç. beta
          kanalını dene ve neyin bozulduğunu bize söyle.</p>
        <p><a href="{ISSUES}" target="_blank" rel="noopener">konu aç →</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="roadmap">
  <div class="wrap prose">
    <h2>yol haritası</h2>
    <p class="note">fikir verir, söz vermez. sırası kesin olmayan, bundan sonra yapmak
      istediklerimiz.</p>
    <ul class="checklist">
      {ROADMAP_HTML}
    </ul>
    <p>başka bir şey mi istiyorsun? <a href="{ISSUES}" target="_blank" rel="noopener">bir konu aç</a> —
      yol haritası insanların gerçekten istediklerini takip ediyor.</p>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <div class="callout">
      <h2 style="font-size:28px">güvenlik bildirimi</h2>
      <p>bir açık mı buldun? ayrıntıları ve nasıl tekrar üretileceğini
        <a href="mailto:support@guvercin.email">support@guvercin.email</a> adresine yaz. herkese açık
        bir konu açmadan önce lütfen bize düzeltmeyi yayınlama şansı ver.</p>
      <p>ödül programımız yok — küçük bir projeyiz — ama istersen sürüm notlarında adın geçer.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap prose">
    <div class="summary-box">
      <h2 style="font-size:24px">üç satırda lisans</h2>
      <p>evde ya da işte, istediğin kadar, ücretsiz kullan.</p>
      <p>oku, değiştir, çatalla ve değişikliklerini aynı koşullarla paylaş.</p>
      <p>satma, ya da değerinin büyük kısmı ondan gelen ücretli bir ürün veya hizmet kurma.</p>
      <p><a href="license.html">tam lisansı oku →</a></p>
    </div>
  </div>
</section>

</main>
"""

# ================================================================ faq.html ==
FAQ_GROUPS = [
    ("temeller", [
        ("guvercin gerçekten ücretsiz mi?",
         ["evet. ücretsiz ve açık kaynak; abonelik yok, ücretli sürüm yok, yükseltilecek bir şey "
          "yok. yeniden satamazsın, ama istediğin kadar kullanabilirsin."]),
        ("hangi e-posta sağlayıcıları çalışıyor?",
         ["IMAP ve SMTP konuşan her sağlayıcı — Gmail, Outlook ve Hotmail, Yandex, iCloud, Fastmail, "
          "üniversiten, kendi sunucun. Google hesapları tek tıkla giriş yapabilir."]),
        ("guvercin bana bir e-posta adresi veriyor mu?",
         ["hayır. zaten sahip olduğun posta kutuları için bir istemci, bir posta sağlayıcısı değil."]),
        ("“guvercin” ne demek?",
         ["Türkçede posta taşıyan kuşun adı. marka da bundan geliyor."]),
        ("ne kadar bitmiş durumda?",
         ["sürüm 0.1.0 erken bir sürüm. yapan insanlar her gün kullanıyor, ama pürüzler bekle ve "
          "lütfen bildir."]),
    ]),
    ("gizlilik ve güvenlik", [
        ("postam nerede saklanıyor?",
         ["kendi bilgisayarındaki yerel bir veritabanında. hiçbir şey sunucularımıza ulaşmaz, çünkü "
          "sunucu diye bir şey yok."]),
        ("analitik topluyor musunuz?",
         ["telemetri yok, kullanım istatistiği yok, çökme raporu yok, reklam yok, hiçbir türden takip "
          "kodu yok — ne uygulamada ne bu sitede."]),
        ("parolam güvende mi?",
         ["kimlik bilgileri ve OAuth jetonları SQLCipher ile şifreli yerel veritabanında tutulur, "
          "hiçbir zaman düz metin olarak değil. Google girişinde uygulama parolanı hiç görmez. şunu "
          "bil: o veritabanının anahtarı işletim sistemi anahtarlığında değil, kullanıcı profilindeki "
          "bir dosyadadır; yani kaybolan bir diske karşı korur, senin adına çalışan bir şeye karşı "
          "değil."]),
        ("gönderenler e-postalarını açtığımı anlayabilir mi?",
         ["hayır — uzak görseller sen \"görselleri yükle\" diyene kadar tutulur, dolayısıyla bir "
          "iletiyi açmak gönderene hiçbir şey göndermez. takip pikselini etkisiz kılan da budur."]),
        ("uygulamayı kaldırırsam verilerime ne olur?",
         ["Ayarlar'da düzgün bir kaldırma akışı var; yerel verinin silinmesini mi yoksa ileride "
          "yeniden kurulum için saklanmasını mı istediğini sorar."]),
    ]),
    ("kurulum ve kullanım", [
        ("çevrimdışı çalışıyor mu?",
         ["evet. eşitlenmiş posta, ekler ve arama bağlantı olmadan çalışır; yaptığın her şey yeniden "
          "bağlandığında tekrar oynatılır."]),
        ("macOS geliştirici doğrulanamadığı için uygulamayı açamıyorum diyor.",
         ["uygulamaya sağ tıklayıp Aç'ı seç ve bir kez onayla. paketler henüz noter onaylı değil; "
          "imzalama yol haritasında."]),
        ("Windows bir SmartScreen uyarısı gösteriyor.",
         ["Ek bilgi, sonra Yine de çalıştır'ı seç. sebebi aynı: yükleyici henüz kod imzalı değil."]),
        ("Linux'ta kullanabilir miyim?",
         ["evet, .deb ya da .rpm paketiyle. WebKitGTK ve libsecret gerekiyor, ki çoğu masaüstünde "
          "zaten var."]),
        ("kararlı ile beta arasındaki fark ne?",
         ["beta özellikleri önce alır, bozulabilir ya da verinin nasıl saklandığını değiştirebilir; "
          "gerçekten güvendiğin posta için kararlı sürümü öneriyoruz."]),
        ("guvercin'i işte ya da şirketimde kullanabilir miyim?",
         ["evet, kurum içi kullanım için. yapamayacağın tek şey onu satmak ya da üzerine ücretli bir "
          "hizmet kurmak."]),
        ("guvercin'i varsayılan posta uygulamam nasıl yaparım?",
         ["ilk açılışta bunu öneriyor, sonrasında Ayarlar'dan değiştirebilirsin — ondan sonra mailto: "
          "bağlantıları bir yazma penceresi açar."]),
        ("klavye kısayollarını değiştirebilir miyim?",
         ["hepsini, tek tek, Ayarlar'dan."]),
        ("mobil uygulama var mı?",
         ["bugün yok. yol haritasında bir yardımcı uygulama var, fazlası değil."]),
        ("nasıl hata bildiririm ya da özellik isterim?",
         [f'<a href="{ISSUES}" target="_blank" rel="noopener">GitHub</a> üzerinde bir konu aç, ya da '
          'işletim sistemini, uygulama sürümünü ve bozulmadan önce ne yaptığını yazarak '
          '<a href="mailto:support@guvercin.email">support@guvercin.email</a> adresine yaz.']),
    ]),
]


def faq_group(title, items):
    rows = []
    for q, answers in items:
        ps = "".join(f"<p>{a}</p>" for a in answers)
        rows.append(
            f"      <details>\n        <summary>{q}</summary>\n"
            f"        <div class=\"answer\">{ps}</div>\n      </details>\n"
        )
    return (f'    <h2>{title}</h2>\n    <div class="accordion" style="margin-bottom:48px">\n'
            + "".join(rows) + "    </div>\n")


FAQ = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>sorular ve destek</h1>
    <p class="lede">insanların kurmadan önce ve kurduktan sonra sorduğu şeyler. sorun burada yoksa
      bize yaz — o adresi bir insan okuyor.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
{''.join(faq_group(t, items) for t, items in FAQ_GROUPS)}  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>hâlâ yardım mı lazım?</h2>
    <div class="grid grid--2" style="margin-top:32px">
      <div class="card">
        {IC_MAIL}
        <h3>hâlâ takıldın mı?</h3>
        <p>işletim sistemin ve uygulama sürümünle birlikte
          <a href="mailto:support@guvercin.email">support@guvercin.email</a> adresine yaz. hepsini
          okuyoruz.</p>
      </div>
      <div class="card">
        {IC_BUG}
        <h3>bir hata mı buldun?</h3>
        <p>tekrar üretme adımlarıyla <a href="{ISSUES}" target="_blank" rel="noopener">GitHub</a>
          üzerinde bir konu aç; doğrudan düzeltebilecek insanlara gider.</p>
      </div>
    </div>
  </div>
</section>

</main>
"""

# ============================================================ contact.html ==
CONTACT = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>bize ulaş</h1>
    <p class="lede">küçük bir açık kaynak projesi, gerçek e-postayla ulaşılabilir.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2 class="visually-hidden">bize ulaşma yolları</h2>
    <div class="grid grid--3">
      <div class="card reveal" data-delay="0">
        {IC_MAIL}
        <h3>genel ve iş birlikleri</h3>
        <p>proje hakkında sorular, basın, iş birlikleri.</p>
        <p><a class="btn btn--secondary btn--sm" href="mailto:hello@guvercin.email">hello@guvercin.email</a></p>
      </div>
      <div class="card reveal" data-delay="1">
        {IC_BUG}
        <h3>destek ve hata bildirimi</h3>
        <p>kurulum sorunu, bağlanmayan bir hesap, çöken bir şey. işletim sistemini ve uygulama
          sürümünü yazarsan daha hızlı yanıt alırsın.</p>
        <p><a class="btn btn--secondary btn--sm" href="mailto:support@guvercin.email">support@guvercin.email</a></p>
      </div>
      <div class="card reveal" data-delay="2">
        {IC_CODE}
        <h3>geliştiriciler</h3>
        <p>özellik istekleri, yamalar ve herkese açık konuşulması daha iyi olan her şey.</p>
        <p>
          <a class="btn btn--secondary btn--sm" href="{ISSUES}" target="_blank" rel="noopener">GitHub Issues</a>
        </p>
        <p><a href="{DISCUSSIONS}" target="_blank" rel="noopener">GitHub Discussions →</a></p>
      </div>
    </div>
    <p class="note" style="margin-top:32px">küçük bir açık kaynak projesiyiz, o yüzden birkaç dakika
      değil birkaç gün içinde yanıt bekle.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap prose">
    <h2>yazmadan önce</h2>
    <ul>
      <li><a href="faq.html">SSS</a>'ye bak — kurulum sorularının çoğu orada yanıtlanıyor.</li>
      <li><a href="{ISSUES}" target="_blank" rel="noopener">açık konulara</a> bak, belki biri zaten
        bildirmiştir.</li>
      <li>işletim sistemini ve guvercin sürümünü yaz, Ayarlar → Hakkında bölümünden bulabilirsin.</li>
    </ul>
    <p>güvenlik sorunları için <a href="mailto:support@guvercin.email">support@guvercin.email</a>
      adresine yaz ve düzeltme çıkana kadar lütfen herkese açık bir konu açma.</p>
    <p class="note">bu sayfada iletişim formu yok, çünkü onu alacak bir sunucu yok. gönderdiğin
      hiçbir şey bir gelen kutusundan başka yere gitmiyor.</p>
  </div>
</section>

</main>
"""

# ============================================================ privacy.html ==
PRIVACY = """<main id="main">

<section class="section">
  <div class="wrap prose">
    <h1>Gizlilik Politikası</h1>
    <p class="note">sade özet: guvercin'in sunucusu yok, dolayısıyla toplayabileceğimiz bir şey de
      yok. bu sayfa bunu ayrıntılı anlatıyor.</p>
    <p class="small">son güncelleme 26 Temmuz 2026</p>

    <div class="toc" style="margin:32px 0">
      <h2 style="font-size:16px;margin-bottom:12px">bu sayfada</h2>
      <ul>
        <li><a href="#app">uygulama</a></li>
        <li><a href="#third-parties">üçüncü taraflar</a></li>
        <li><a href="#analytics">analitik ve telemetri</a></li>
        <li><a href="#website">web sitesi</a></li>
        <li><a href="#email">e-posta</a></li>
        <li><a href="#children">çocuklar</a></li>
        <li><a href="#rights">haklarınız</a></li>
        <li><a href="#changes">değişiklikler</a></li>
      </ul>
    </div>

    <p>guvercin açık kaynak bir masaüstü e-posta uygulamasıdır. Bu politika hem guvercin.email
      web sitesini hem de masaüstü uygulamasını kapsar.</p>

    <h2 id="app" style="font-size:24px">Uygulama</h2>
    <p>guvercin tamamen kendi bilgisayarınızda çalışır. İletileriniz, taslaklarınız, ekleriniz,
      takvim etkinlikleriniz, kişileriniz ve görevleriniz cihazınızdaki yerel bir veritabanında
      saklanır. Hesap kimlik bilgileriniz ve OAuth jetonlarınız da hiçbir zaman düz metin olarak
      değil, bu şifreli veritabanının içinde tutulur; onu açan anahtar kullanıcı profilinizdeki bir
      dosyadır. Hiçbir sunucu, hesap ya da bulut depolama işletmiyoruz —
      verileriniz bize hiçbir zaman yüklenmez, çünkü gidebileceği bir yer yok.</p>

    <h2 id="third-parties" style="font-size:24px">Üçüncü taraflar</h2>
    <p>Bir hesap eklediğinizde uygulama, bilgisayarınızdan doğrudan kendi e-posta, takvim veya kişi
      sağlayıcınıza bağlanır (örneğin Gmail, Outlook, Yandex ya da kendi IMAP/SMTP veya CalDAV
      sunucunuz). Bu bağlantılar ilgili sağlayıcının gizlilik politikasına tabidir. İletilerin
      içindeki uzak görseller siz yüklemeyi seçene kadar hiç çekilmez; gönderen avatarları üçüncü
      taraf servislerden istenebilir. İkisi de Ayarlar'dan kapatılabilir. Bir e-postadaki bağlantıyı açmak onu kendi tarayıcınızda açar.</p>

    <h2 id="analytics" style="font-size:24px">Analitik ve telemetri</h2>
    <p>Uygulama hiçbir analitik, kullanım istatistiği veya çökme telemetrisi toplamaz ve içinde
      reklam ya da takip kodu bulunmaz.</p>

    <h2 id="website" style="font-size:24px">Web sitesi</h2>
    <p>guvercin.email statik bir sitedir. Google Analytics 4, sayfa görüntülemelerini ve tahmini tekil ziyaretçi sayısını ölçer. Google, kullanım ve cihaz verilerini
      kendi gizlilik koşullarına göre işleyebilir. Tarayıcınızda açık/koyu tema ve dil tercihiniz
      saklanır. Barındırma sağlayıcımız güvenlik ve güvenilirlik için standart sunucu günlükleri
      (IP adresi, tarayıcı türü, istenen sayfa) tutabilir. İndirmeler GitHub üzerinden sunulur; bir
      sürüm indirdiğinizde GitHub'ın kendi gizlilik politikası geçerlidir.</p>

    <h2 id="email" style="font-size:24px">E-posta</h2>
    <p><a href="mailto:hello@guvercin.email">hello@guvercin.email</a> veya
      <a href="mailto:support@guvercin.email">support@guvercin.email</a> adresine yazarsanız,
      iletinizi ve adresinizi yalnızca size yanıt vermek ve konunun kaydını tutmak için gereken
      süre boyunca saklarız; hiçbir zaman pazarlama için kullanmayız.</p>

    <h2 id="children" style="font-size:24px">Çocuklar</h2>
    <p>guvercin 13 yaşın altındaki çocuklara yönelik değildir.</p>

    <h2 id="rights" style="font-size:24px">Haklarınız</h2>
    <p>Hakkınızda hiçbir kişisel veri tutmadığımız için dışa aktaracağımız veya sileceğimiz bir şey
      yok — verileriniz zaten kendi elinizde, kendi diskinizde. Bize e-posta yazdıysanız ve o
      yazışmanın silinmesini istiyorsanız, söyleyin, sileriz.</p>

    <h2 id="changes" style="font-size:24px">Değişiklikler</h2>
    <p>Bu politika değişirse yukarıdaki tarih güncellenir ve değişiklik web sitesinin herkese açık
      depo geçmişinde görünür olur.</p>

    <p>Sorular: <a href="mailto:hello@guvercin.email">hello@guvercin.email</a></p>
  </div>
</section>

</main>
"""

# ============================================================ license.html ==
LICENSE = f"""<main id="main">

<section class="section">
  <div class="wrap prose">
    <h1>lisans</h1>
    <p class="lede">kullanması serbest, okuması serbest, değiştirmesi serbest — satması değil.</p>

    <div class="summary-box" style="margin:32px 0">
      <p><strong>guvercin, Commons Clause koşuluyla birlikte Apache License 2.0 altında
        lisanslanmıştır.</strong></p>
      <p><strong>Yapabilecekleriniz:</strong> evde ya da işte ücretsiz kullanmak; kaynağı okumak,
        incelemek ve değiştirmek; çatallamak ve değişikliklerinizi paylaşmak; aynı koşullarla
        yeniden dağıtmak.</p>
      <p><strong>Yapamayacaklarınız:</strong> yazılımı satmak, yeniden satmak, karşılığında abonelik
        ücreti almak ya da değerinin büyük kısmı ondan gelen ücretli bir ürün veya hizmet sunmak.</p>
    </div>

    <h2 style="font-size:24px">sözcükler hakkında dürüst bir not</h2>
    <p>Commons Clause, Apache 2.0'ın üzerine eklenmiş ek bir koşuldur. Bu yüzden guvercin,
      OSI onaylı açık kaynak değil, kaynağı erişilebilir bir yazılımdır. Bu sitede “açık kaynak”
      ifadesini günlük anlamıyla kullanıyoruz — kaynak herkese açık ve kendin derleyebilirsin — ve
      bunu gizlemektense burada açıkça söylemeyi tercih ediyoruz.</p>

    <h2 style="font-size:24px">telif</h2>
    <p>Copyright (c) 2026 Hidayet Erdem / Guvercin / Herdem.</p>

    <h2 style="font-size:24px">üçüncü taraf bildirimleri</h2>
    <p>uygulama, Hanken Grotesk yazı tipini SIL Open Font License altında dağıtır. bağımlılıkların
      geri kalanının lisansları depoda listelenmiştir.</p>

    <p style="margin-top:32px">
      <a class="btn btn--secondary" href="{LICENSE_FILE}" target="_blank" rel="noopener">tam lisans metnini oku →</a>
    </p>
  </div>
</section>

</main>
"""

# ================================================================ 404.html ==
NOTFOUND = """<main id="main">
<section class="section center">
  <div class="wrap">
    <img class="brand__mark--light" src="assets/img/logo-mark-light.svg" width="120" height="112" alt="">
    <img class="brand__mark--dark" src="assets/img/logo-mark-dark.svg" width="120" height="112" alt="">
    <h1 style="margin-top:24px">bu sayfa uçup gitmiş</h1>
    <p class="lede">kuş o adresi bulamadı. olur böyle şeyler.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="index.html">ana sayfaya dön</a>
      <a class="btn btn--secondary btn--lg" href="download.html">guvercin'i indir</a>
    </div>
  </div>
</section>
</main>
"""


PAGES = [
    ("index.html",
     "guvercin — macOS, Windows ve Linux için ücretsiz açık kaynak e-posta uygulaması",
     "guvercin, macOS, Windows ve Linux için ücretsiz ve açık kaynak bir masaüstü e-posta "
     "uygulaması. takvim, kişiler, görevler dahil. postan kendi makinende kalır.",
     "index.html", INDEX, JSONLD, True),
    ("download.html",
     "guvercin'i indir — macOS, Windows ve Linux",
     "guvercin'i macOS, Windows veya Linux için ücretsiz indir. .dmg, .exe, .deb ve .rpm paketleri, "
     "kurulum adımları, sistem gereksinimleri ve kaynaktan derleme.",
     "download.html", DOWNLOAD, "", True),
    ("features.html",
     "özellikler — guvercin",
     "posta, takvim, kişiler, görevler, çevrimdışı eşitleme, 64 dil ve değiştirilebilir kısayollar, "
     "tek bir yerel pencerede. guvercin ne yapar, gör ve ücretsiz indir.",
     "features.html", FEATURES, "", True),
    ("open-source.html",
     "açık kaynak — guvercin",
     "guvercin'in kaynağı herkese açık: Tauri, Rust, React ve SQLite. depoyu, yol haritasını ve "
     "nasıl katkıda bulunabileceğini gör, sonra ücretsiz indir.",
     "open-source.html", OPEN_SOURCE, "", True),
    ("faq.html",
     "sss ve destek — guvercin",
     "guvercin hakkında yanıtlar: ücreti, hangi sağlayıcıların çalıştığı, postanın nerede saklandığı, "
     "macOS, Windows ve Linux kurulumu ve nasıl yardım alacağın.",
     "faq.html", FAQ, "", True),
    ("contact.html",
     "iletişim — guvercin",
     "guvercin projesine e-postayla ulaş: genel sorular, destek ve hata bildirimi, ya da herkese "
     "açık konuşulacak her şey için GitHub. form yok, takip yok.",
     "contact.html", CONTACT, "", True),
    ("privacy.html",
     "gizlilik politikası — guvercin",
     "guvercin'in sunucusu, hesabı ve telemetrisi yok; dolayısıyla toplayacağımız bir şey de yok. "
     "uygulamanın ve bu sitenin verini nasıl ele aldığını oku.",
     "privacy.html", PRIVACY, "", False),
    ("license.html",
     "lisans — guvercin",
     "guvercin, Commons Clause koşuluyla Apache License 2.0 altındadır: evde ya da işte ücretsiz "
     "kullanılır, okunur ve değiştirilir, ama satılamaz.",
     "license.html", LICENSE, "", False),
    ("404.html",
     "sayfa bulunamadı — guvercin",
     "guvercin.email üzerinde böyle bir sayfa yok. ana sayfaya dön, ya da macOS, Windows ve Linux "
     "için ücretsiz açık kaynak guvercin e-posta uygulamasını indir.",
     "404.html", NOTFOUND, "", False),
]
