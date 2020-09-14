console.log('hola')


$('#exec').on('click', () => {
    let data = {
        "input_image": "lena.jpg",
        "output_image": "test.jpg",
        "num_cores": 4
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