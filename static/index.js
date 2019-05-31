$(function() {
    var clicked = false;
    var openlist =[]; 
    $('[id*="front"]').bind('click', function() {
    	let id = $(this).attr("id");  	
    	if (clicked) {
    		openlist.push(id);
    		while(1){
    			open();
    			if(openlist.length == 0 ){
    				break;
    			}
    		}
        	clicked = false;
        	return;
    	}
 	    // シングルクリックを受理、300ms間だけダブルクリック判定を残す
    	clicked = true;
    	setTimeout(function () {
        // ダブルクリックによりclickedフラグがリセットされていない
        //     -> シングルクリックだった
        	if (clicked) {
        		flag(id);
   			}
        	clicked = false;
    	}, 300);
    });
    
    function open(){
    	let id = openlist.pop();
    	let target = id.replace('front','back');
    	$('#' + id ).attr('hidden','true');
    	$('#' + target ).removeAttr('hidden');
    	
    	let val = document.getElementById(target).dataset.val;
    	if(val == 'B'){
    		alert("GAME OVER!!");
    	}else if( val == '0'){
    		let row =Number(id.replace('front-','').substr(0,1));
    		let col =Number(id.replace('front-','').substr(2,1));
    		check("back-"+ String(row - 1) + "-" + String(col - 1));
    		check("back-"+ String(row - 1) + "-" + String(col));
    		check("back-"+ String(row - 1) + "-" + String(col + 1));
    		check("back-"+ String(row) + "-" + String(col - 1));
    		check("back-"+ String(row) + "-" + String(col + 1));
    		check("back-"+ String(row + 1) + "-" + String(col - 1));
    		check("back-"+ String(row + 1) + "-" + String(col));
    		check("back-"+ String(row + 1) + "-" + String(col + 1));
    	}
    	return;
    }

   	function check(id){
   		if($('#' + id ).attr('hidden') == 'hidden'){
   			openlist.push(id.replace('back','front'));
   		}
   	}

    function flag(id){
    	if($('#' + id +' button').attr('hidden') != 'hidden'){
			$('#' + id +' button').attr('hidden','true');
    		$('#' + id +' input').removeAttr('hidden');
    	}else{
    		$('#' + id +' button').removeAttr('hidden');
    		$('#' + id +' input').attr('hidden','true');
    	}
    	return;
    }
});