def get_greek_urls():
    return [
        "https://www.tovima.gr/2025/01/31/politics/nikos-androulakis-gia-tempi-resital-psematos-apo-tin-kyvernisi/",
        "https://www.ot.gr/2025/01/31/texnologia/texniti-noimosyni/texniti-noimosyni-den-exei-edraiosei-akoma-ti-thesi-tis-sta-dioikitika-symvoulia-ti-edeikse-ereyna-tis-deloitte/",
        "https://www.kathimerini.gr/society/reportaz/563444431/skeyasmata-gia-stytiki-dysleitoyrgia-kai-anavolika-diakinoyntai-paranoma-stin-ellada/",
        "https://www.iefimerida.gr/kosmos/oi-ipa-skeftontai-apostoli-kratoymenon-kai-amerikanon-stis-fylakes-froyria-toy-el-salbador",
        "https://www.economistas.gr/diethni/68953_pikrizoyn-oi-times-toy-kafe-o-rolos-tramp-kai-i-brazilia",
        "https://www.protothema.gr/world/article/1596642/o-mask-eleghei-pleon-to-sustima-pliromon-tou-amerikanikou-up-oikonomikon-se-theseis-kleidia-20arides-sunergates-tou/",
        "https://www.tanea.gr/2025/02/04/politics/polemos-neyron-voreia-tis-kritis-online/",
        "https://www.tanea.gr/2025/02/05/world/dixasmeni-metaksy-tis-sfyras-tramp-lfkai-tou-akmonos-poutin-i-ee-online/",
        "https://www.tanea.gr/2025/02/05/world/ipa-se-argia-oi-ypalliloi-tis-usaid-protofanis-kinisi-apo-tramp/"
    ], 'el'


def get_polish_urls():
    return [
        "https://www.rp.pl/kraj/art37748781-coraz-trudniej-sforsowac-granice-po-postawieniu-plotu-nielegalni-migranci-przerzucili-sie-na-inne-szlaki",
        "https://warszawa.wyborcza.pl/warszawa/7,54420,31636213,kaleta-w-muzeum-sztuki-nowoczesnej-probuje-sie-dzieciom-wciskac.html",
        "https://www.medonet.pl/zdrowie-i-wellbeing-pracownikow/stan-zdrowia-pracownikow,na-takim-l4-mozesz-jechac-z-dzieckiem-na-ferie--pamietaj-o-jednym,artykul,81303708.html",
        "https://www.gazetapolska.pl/29464-czego-boi-sie-tusk",
        "https://www.fakt.pl/wydarzenia/polska/warszawa/warszawa-po-marszu-niepodleglosci-zerwal-teczowa-flage-i-zaliczyl-wpadke/6fk6dxn",
        "https://superbiz.se.pl/wiadomosci/10-tys-zl-na-uchodzce-w-polsce-urzad-do-spraw-cudzoziemcow-ujawnia-kwoty-aa-zu9r-tmde-t7gJ.html"
    ], 'pl'


def get_english_urls():
    return [
        "https://tribunemag.co.uk/2025/01/how-finlands-left-is-beating-the-far-right",
        "https://tribunemag.co.uk/2025/02/hard-truths-captures-the-anxieties-of-modern-britain",
        "https://www.theguardian.com/uk/commentisfree",
        "https://www.theguardian.com/commentisfree/2025/feb/03/why-i-quit-background-noise-phone-silence-writers-retreat",
        "https://www.theguardian.com/commentisfree/2025/feb/02/heathrow-expansion-puts-the-government-on-the-flight-path-to-years-of-trouble-and-strife",
        "https://www.spectator.co.uk/article/ed-miliband-doesnt-understand-how-energy-prices-work/",
        "https://www.spectator.co.uk/article/is-the-uk-prepared-to-welcome-1-million-migrants-a-year/",
        "https://www.spectator.co.uk/article/how-deepseek-can-help-britain/"
    ], 'en'


def get_italian_urls():
    return [
        "https://www.avantionline.it/altro-che-educazione-alla-sessualita-la-regione-liguria-finanza-parrocchie-e-oratori/",
        "https://www.ilfattoquotidiano.it/2025/02/03/in-italia-si-ferma-la-crescita-economica-ma-t[…]aio-15-in-rialzo-su-dicembre-pesano-le-bollette/7862366/",
        "https://www.liberoquotidiano.it/news/giustizia/41517450/musumeci-scontro-toghe-cosa-dicono-sondaggi-riservati-sinistra-impazzisce.html",
        "https://contropiano.org/news/ambiente-news/2025/01/28/fermiamo-il-governo-del-ritorno-al-nucleare-0179773",
        "https://www.ilgiornale.it/news/borsa-e-mercati/i-dazi-fanno-tremare-borse-ecco-chi-soffre-pi-e-dove-trovare-2432335.html",
        "https://www.corriere.it/opinioni/25_gennaio_31/social-e-regole-l-insofferenza-contro-l-europa-2c996228-ab72-4166-9091-a7ecda29axlk.shtml",
        "https://beppegrillo.it/il-trasporto-deve-essere-pubblico-e-condiviso/",
        "https://www.ilpost.it/2025/02/01/whatsapp-dice-che-oltre-novanta-giornalisti-e-attivisti-sono-stati-spiati-sulla-sua-app/",
        "https://www.ilfoglio.it/politica/2025/02/03/news/abbiamo-speso-meno-di-un-terzo-dei-fondi-del-pnrr-i-dati-di-openpolis-7387399/"
    ], 'it'


languages = {
    'el': get_greek_urls,
    'pl': get_polish_urls,
    'en': get_english_urls,
    'it': get_italian_urls
}


def get_language_urls(language):
    method = languages.get(language, None)
    if method is None:
        raise RuntimeError(f'Invalid language provided! Supported: {languages.keys()}')
    return method()
