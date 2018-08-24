$(document).ready(function(){
    var clnk = $(location).attr('pathname');
    var links=$('nav ul li a');
    var clink = links.filter("[href='"+clnk+"']");
    $(clink).addClass('well');
    $(clink).parent().addClass('active');
        
    //flash light
    for (h=0;h<2;h++){
        for (i=0;i<links.length;i++){
            $(links[i]).slideToggle(1000);
        };
    };
    //الضغط على التعريف 
    var dli=$('.row div');
    $(dli).on('click',slidmenu);
    function slidmenu(){
        var menu=$(this).attr('data-menu')
        $('nav #'+menu).children().addClass('alert alert-warning');
        $('nav #'+menu).children().slideToggle(1000,function(){
            $(this).removeClass('alert alert-warning');
            $(this).slideToggle(1000);
            });
    };
});
