$(function() {
    $('#boardCont').delegate('.col', 'click',function(){
        var json = {
            row: parseInt($(this).parent('.row').index())+1,
            column: parseInt($(this).index())+1,

            play1Movs:parseInt($('#player1Movs').text()),
            play2Movs:parseInt($('#player2Movs').text()),

            play1: $('#player1').text(),
            play2: $('#player2').text()
        }

        console.log(json.play1Movs);
        console.log(json.play1Movs);
        $.ajax({
            url: '/A',
            data: JSON.stringify(json),
            dataType: 'json',
            contentType: 'application/json;charset=UTF-8',
            type: 'POST',
            success: function(response) {
               $("#boardCont").empty();  //Se limpia la matriz
               $("#boardCont").append(response.page); //Se vuelve agregar actualizada
                //Se sobre escriben los textos de los movimientos
               $("#player1Movs").text(response.play1movs);
               $("#player2Movs").text(response.play2movs);
               },
            error: function(error) {
                console.log(error);
            }
        });
    });
});



