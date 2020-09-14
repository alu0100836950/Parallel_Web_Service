console.log('cargar imagen')


$('#exec-mpi').on('click', () => {
    
    name_file = $('#file').val().split("\\")
    name_file = name_file[name_file.length -1]
    
    let data = {
        "algoritmo": "mpi",
        "input_image": name_file, 
        "output_image": "image_out_mpi.jpg",
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

$('#exec-openmp').on('click', () => {

    name_file = $('#file').val().split("\\")
    name_file = name_file[name_file.length -1]

    let data = {
        "algoritmo": "openmp",
        "input_image": name_file,
        "output_image": "image_out_openmp.jpg"  
    }

    $.ajax({
        url: `/exec/openmp.exe`,
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: res => {
            window.location.replace('/static/temp/output.jpg')
        }
    })

})