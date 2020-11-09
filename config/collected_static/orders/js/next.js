$(document).ready(function() {
    $('#num_2').show(); 
    $('#num_3').show(); 
    $('#num_4').show(); 
    $('#num_11').hide(); 
    $('#anchor_right').click(function(e){
        // e.stopPropagation();
        e.preventDefault();
        $('#num_2').hide(); 
        $('#num_3').hide(); 
        $('#num_4').hide(); 
        $('#num_11').show(); 
    });   
    $('#anchor_left').click(function(e){
        // e.stopPropagation();
        e.preventDefault();
        $('#num_2').show(); 
        $('#num_3').show(); 
        $('#num_4').show(); 
        $('#num_11').hide(); 
    return false;
    });
});