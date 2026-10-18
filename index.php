<?php

$contact = [
    'phone' => '06-12345678',
    'phoneLink' => '+31612345678',
    'whatsapp' => '31612345678',
    'email' => 'info@rijschool-mos.nl',
    'area' => 'Regio Spijkenisse, Rotterdam',
    'instagram' => 'https://www.instagram.com/rijschoolmos',
];

$instructorName = 'Alvindo';

$madeBy = [
    'name' => 'Lucas van Briemen',
    'url' => 'https://ltvb.nl',
];

$packages = [
    [
        'name' => 'Proefles',
        'description' => 'Maak kennis met de auto en de instructeur. Na afloop krijg je een advies over hoeveel lessen je nodig hebt.',
        'items' => ['60 minuten', 'Vrijblijvend advies', 'Ophalen vanaf huis'],
        'featured' => false,
    ],
    [
        'name' => 'Pakket 20 lessen',
        'description' => 'Een goede basis voor de meeste leerlingen, inclusief praktijkexamen.',
        'items' => ['20 lessen van 60 minuten', 'Praktijkexamen CBR', 'Online voortgang bekijken'],
        'featured' => true,
    ],
    [
        'name' => 'Losse les',
        'description' => 'Voor extra oefenen, of als je al ervaring hebt en alleen nog wat bijsturing nodig hebt.',
        'items' => ['60 minuten', 'Flexibel inplannen'],
        'featured' => false,
    ],
];

include_once 'view/index.view.php';
