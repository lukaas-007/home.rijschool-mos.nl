<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rijschool-mos</title>

    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

    <link rel='icon' href='img/favicon.jpg'>

    <link rel="stylesheet" href="css/menu.css">
    <link rel="stylesheet" href="css/index.css">
</head>

<body>
    <div class="menu-icon menu-icon-closed ">
        <span class="menu-icon__bar menu-icon__bar-1"></span>
        <span class="menu-icon__bar menu-icon__bar-2"></span>
        <span class="menu-icon__bar menu-icon__bar-3"></span>
    </div>

    <div class="menu menu-closed">
        <div class="menu-items-wrapper">
            <a href="overzicht.php" class='menu-item menu-selected'>Overzicht</a>
            <a href="lessen.php" class='menu-item'>Lessen</a>
            <a href="lestof.php" class='menu-item'>Lestof</a>
        </div>
    </div>

    <main>
        <div class='overzicht-lessen-over overzicht-item'>
            Je hebt nog <?= $lessonsLeft ?> lessen
        </div>
        <div class='overzicht-module overzicht-item'>
            Je bent nu bij: <?= $upcomingModule ?><br>
            Onderdeel <?= $upcomingModuleIndex ?> van de <?= $moduleCount ?>
        </div>
        <div class='overzicht-aanstaande-les overzicht-item'>
            <div class='overzicht-aanstaande-les__title'>
                Aanstaande les
            </div>

            <div class='overzicht-aanstaande-les__inhoud'>
                <div class="aanstaande-les-left-side">
                    <div class='overzicht-aanstaande-les__date'>
                        <?= $nextLesson['date'] ?>
                    </div>

                    <div class='overzicht-aanstaande-les__time'>
                        <?= $nextLesson['startTime'] ?> - <?= $nextLesson['endTime'] ?>
                    </div>
                </div>

                <div class='aanstaande-les-right-side'>

                    <div class='overzicht-aanstaande-les__note'>
                        <?= $nextLesson['note'] ?>
                    </div>

                    <div class='overzicht-aanstaande-les__note'>
                        <?= $upcomingModule ?>
                    </div>
                </div>

            </div>

        </div>
    </main>
</body>

</html>