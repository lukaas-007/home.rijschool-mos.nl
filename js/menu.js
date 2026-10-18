const menu_icon = document.querySelector('.menu-icon');
const menu = document.querySelector('.menu');

function closeMenu() {
    menu.classList.remove('menu-open');
    menu.classList.add('menu-closed');

    menu_icon.classList.remove('menu-icon-open');
    menu_icon.classList.add('menu-icon-closed');
}

menu_icon.addEventListener('click', () => {
    if (menu.classList.contains('menu-closed')) {
        // open menu
        menu.classList.remove('menu-closed');
        menu.classList.add('menu-open');

        menu_icon.classList.remove('menu-icon-closed');
        menu_icon.classList.add('menu-icon-open');
    } else {
        closeMenu();
    }
});

// close the menu after clicking a link on mobile
document.querySelectorAll('.menu-item').forEach((item) => {
    item.addEventListener('click', closeMenu);
});
