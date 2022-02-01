function loading(opcao) {
    var time = 1000;
    if (opcao == 'login') {
        setTimeout(function () {
            window.location.href = "../home";
        }, time);
    }
    else {
        setTimeout(function () {
            window.location.href = "../logout";
        }, time);
    }
}