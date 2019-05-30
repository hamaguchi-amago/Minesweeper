$(function() {
    var clicked = false; 
    $('[id*="front"]').bind('click', function() {
    	let id = $(this).attr("id");  	
    	if (clicked) {

    		open(id);
        	clicked = false;
        	return;
    	}
 	    // シングルクリックを受理、300ms間だけダブルクリック判定を残す
    	clicked = true;
    	setTimeout(function () {
        // ダブルクリックによりclickedフラグがリセットされていない
        //     -> シングルクリックだった
        	if (clicked) {
        		
   			}
        	clicked = false;
    	}, 300);
    });
    function open(id){
    	let target = id.replace('front','back');
    	$('#' + id ).attr('hidden','true');
    	$('#' + target ).removeAttr('hidden');
    }
});