var table;
var data;
function listarOrdenes (urlAll) {
    console.log(urlAll);
    var table = $('#myTable').DataTable( {
        "ajax": {
            "url":  host+urlAll,
            "dataSrc": ""
        },
        "columns": [
            { data: "descripcion" },
            { data: "proveedor" },
            { data: "costo" },
        ]
        } );
}
