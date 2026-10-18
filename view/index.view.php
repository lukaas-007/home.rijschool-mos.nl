<!DOCTYPE html>
<html lang="nl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rijschool Mos</title>
    <meta name="description" content="Rijschool Mos - rijlessen met persoonlijke begeleiding. Plan een proefles en haal je rijbewijs.">

    <link rel='icon' href='img/favicon.jpg'>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/menu.css">
    <link rel="stylesheet" href="css/index.css">

    <script src="js/menu.js" defer></script>
</head>

<body>
    <header class="header">
        <a href="#top" class="header-logo">
            <img src="img/favicon.jpg" alt="" class="header-logo__icon">
            Rijschool <span>Mos</span>
        </a>

        <nav class="menu menu-closed">
            <div class="menu-items-wrapper">
                <a href="#over" class='menu-item'>Over ons</a>
                <a href="#werkwijze" class='menu-item'>Werkwijze</a>
                <a href="#lespakketten" class='menu-item'>Lespakketten</a>
                <a href="#contact" class='menu-item'>Contact</a>
                <a href="https://login.rijschool-mos.nl" class='menu-item menu-login'>Inloggen</a>
            </div>
        </nav>

        <div class="menu-icon menu-icon-closed">
            <span class="menu-icon__bar menu-icon__bar-1"></span>
            <span class="menu-icon__bar menu-icon__bar-2"></span>
            <span class="menu-icon__bar menu-icon__bar-3"></span>
        </div>
    </header>

    <main id="top">
        <section class="hero">
            <div class="hero-text">
                <p class="eyebrow">Rijlessen in <?= $contact['area'] ?></p>
                <h1>Haal je rijbewijs met <span>rust en vertrouwen</span></h1>
                <p class="hero-intro">
                    Persoonlijke begeleiding, een vaste instructeur en een duidelijk lesplan.
                    Zo weet je altijd waar je staat, en stap je goed voorbereid je examen in.
                </p>
                <div class="hero-buttons">
                    <a href="#contact" class="button button-primary">Plan een proefles</a>
                    <a href="#lespakketten" class="button button-secondary">Bekijk lespakketten</a>
                </div>
            </div>

            <div class="hero-image">
                <img src="img/auto.jpg" alt="Interieur van de lesauto van Rijschool Mos">
            </div>
        </section>

        <section class="usps">
            <div class="usp">
                <div class="usp__title">Vaste instructeur</div>
                <div class="usp__text">Je rijdt elke les met dezelfde instructeur.</div>
            </div>
            <div class="usp">
                <div class="usp__title">Ophalen vanaf huis</div>
                <div class="usp__text">De les begint en eindigt bij jou voor de deur.</div>
            </div>
            <div class="usp">
                <div class="usp__title">Online voortgang</div>
                <div class="usp__text">Bekijk je lessen en lesstof in je eigen omgeving.</div>
            </div>
        </section>

        <section class="section about" id="over">
            <img src="img/instructeur.jpg" alt="<?= $instructorName ?>, instructeur bij Rijschool Mos" class="about-image">

            <div class="about-text">
                <p class="eyebrow">Over ons</p>
                <h2>Maak kennis met <?= $instructorName ?></h2>
                <p>
                    Bij Rijschool Mos staat de leerling centraal. Iedereen leert op zijn eigen tempo,
                    daarom stemmen we elke les af op wat jij nodig hebt. Rustig uitleggen,
                    eerlijk advies en veel oefenen in het echte verkeer.
                </p>
                <p>
                    Je lest in een moderne, goed onderhouden Opel met dubbele bediening,
                    zodat je altijd veilig de weg op gaat.
                </p>
            </div>
        </section>

        <section class="section" id="werkwijze">
            <p class="eyebrow">Werkwijze</p>
            <h2>Zo werkt het</h2>

            <ol class="steps">
                <li class="step">
                    <div class="step__number">1</div>
                    <div class="step__title">Proefles</div>
                    <div class="step__text">We maken kennis en kijken samen hoeveel lessen je ongeveer nodig hebt.</div>
                </li>
                <li class="step">
                    <div class="step__number">2</div>
                    <div class="step__title">Lessen volgen</div>
                    <div class="step__text">Je doorloopt alle onderdelen stap voor stap, van de basis tot de snelweg.</div>
                </li>
                <li class="step">
                    <div class="step__number">3</div>
                    <div class="step__title">Voortgang volgen</div>
                    <div class="step__text">In je eigen account zie je je geplande lessen en waar je nu staat.</div>
                </li>
                <li class="step">
                    <div class="step__number">4</div>
                    <div class="step__title">Examen</div>
                    <div class="step__text">Ben je er klaar voor? Dan vragen we samen je praktijkexamen aan bij het CBR.</div>
                </li>
            </ol>
        </section>

        <section class="section" id="lespakketten">
            <p class="eyebrow">Lespakketten</p>
            <h2>Kies wat bij je past</h2>

            <div class="packages">
                <?php foreach ($packages as $package) { ?>
                    <div class="package <?= $package['featured'] ? 'package-featured' : '' ?>">
                        <?php if ($package['featured']) { ?>
                            <div class="package__badge">Meest gekozen</div>
                        <?php } ?>
                        <div class="package__name"><?= $package['name'] ?></div>
                        <p class="package__description"><?= $package['description'] ?></p>
                        <ul class="package__items">
                            <?php foreach ($package['items'] as $item) { ?>
                                <li><?= $item ?></li>
                            <?php } ?>
                        </ul>
                        <a href="#contact" class="button <?= $package['featured'] ? 'button-primary' : 'button-secondary' ?>">Aanvragen</a>
                    </div>
                <?php } ?>
            </div>
        </section>

        <section class="section contact" id="contact">
            <div class="contact-text">
                <p class="eyebrow">Contact</p>
                <h2>Klaar om te beginnen?</h2>
                <p>
                    Neem contact op voor een proefles of als je vragen hebt.
                    Een appje sturen mag ook, dan reageren we zo snel mogelijk.
                </p>
            </div>

            <div class="contact-options">
                <a href="https://wa.me/<?= $contact['whatsapp'] ?>" class="contact-option contact-option-whatsapp" target="_blank" rel="noopener">
                    <span class="contact-option__label">WhatsApp</span>
                    <span class="contact-option__value">Stuur een bericht</span>
                </a>
                <a href="tel:<?= $contact['phoneLink'] ?>" class="contact-option">
                    <span class="contact-option__label">Bellen</span>
                    <span class="contact-option__value"><?= $contact['phone'] ?></span>
                </a>
                <a href="mailto:<?= $contact['email'] ?>" class="contact-option">
                    <span class="contact-option__label">E-mail</span>
                    <span class="contact-option__value"><?= $contact['email'] ?></span>
                </a>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div>&copy; <?= date('Y') ?> Rijschool Mos</div>
        <div class="footer-credit">
            Made by
            <?php if ($madeBy['url']) { ?>
                <a href="<?= $madeBy['url'] ?>" target="_blank" rel="noopener"><?= $madeBy['name'] ?></a>
            <?php } else { ?>
                <?= $madeBy['name'] ?>
            <?php } ?>
        </div>
        <div class="footer-links">
            <a href="<?= $contact['instagram'] ?>" target="_blank" rel="noopener">Instagram</a>
            <a href="https://login.rijschool-mos.nl">Inloggen leerlingen</a>
        </div>
    </footer>
</body>

</html>
