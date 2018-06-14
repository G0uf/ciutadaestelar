$(document).ready(function(){
    $( ".navbar" ).removeClass( "bg-dark" )
   var posicio_scroll = 0;
   var startchange = $('#startchange');
   var offset = startchange.offset();
   $(document).scroll(function() { 
      posicio_scroll = $(this).scrollTop();

      if(posicio_scroll > offset.top) {
          $(".navbar").css('background-color', "#303030");
       } else {
           
         $(".navbar").css('background-color', 'transparent');
       }
   });
   $(".navbar-toggler").on("click", function() {
       alert("A");
        //canviar color navbar
       $(".navbar").css('background-color', '#303030');
    });
});