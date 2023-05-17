let email = $('#reg-email')
let phone_number = $('#reg-phone-number')
let password1 = $('#reg-password1')
let password2 = $('#reg-password2')

email.blur(function () {
    if (email.val() !== '') {
        $('div#mark-email').removeClass('bg-slate-100 dark:bg-darkmode-800').addClass('bg-success')
    }
})

phone_number.blur(function () {
    if (phone_number.val() !== '') {
        $('div#mark-phone-number').removeClass('bg-slate-100 dark:bg-darkmode-800').addClass('bg-success')
    }
})

password1.blur(function () {
    if (password1.val() !== '') {
        $('div#mark-password1').removeClass('bg-slate-100 dark:bg-darkmode-800').addClass('bg-success')
    }
})

password2.blur(function () {
    if (password2.val() !== '') {
        $('div#mark-password2').removeClass('bg-slate-100 dark:bg-darkmode-800').addClass('bg-success')
    }
})
