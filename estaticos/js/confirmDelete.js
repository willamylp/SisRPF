function ConfirmarDelete(valor, tipoDelete) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-success',
        },
        buttonsStyling: true
    })

    swalWithBootstrapButtons.fire({
        title: 'Você tem certeza?',
        text: "Você não poderá reverter isso!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: '✓ Deletar',
        cancelButtonText: '✗ Cancelar',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            swalWithBootstrapButtons.fire(
                'Deletado!',
                'REGISTRO DELETADO COM SUCESSO!',
                'success'
            )
            var url;
            var urlAtual = window.location.href;
            var urlAtual = urlAtual.split('/');
            if (tipoDelete == 'integrante') {
                if (urlAtual.length > 6) {
                    url = '../../DeletarIntegrante/' + valor;
                } else {
                    url = '../DeletarIntegrante/' + valor;
                }
            }
            else {
                if (urlAtual.length > 6) {
                    url = '../../DeletarProntuario/' + valor;
                } else {
                    url = '../DeletarProntuario/' + valor;
                }
            }
            location.href = url;
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado!',
                'O REGISTRO <b>NÃO</b> FOI DELETADO!',
                'info'
            )
        }
    })
}