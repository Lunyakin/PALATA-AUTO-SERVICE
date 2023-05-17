let dark_mod = $("#dark-mode-switcher")

function change() {
    let html = $('#html');

    if ($(html).hasClass("dark")) {
        $(html).removeClass("dark").addClass("light");
    } else {
        $(html).removeClass("light").addClass("dark");
    }
}

function change_dark_mode() {
    let switcher = $("#dark-mode-switcher-toggle");

    if ($(switcher).hasClass("dark-mode-switcher__toggle--active")) {
        $(switcher).removeClass("dark-mode-switcher__toggle--active")
        change()
    } else {
        $(switcher).addClass("dark-mode-switcher__toggle--active");
        change()
    }
}

dark_mod.on('click', change_dark_mode)