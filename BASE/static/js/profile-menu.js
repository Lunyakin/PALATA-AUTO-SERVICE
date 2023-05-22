function active_class() {
    $("#user-menu a").each(function () {
        let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
        let link = this.href;
        if (location == link) {
            $(this).parent().addClass('active')
        }

    });
}

active_class()