console.log('cargar imagen')


$('#exec').on('click', () => {

    let data = {
        "input_image": "lena.jpg",
        "output_image": "test.jpg",
        "num_cores": parseInt($('#number-cores').val())
    }

    $.ajax({
        url: `/exec/mpi.exe`,
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: res => {
            window.location.replace('/static/temp/output.jpg')
        }
    })

})